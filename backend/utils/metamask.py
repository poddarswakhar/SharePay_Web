from web3 import Web3
from eth_account import Account

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/7e2ee82c1a1f4a8a9b3b75b22162b90a'))
if w3.is_connected():
    # Connect to MetaMask
    provider = w3.currentProvider
    if provider is not None:
        web3 = Web3(provider)
        if web3.eth.accounts:
            user_address = web3.eth.accounts[0]
        else:
            print('No accounts found in MetaMask')
    else:
        print('MetaMask not found')
else:
    print('Web3 is not connected')

from web3 import Transaction

# Create the transaction object
tx = Transaction({
    'from': user_address,
    'to': '0x7d1017267455FAFec280F51b3Fb6E139Dfd8CDb0',
    'value': web3.toWei(0.1, 'ether'),
    'gasPrice': web3.toWei(50, 'gwei'),
    'nonce': web3.eth.getTransactionCount(user_address)
})

# Estimate the gas cost
tx_gas = tx.estimateGas()
tx_gas_price = web3.eth.gasPrice
tx_cost = tx_gas * tx_gas_price
from eth_account.messages import defunct_hash_message

# Prepare the message to sign
message = defunct_hash_message(primitive=tx)
message_hex = message.hex()

# Prompt the user to sign the message in MetaMask
signature = web3.eth.personal.sign(message_hex, user_address)

# Update the transaction with the signature
tx.rawHash = tx.hash()
tx.r, tx.s, tx.v = web3.eth.account._parse_sig(signature)

# Send the transaction to the network
tx_hash = web3.eth.sendRawTransaction(tx.rawTransaction)
print(f'Transaction sent: {tx_hash.hex()}')
