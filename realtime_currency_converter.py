import requests
import json
key = "AVK6S1C5YK1EOPPA"

country1 = input('Enter the code of the country you want to convert :')
amount = float(input('Enter the amount in %s' % country1))
country2 = input('Enter the code of the country you want to get converted:')

base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = base_url + '&from_currency=' + country1 + '&to_currency=' + country2 + '&apikey=' + key




response = requests.get(main_url)
data = response.json()['Realtime Currency Exchange Rate']

rate = round(float(data['5. Exchange Rate']), 2)

print('\nThe exchange rate for', country1, 'to', country2, 'is:', rate)

result = rate * amount
print('')
print(amount, country1, 'is', result, country2)


