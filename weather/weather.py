import json


all_weather_code = {0: "sunny",
                1: "cloudy",
                2: "over cast",
                61: "rain",
                63: "thunderstorm",
                65: "snow"}



with open("weather.json", encoding='utf-8') as f:
    data = json.load(f)
#
#print(f"In a city {data['city']} temperature is {data['temperature']} *C")
#
#with open("response.json", encoding='utf-8') as f:
#    data1 = json.load(f)
#    for code in all_weather_code:
#        data1['current']['weather_code'] = all_weather_code[code]
#print(f"In Maykop {data1['current']['temperature_2m']} and {data1['current']['wind_speed_10m']} and {data1['current'][code]}")

#with open("weather.json", encoding="utf-8") as f:
#    data = json.load(f)
#
#for item in data:
#    weather_cities = {}
#    weather_city = item['city']
#    print(weather_city)
data.append({"city": "Volgograd", "temperature": 12, "wind": 6})

with open("weather_new.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
