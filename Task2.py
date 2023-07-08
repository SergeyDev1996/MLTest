import requests
api_key = '613bc8ad5d354148c9a786240ae8d661'
base_url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=7707d8517dca7a2ca3ae1a6836dc966d'
london_url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=7707d8517dca7a2ca3ae1a6836dc966d'
# Define the city name
city_name = 'Kyiv'

# Make the API request
# current_weather_url = f'{base_url}weather?q={city_name}&appid={api_key}'
response = requests.get(london_url)
current_weather_data = response.json()
print(current_weather_data)
# Extract relevant information
# temperature = current_weather_data['main']['temp']
# humidity = current_weather_data['main']['humidity']
# weather_description = current_weather_data['weather'][0]['description']
# # Print the current weather
# print(f'Current weather in {city_name}:')
# print(f'Temperature: {temperature} K')
# print(f'Humidity: {humidity}%')
# print(f'Weather description: {weather_description}')
# # Define the number of days for the forecast
# num_days = 10
#
# # Make the API request
# forecast_url = f'{base_url}forecast?q={city_name}&cnt={num_days}&appid={api_key}'
# response = requests.get(forecast_url)
# forecast_data = response.json()
# # Extract forecast information for each day
# forecast = []
# for item in forecast_data['list']:
#     date = item['dt_txt'].split()[0]  # Extract only the date part
#     temperature = item['main']['temp']
#     humidity = item['main']['humidity']
#     weather_description = item['weather'][0]['description']
#     forecast.append({'date': date, 'temperature': temperature, 'humidity': humidity, 'weather_description': weather_description})
#
# # Print the forecast
# print('\nForecast for the next 10 days:')
# for day in forecast:
#     print('---------------------')
#     print(f"Date: {day['date']}")
#     print(f"Temperature: {day['temperature']} K")
#     print(f"Humidity: {day['humidity']}%")
#     print(f"Weather description: {day['weather_description']}")