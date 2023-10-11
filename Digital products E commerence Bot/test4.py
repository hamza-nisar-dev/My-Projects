from web3 import Web3
import json
import requests
api_key = "M76BUETIHMDYXYS13P9SJF9I4WB2S3WS4K"
contract_address = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
etherscan_api_url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={api_key}"
response = requests.get(etherscan_api_url)
data = response.json()
abi = data["result"]
print(abi)
abiu=json.load(abi)
bsc_rpc_url = 'https://bsc-dataseed.binance.org/'


web3 = Web3(Web3.HTTPProvider(bsc_rpc_url))


factory_contract = web3.eth.contract(address=contract_address, abi=abiu)

total_pairs = factory_contract.functions.allPairsLength().call()
print(total_pairs)
token_has_pairs = False
for i in range(total_pairs):
    pair_address = factory_contract.functions.allPairs(i).call()
    print(pair_address)
