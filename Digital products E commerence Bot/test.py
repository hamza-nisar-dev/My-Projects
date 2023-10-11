from web3 import Web3
import json

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
with open('fs.json', 'r') as abi_file:
    panAbi = json.load(abi_file)
panRouterContractAddress = '0x10ED43C718714eb63d5aA57B78B54704E256024E'         
contract = web3.eth.contract(address=panRouterContractAddress, abi=panAbi)

baseCurrency = web3.to_checksum_address("0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56")    #BUSD

tokenToSell = web3.to_checksum_address("0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82")     #FINE

amountOfTokens =1


amountOut = contract.functions.getAmountsOut(
    web3.to_wei(amountOfTokens, "ether"), [tokenToSell, baseCurrency]
).call()

priceOfOneTokenInBaseUnit = amountOut[1] / web3.to_wei(amountOfTokens, "ether")


print(priceOfOneTokenInBaseUnit)
