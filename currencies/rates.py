import requests


url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
data = response.json()
valute = input('введите код валюты: ').split(' ',1)
a = []
if valute[0] =='?':
    for key in data["Valute"]:
        a.append(key)
    print(f'вот все коды валют: {" ".join(a)}')
    exit()
m = 0
vlaue1 = data['Valute'][valute[0]]["Value"]
vlaue2 = data['Valute'][valute[1]]["Value"]
if vlaue1>vlaue2:
    m = f'Дороже:{data["Valute"][valute[0]]["Name"]},его курс на данный момент {data["Valute"][valute[0]]["Value"]}'
else:
    m = f'Дороже:{data["Valute"][valute[1]]["Name"]},его курс на данный момент {data["Valute"][valute[1]]["Value"]}'
# with open('answer.txt','a', encoding='utf-8') as f:
#     f.write(m+'\n')