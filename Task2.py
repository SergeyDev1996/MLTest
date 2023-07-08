from datetime import datetime

import requests
api_key = '613bc8ad5d354148c9a786240ae8d661'
city_name = "Kyiv"
city_country = "UA"
# The open weather API accepts only the latitude and longitude, so first we need to get them using the city name and
# country.
city_request = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{city_country}&appid={api_key}'
city_info = requests.get(city_request).json()
base_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={city_info[0]["lat"]}&lon={city_info[0]["lon"]}&appid={api_key}'
# Define the city name
data = requests.get(base_url).json()
for forecast in data['list']:
    timestamp = forecast['dt']
    date = forecast['dt_txt'].split()[0]  # Extract date from dt_txt field
    weather = forecast['weather'][0]['description']  # Extract weather description
    time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Date: {date}, Weather: {weather}, Time: {time}")