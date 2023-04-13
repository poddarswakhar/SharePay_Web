import os
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/7e2ee82c1a1f4a8a9b3b75b22162b90a'))

account = w3.eth.account.create()

print("Account address:", account.address)
print("Private key:", account._private_key.hex())








