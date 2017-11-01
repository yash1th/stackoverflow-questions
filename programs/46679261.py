import requests

params={'q': 'NASDAQ:AAPL','expd': 19, 'expm': 1, 'expy': 2018, 'output': 'json'}
response = requests.get('https://www.google.com/finance/option_chain', params=params)

print(response.url)
print(response.request.url)