import requests

#import json
#
#
#all_weather_code = {0: "sunny",
#                1: "cloudy",
#                2: "over cast",
#                61: "rain",
#                63: "thunderstorm",
#                65: "snow"}
#
#
#
#with open("weather.json", encoding='utf-8') as f:
#    data = json.load(f)
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
#    print(weather_city)data.append({"city": "Volgograd", "temperature": 12, "wind": 6})with open("weather_new.json", "w", encoding="utf-8") as f:    json.dump(data, f, ensure_ascii=False, indent=4)

#def build_url(lat, lon):
#    url = (
#        "https://api.open-meteo.com/v1/forecast"
#        f"?latitude={lat}&longitude{lon}"
#        "&current=temperature_2m_speed_10m"
#        )
#    return url
#
#print(build_url(44.61, 40.11))
#print(build_url(43.60, 39.73))


def build_request(request):
    url = (
        f"https://www.google.com/search?q={request}"
    )

    return url

request = input()
user_request = build_request(request)

#url = (
#    f"https://www.google.com/search?q={request}"
#)
#
#response = requests.get(url)

print(build_request(request))
