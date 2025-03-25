import requests

def get_weather(city, api_key):
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(base_url)
    return response.json()

def get_forecast(city, api_key, days = 3):
    base_url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}"
    response = requests.get(base_url)
    return response.json()

def get_alerts(city, api_key):
    base_url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&alerts=yes"
    response = requests.get(base_url)
    return response.json()

def get_hourly_forecast(city, api_key):
    base_url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&hours=24"
    response = requests.get(base_url)
    return response.json()