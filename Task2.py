import json
from datetime import datetime

import requests


def get_city_info(api_key, city_name, city_country):
    city_request = f'http://api.openweathermap.org/geo/1.0/direct?q=' \
                   f'{city_name},' \
                   f'{city_country}&appid={api_key}'
    try:
        city_info = requests.get(city_request).json()
        return city_info[0] if city_info else None
    except requests.RequestException as e:
        print(f"Error occurred while fetching city information: {e}")
        return None


def get_weather_forecast(api_key, city_info):
    if not city_info:
        return None
    base_url = f'https://api.openweathermap.org/data/2.5/forecast?lat=' \
               f'{city_info["lat"]}&lon=' \
               f'{city_info["lon"]}&appid={api_key}'
    try:
        data = requests.get(base_url).json()
        return data['list'] if data else None
    except requests.RequestException as e:
        print(f"Error occurred while fetching weather forecast: {e}")
        return None


def print_forecast(forecast):
    if not forecast:
        print("No forecast data available.")
        return
    for entry in forecast:
        timestamp = entry['dt']
        date = entry['dt_txt'].split()[0]
        weather = entry['weather'][0]['description']
        time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Date: {date}, Weather: {weather}, Time: {time}")


if __name__ == "__main__":
    # OpenWeatherMap doesn't now allow a free 10-day forecast,
    # I would need to buy a 30$ subscription.
    # Only 3 day forecasts are free, and I will use it here.
    with open("config.json") as config_file:
        config = json.load(config_file)
    api_key = config["openweathermap_api_key"]
    city_name = "Kyiv"
    city_country = "UA"
    city_info = get_city_info(api_key, city_name, city_country)
    forecast = get_weather_forecast(api_key, city_info)
    print_forecast(forecast)
