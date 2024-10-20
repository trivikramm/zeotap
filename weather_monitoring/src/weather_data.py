import requests
import time
from .config import API_KEY, METROS

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather_data():
    weather_data = []
    for city in METROS:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
        data = response.json()
        weather_data.append({
            'city': city,
            'main': data['weather'][0]['main'],
            'temp': kelvin_to_celsius(data['main']['temp']),
            'feels_like': kelvin_to_celsius(data['main']['feels_like']),
            'dt': data['dt']
        })
    return weather_data

def fetch_weather_data_periodically(interval):
    while True:
        weather_data = get_weather_data()
        # Process the weather data (e.g., store in database, calculate rollups)
        time.sleep(interval)
