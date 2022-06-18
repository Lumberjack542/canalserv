from pprint import pprint

import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
pprint(data['Valute']['USD'])

pprint(data['Valute']['USD']["Value"])
