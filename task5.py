import requests
import json

api_key = '2081eefbe35448eca50533fee9ee55e6'
base_url = 'https://api.sportsdata.io/v3/'
sport = 'Soccer'
league = 'EnglishPremierLeague'
match_id = 'MATCH_ID'  # Replace with the actual match ID

# Make the API request
prediction_url = f'{base_url}{sport}/{league}/MatchPredictions/{match_id}?key={api_key}'
response = requests.get(prediction_url)
prediction_data = response.json()