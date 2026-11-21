import json


def load_city(name):

    path = name + ".json"

    with open(path, encoding='utf-8') as f:

        return json.load(f)


cities = ["krasnodar", "sochi", "maykop"]
city_temperature = []
for city in cities:

    try:
        notation = load_city(city)
        city_temperature.append(notation)
        print(f" In {notation['city']} temperature is {notation['temperature']}")
    except FileNotFoundError:
        print(f"This city {city} doesn't have any data.")

max_t = city_temperature[0]
min_t = city_temperature[0]

for temperature in city_temperature:
    if temperature['temperature'] > max_t['temperature']:
        max_t = temperature

    if temperature['temperature'] < min_t['temperature']:
        min_t = temperature

with open('summary_temperature.json', 'w', encoding='utf-8') as f:

    json.dump([min_t, max_t], f, encure_ascii=False, indent=2)