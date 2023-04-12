#https://web3py.readthedocs.io/en/stable/web3.contract.html#contract-example

import os
from eth_account import Account
from solcx import install_solc
from web3.gas_strategies.rpc import rpc_gas_price_strategy

install_solc(version='latest')

from web3 import Web3
from solcx import compile_source

# with open("MyContract.sol", "r") as f:
#     contract_source_code = f.read()

# compiled_sol = compile_source(contract_source_code)


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

#set pre-funded account as sender

#private_key = os.environ["PRIVATE_KEY"]

#hardcoded private key
private_key="0x896c9790b20f73c0e9186889e0bc4fa74df9963a474e3cd87b811b5c2d7100cb"
account = Account.from_key(private_key)
w3.eth.defaultAccount = account.address



# create the contract
Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction that deploys the contract
construct_txn = Greeter.constructor().build_transaction({
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
greeter = w3.eth.contract(
    address=contract_address,
    abi=abi
)

print("Contract address:", contract_address)

