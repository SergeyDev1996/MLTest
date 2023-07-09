import requests
import json
date = '2023-07-09'
competition = 'MLS'
# response = requests.get(f'https://api.sportsdata.io/v4/soccer/scores/json/GamesByDate/{competition}/{date}?key=2081eefbe35448eca50533fee9ee55e6').json()
# game_ids = []
# for game in response:
#     game_ids.append(game["GameId"])
# beting_markets = requests.get(f"https://api.sportsdata.io/v4/soccer/odds/json/BettingMarketsByGameID/{competition}/{game_ids[0]}?key=2081eefbe35448eca50533fee9ee55e6")
# print(beting_markets.json()[2])

pre_game_odds = requests.get(f"https://api.sportsdata.io/v4/soccer/odds/json/GameOddsByDate/{competition}/{date}?key=2081eefbe35448eca50533fee9ee55e6").json()
response_game_number = 0
# Team Score Prediction

home_team_name = pre_game_odds[response_game_number]['HomeTeamName']
away_team_name = pre_game_odds[response_game_number]['AwayTeamName']
home_team_score = pre_game_odds[response_game_number]['HomeTeamScore']
away_team_score = pre_game_odds[response_game_number]['AwayTeamScore']
#
# Predict the outcome
if home_team_score > away_team_score:
    prediction = f"The next match between {home_team_name} and {away_team_name} is likely to result in a win for the {home_team_name}."
elif home_team_score < away_team_score:
    prediction = f"The next match between {home_team_name} and {away_team_name} is likely to result in a win for the {away_team_name}."
else:
    prediction = f"The next match between {home_team_name} and {away_team_name} is likely to result in a draw."
print(prediction)


home_wins = 0
away_wins = 0
draws = 0

# Iterate through the pregame odds from different sportsbooks
for odds in pre_game_odds[0]['PregameOdds']:
    home_money_line = odds['HomeMoneyLine']
    away_money_line = odds['AwayMoneyLine']

    # Compare the moneyline odds
    if home_money_line < away_money_line:
        home_wins += 1
    elif home_money_line > away_money_line:
        away_wins += 1
    else:
        draws += 1

# Determine the prediction based on the majority opinion
if home_wins > away_wins and home_wins > draws:
    prediction = f"The majority of sportsbooks predict a win for the {home_team_name}."
elif away_wins > home_wins and away_wins > draws:
    prediction = f"The majority of sportsbooks predict a win for the {away_team_name}."
else:
    prediction = f"The majority of sportsbooks predict a draw in the next match between {home_team_name} and {away_team_name}."

# Print the prediction
print(prediction)