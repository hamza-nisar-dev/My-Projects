import requests

api_key = '1D1UXRRI0FK50QZU'
endpoint = 'https://www.alphavantage.co/query'
params = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'ETH',
    'to_currency': 'USD',
    'apikey': api_key
}
response = requests.get(endpoint, params=params)
data = response.json()
eth= float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
aso=1700/eth
ase=round(aso,4)
print(ase)

