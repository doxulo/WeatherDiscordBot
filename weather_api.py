import requests


def get_weather(city, api_key):
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(base_url)
    return response.json()
