import requests

def get_location(cuantry, key):
    url_get_location = rf'https://api.openweathermap.org/geo/1.0/direct?q={cuantry}&appid={key}'
    location = requests.get(url_get_location).json()
    return location
