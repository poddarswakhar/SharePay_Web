from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account

# Connect to Infura using the project ID and endpoint
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/7e2ee82c1a1f4a8a9b3b75b22162b90a'))

# Add the PoA middleware if using a PoA chain like Rinkeby
#w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Set the sending and receiving addresses
# sender_private_key="0x896c9790b20f73c0e9186889e0bc4fa74df9963a474e3cd87b811b5c2d7100cb"
# account = Account.from_key(sender_private_key)
# sender_address= account.address
contract_address = '0xBAA8720658D95D3239920c3aAa38BDBE44f8cC3D'
# print(sender_address)


# Load the sender account using the private key
# sender_account = Account.from_key(sender_private_key)

# Define the transaction parameters
nonce = w3.eth.get_transaction_count(contract_address)
gas_price = w3.eth.gas_price
gas_limit = 100000


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
contract_function = w3.eth.contract(address=contract_address, abi=ABI).functions.withdraw()
tx_data = contract_function.build_transaction({'gas': gas_limit, 'gasPrice': gas_price, 'nonce': nonce})

# Sign the transaction using the sender's private key
# signed_txn = sender_account.sign_transaction(tx_data)

# Send the signed transaction to the network
tx_hash = w3.eth.send_raw_transaction(tx_data)

# Wait for the transaction to be mined
#tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Print the transaction receipt
#print(tx_receipt)