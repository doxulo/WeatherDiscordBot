import requests
import os

def get_weather(city, api_key):
    base_url = os.getenv('WEATHER_API_BASE_URL', 'http://api.weatherapi.com/v1') + f"/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {"error": "Request failed"}
    except ValueError:
        return {"error": "Invalid JSON response"}
def get_alerts(city, api_key):
    base_url = os.getenv('WEATHER_API_BASE_URL', 'http://api.weatherapi.com/v1') + f"/forecast.json?key={api_key}&q={city}&alerts=yes"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return {"error": "Invalid JSON response"}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {"error": "Request failed"}

def get_hourly_forecast(city, api_key):
    base_url = os.getenv('WEATHER_API_BASE_URL', 'http://api.weatherapi.com/v1') + f"/forecast.json?key={api_key}&q={city}&hours=24"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {"error": "Request failed"}
    except ValueError:
        return {"error": "Invalid JSON response"}