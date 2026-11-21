import requests


url = "https://www.cbr-xml-daily.ru/daily_json.js"

response = requests.get(url)
data = response.json()
valute = data['Valute']
previous_url = "https:" + data['PreviousURL'].replace("\\", "")
response = requests.get(previous_url)
previous_data = response.json()

