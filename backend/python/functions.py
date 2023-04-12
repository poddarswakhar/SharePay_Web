from eth_account import Account
from web3 import Web3
from solcx import install_solc
install_solc(version='latest')
from solcx import compile_source


def deposit(sender_address,sender_private_key,contract_address,abi):
    w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/7e2ee82c1a1f4a8a9b3b75b22162b90a'))
    sender_account = Account.from_key(sender_private_key)
    nonce = w3.eth.get_transaction_count(sender_address)
    gas_price = w3.eth.gas_price
    gas_limit = 100000
    value = w3.to_wei(0.5, 'ether')
    contract = w3.eth.contract(address=contract_address, abi=abi)
    tx = contract.functions.deposit().buildTransaction({
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
        'value': value
    })
    signed_tx = sender_account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt)

def withdraw(sender_address,sender_private_key,contract_address,abi):
    w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/7e2ee82c1a1f4a8a9b3b75b22162b90a'))
    sender_account = Account.from_key(sender_private_key)
    nonce = w3.eth.get_transaction_count(sender_address)
    gas_price = w3.eth.gas_price
    gas_limit = 100000
    contract = w3.eth.contract(address=contract_address, abi=abi)
    tx = contract.functions.withdraw().buildTransaction({
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
    })
    signed_tx =sender_account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt)

def deployContract(private_key):
    # with open('../contracts/SharePay.sol', 'r') as file:
    #     source_code = file.read()

    # compiled_sol = compile_source(source_code)

    #contract_interface = compiled_sol['SharePay.sol:SharePay']

    # abi = contract_interface['abi']
    # bytecode = contract_interface['bin']


    compiled_sol = compile_source(
        '''
    // SPDX-License-Identifier: MIT
    pragma solidity ^0.8.0;

    contract MoneyPool {
        mapping(address => uint) public balances;
        address[] public users;
        address payable netflix = payable(0x7d1017267455FAFec280F51b3Fb6E139Dfd8CDb0);

        function deposit() public payable {
            if (balances[msg.sender] == 0) {
                users.push(msg.sender);
            }
            balances[msg.sender] += msg.value;
        }

        function withdraw() public {

            uint totalBalance = address(this).balance;
            require(1 <= totalBalance, "Insufficient funds in the money pool");

            // for (uint i = 0; i < users.length; i++) {
            //     address user = users[i];
            //     uint userBalance = balances[user];
            //     uint userShare = (userBalance * amount) / totalBalance;

            //     balances[user] -= userShare;
            //     payable(user).transfer(userShare);
            // }
            payable(netflix).transfer(100000000000000000);
        }
    }
        ''',
        output_values=['abi', 'bin']
    )

    # retrieve the contract interface
    contract_id, contract_interface = compiled_sol.popitem()

    # get bytecode / bin
    bytecode = contract_interface['bin']

    # get abi
    abi = contract_interface['abi']

    # connect to the network
    w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/7e2ee82c1a1f4a8a9b3b75b22162b90a'))
    account = Account.from_key(private_key)
    w3.eth.defaultAccount = account.address

    SharePay = w3.eth.contract(abi=abi, bytecode=bytecode)
        # Submit the transaction that deploys the contract
    construct_txn = SharePay.constructor().build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 1728712,
        'gasPrice': w3.to_wei('21', 'gwei')})

    signed = account.signTransaction(construct_txn)

    tx_hash=w3.eth.send_raw_transaction(signed.rawTransaction)

    # Wait for the transaction to be mined, and get the transaction receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Get the contract address
    contract_address = tx_receipt.contractAddress

    #set gas stratergy
    #web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)
    #create a contract instance with the newly-deployed address
    SharePay= w3.eth.contract(
        address=contract_address,
        abi=abi
    )

    print("Contract address:", contract_address)
    return [contract_address, abi]