from web3 import Web3

# Connect to Ethereum node (Infura / Alchemy / local node)
RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Check connection
if not w3.is_connected():
    raise Exception("Connection failed")

# Account setup (DO NOT hardcode in production)
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(PRIVATE_KEY)
sender = account.address

# Contract details
CONTRACT_ADDRESS = Web3.to_checksum_address("0xYourContractAddress")
CONTRACT_ABI = [
    {
        "inputs": [],
        "name": "yourFunction",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Build transaction
nonce = w3.eth.get_transaction_count(sender)

tx = contract.functions.yourFunction().build_transaction({
    "from": sender,
    "nonce": nonce,
    "gas": 200000,
    "gasPrice": w3.to_wei("20", "gwei"),
    "chainId": 1
})

# Sign transaction
signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)

# Send transaction
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print("Transaction sent!")
print("Tx hash:", w3.to_hex(tx_hash))
