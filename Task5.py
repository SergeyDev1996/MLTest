import requests
import json

api_key = '2081eefbe35448eca50533fee9ee55e6'
base_url = 'https://api.sportsdata.io/v3/'
sport = 'Soccer'
league = 'EnglishPremierLeague'
match_id = 'MATCH_ID'  # Replace with the actual match ID

# Make the API request
prediction_url = f"https://api.sportsdata.io/v4/soccer/odds/json/BettingEventsBySeason/EPL/2020?key=2081eefbe35448eca50533fee9ee55e6"
response = requests.get(prediction_url)
prediction_data = response.json()
print(prediction_data)
# home_team = prediction_data['HomeTeam']
# away_team = prediction_data['AwayTeam']
# predicted_outcome = prediction_data['Prediction']
# confidence_level = prediction_data['Confidence']
# print(f'Next match prediction:')
# print(f'Home Team: {home_team}')
# print(f'Away Team: {away_team}')
# print(f'Predicted Outcome: {predicted_outcome}')
# print(f'Confidence Level: {confidence_level}')