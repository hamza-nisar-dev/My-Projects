from web3 import Web3

import json
# Replace with your Ethereum node URL
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/2ccbd7fd1aaa4afe8e0fe41e86ee991f"))

# Replace with actual contract addresses
token_contract_address = w3.to_checksum_address('0x1ec9f8d4b77aa4243d90d5dc61a57c95241af7a9')
router_contract_address =w3.to_checksum_address ('0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D')
pair_address = w3.to_checksum_address('0x5bd8dcc7e18a873da2293ea7bc5efd3ef968066e')

# Load ABI from JSON file
with open('cv.json', 'r') as abi_file:
    router_abi = json.load(abi_file)
router_contract = w3.eth.contract(address=router_contract_address, abi=router_abi)
print(router_contract.functions)
print(router_contract)
# Get token amount in exchange for some ETH
def get_token_price_in_eth():
    eth_amount = w3.to_wei(1,"ether")# 1 ETH worth of tokens
    amounts_out = router_contract.functions.getAmountsOut(eth_amount, [token_contract_address, pair_address]).call()
    print(amounts_out)
    token_amount = amounts_out[1] 
    print(token_amount) # Amount of tokens received

    return token_amount / 1e18  # Convert to token units

try:
    token_price_in_eth = get_token_price_in_eth()
    print(f'Token Price in ETH: {token_price_in_eth}')
except Exception as e:
    print('Error:', e)
