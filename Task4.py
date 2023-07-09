import requests
import sys

api_key = "613bc8ad5d354148c9a786240ae8d661"


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(len(sys.argv))
        print("Please provide the city name as an argument.")
        sys.exit(1)
    city = sys.argv[1]

    get_weather(city)
