import requests

def get_location(cuantry, key):
    url_get_location = rf'https://api.openweathermap.org/geo/1.0/direct?q={cuantry}&appid={key}'
    location = requests.get(url_get_location).json()
    return location

def get_weather(cuantry, key):
    url_get_weather = rf'https://api.openweathermap.org/data/2.5/forecast?q={cuantry}&appid={key}'
    weather = requests.get(url_get_weather).json()
    return weather


print(get_weather('yemen', 'a10e75d5c94c635e8496808e1a2918a5'))