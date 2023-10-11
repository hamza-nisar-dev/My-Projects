from web3 import Web3
import json
# Define the BSC RPC URL
bsc_rpc_url = 'https://bsc-dataseed.binance.org/'

# Create a Web3 instance
web3 = Web3(Web3.HTTPProvider(bsc_rpc_url))

# Token address for the token you want to find trading pairs for
token_address = '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'
with open('fs.json', 'r') as abi_file:
    panAbi = json.loads('[{"constant":true,"inputs":[{"name":"tokenA","type":"address"},{"name":"tokenB","type":"address"}],"name":"getPair","outputs":[{"name":"pair","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')
panRouterContractAddress = '0x13f4EA83D0bd40E75C8222255bc855a974568Dd4'         
router_contract= web3.eth.contract(address=panRouterContractAddress, abi=panAbi)

pairs = router_contract.functions.getTradingPairs(token_address).call()

if pairs:
    print(f"Trading pairs for token {token_address}:")
    for pair in pairs:
        print(pair)
else:
    print(f"No trading pairs found for token {token_address}")
