import json
import requests
import sys


def get_weather(city, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful requests
        data = response.json()
        if data["cod"] == "404":
            print(f"City '{city}' not found.")
            return
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather forecast for {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    except (requests.RequestException, ValueError) as e:
        print(f"Error occurred while fetching weather data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the city name as an argument.")
        sys.exit(1)
    city = sys.argv[1]
    try:
        with open("config.json") as config_file:
            config = json.load(config_file)
        api_key = config["openweathermap_api_key"]
        get_weather(city, api_key)
    except FileNotFoundError:
        print("Config file not found.")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error occurred while reading the config file: {e}")
