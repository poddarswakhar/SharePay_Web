from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account



# Connect to Infura using the project ID and endpoint
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/7e2ee82c1a1f4a8a9b3b75b22162b90a'))

# Add the PoA middleware if using a PoA chain like Rinkeby
#w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Set the sending and receiving addresses
sender_address = '0x05fE208517baD991BE7D33eC294aF0ad3245b38a'
sender_private_key = '0xcbbfca728656945d84315e2930c355a76341f3b32d69bb3f4cd8d15a11d03c03'
contract_address = '0xBAA8720658D95D3239920c3aAa38BDBE44f8cC3D'


# Load the sender account using the private key
sender_account = Account.from_key(sender_private_key)

# Define the transaction parameters
nonce = w3.eth.get_transaction_count(sender_address)
gas_price = w3.eth.gas_price
gas_limit = 100000
value = w3.to_wei(0.1, 'ether')

ABI = [
    {
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "balances",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "users",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
# Define the transaction data for sending Ether to the contract
contract_function = w3.eth.contract(address=contract_address, abi=ABI).functions.deposit()
tx_data = contract_function.build_transaction({'value': value, 'gas': gas_limit, 'gasPrice': gas_price, 'nonce': nonce})

# Sign the transaction using the sender's private key
signed_txn = sender_account.sign_transaction(tx_data)

# Send the signed transaction to the network
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for the transaction to be mined
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Print the transaction receipt
print(tx_receipt)