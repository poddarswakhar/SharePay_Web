from web3 import Web3
from web3.middleware import geth_poa_middlewareweb3 
from eth_account import Account

# Connect to Infura using the project ID and endpoint
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/7e2ee82c1a1f4a8a9b3b75b22162b90a'))

# Add the PoA middleware if using a PoA chain like Rinkeby
#w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Set the sending and receiving addresses
sender_address = '0x14d4ACD172e4CEe6E54F9239a405E8aCb5530EbF'
sender_private_key = '0xb3ec03a7b5b62cde1c6b7e73c598376af2da7be3af9e00496ed87a4aabc828f4'
contract_address = '0xAe5E0fa16f95f155cfeB69c80d819Ced263da387'

# Load the sender account using the private key
sender_account = Account.from_key(sender_private_key)

# Define the transaction parameters
nonce = w3.eth.get_transaction_count(sender_address)
gas_price = w3.eth.gas_price
gas_limit = 100000
value = w3.to_wei(0.0001, 'ether')

ABI = [
    {
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
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

# from eth_account import Account
# from web3 import Web3, EthereumTesterProvider
# from ethtoken.abi import EIP20_ABI
# w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/7e2ee82c1a1f4a8a9b3b75b22162b90a'))
# connected = w3.isConnected()
# print(connected)
#
# my_private_key = '0xb3ec03a7b5b62cde1c6b7e73c598376af2da7be3af9e00496ed87a4aabc828f4'
# my_public_key = '0x14d4ACD172e4CEe6E54F9239a405E8aCb5530EbF'
# rec_add = '0xAe5E0fa16f95f155cfeB69c80d819Ced263da387'
#
# nonce = w3.eth.getTransactionCount('0x14d4ACD172e4CEe6E54F9239a405E8aCb5530EbF')
# print(nonce)
#
#
# transaction = {
#     'to': '0xAe5E0fa16f95f155cfeB69c80d819Ced263da387', # Replace with the recipient address
#     'value': w3.toWei(0.00001, 'ether'), # Replace with the amount you want to send in ETH
#     'gas': 40000, # This is the default gas limit for a simple ETH transfer
#     'gasPrice': w3.toWei('10000', 'gwei'), # Replace with the gas price you want to use (in Gwei)
#     'nonce': nonce, # Replace with the sender address
# }
#
# abi = [
#     {
#         "inputs": [],
#         "name": "deposit",
#         "outputs": [],
#         "stateMutability": "payable",
#         "type": "function"
#     },
#     {
#         "inputs": [
#             {
#                 "internalType": "uint256",
#                 "name": "amount",
#                 "type": "uint256"
#             }
#         ],
#         "name": "withdraw",
#         "outputs": [],
#         "stateMutability": "nonpayable",
#         "type": "function"
#     },
#     {
#         "inputs": [
#             {
#                 "internalType": "address",
#                 "name": "",
#                 "type": "address"
#             }
#         ],
#         "name": "balances",
#         "outputs": [
#             {
#                 "internalType": "uint256",
#                 "name": "",
#                 "type": "uint256"
#             }
#         ],
#         "stateMutability": "view",
#         "type": "function"
#     },
#     {
#         "inputs": [
#             {
#                 "internalType": "uint256",
#                 "name": "",
#                 "type": "uint256"
#             }
#         ],
#         "name": "users",
#         "outputs": [
#             {
#                 "internalType": "address",
#                 "name": "",
#                 "type": "address"
#             }
#         ],
#         "stateMutability": "view",
#         "type": "function"
#     }
# ]
# #
# # signed = w3.eth.account.signTransaction(transaction, private_key=my_private_key)
# #
# # tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
# #
# # receipt = w3.eth.waitForTransactionReceipt(tx_hash)
# # print(receipt)
#
# contract = w3.eth.contract(address=rec_add, abi=abi)
#
# transaction = {
#     'to': '0xAe5E0fa16f95f155cfeB69c80d819Ced263da387', # Replace with the recipient address
#     'value': w3.toWei(0.00001, 'ether'), # Replace with the amount you want to send in ETH
#     'gas': 40000, # This is the default gas limit for a simple ETH transfer
#     'gasPrice': w3.toWei('10000', 'gwei'), # Replace with the gas price you want to use (in Gwei)
#     'nonce': nonce, # Replace with the sender address
# }
#
# signed = w3.eth.account.signTransaction(transaction, private_key=my_private_key)
#
# # call the deposit function with a value of 1 ETH
# tx_hash = contract.functions.deposit().transact(signed)
#
#
#
# # wait for the transaction to be mined and get the receipt
# tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#
# # print the receipt to confirm the transaction was successful
# print(tx_receipt)
#
#
#
#