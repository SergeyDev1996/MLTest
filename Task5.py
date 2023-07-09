import json
from random import randrange
import requests


def fetch_game_odds(competition, date, api_key):
    sportsdata_api_key = api_key
    url = f"https://api.sportsdata.io/v4/soccer/odds/json/GameOddsByDate/{competition}/{date}?key={sportsdata_api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful requests
        pre_game_odds = response.json()
        return pre_game_odds
    except (requests.RequestException, ValueError) as e:
        print(f"Error occurred while fetching pre-game odds: {e}")
        return None


def determine_prediction(pre_game_odds):
    if not pre_game_odds:
        print("No games for the chosen date and competition, sorry.")
        return

    total_games = len(pre_game_odds)
    response_game_number = randrange(0, total_games)

    game_odds = pre_game_odds[response_game_number]
    home_team_name = game_odds['HomeTeamName']
    away_team_name = game_odds['AwayTeamName']

    outcomes = {'home_wins': 0, 'away_wins': 0, 'draws': 0}

    for odds in game_odds['PregameOdds']:
        home_money_line = odds['HomeMoneyLine']
        away_money_line = odds['AwayMoneyLine']

        if home_money_line < away_money_line:
            outcomes['home_wins'] += 1
        elif home_money_line > away_money_line:
            outcomes['away_wins'] += 1
        else:
            outcomes['draws'] += 1

    home_wins = outcomes['home_wins']
    away_wins = outcomes['away_wins']
    draws = outcomes['draws']

    predictions = []

    if home_wins > away_wins and home_wins > draws:
        predictions.append(f"In the next match between {home_team_name} and {away_team_name}, the majority of sportsbooks predict a win for the {home_team_name}.")
    elif away_wins > home_wins and away_wins > draws:
        predictions.append(f"In the match between {home_team_name} and {away_team_name}, the majority of sportsbooks predict a win for the {away_team_name}.")
    else:
        predictions.append(f"The majority of sportsbooks predict a draw in the next match between {home_team_name} and {away_team_name}.")

    return predictions


def print_predictions(predictions):
    print("\n".join(predictions))


if __name__ == "__main__":
    # Load configuration from JSON file
    with open("config.json") as config_file:
        config = json.load(config_file)

    date = config["date"]
    competition = config["competition"]
    api_key = config["sportsdata_api_key"]
    pre_game_odds = fetch_game_odds(competition, date, api_key)
    prediction_messages = determine_prediction(pre_game_odds)
    print_predictions(prediction_messages)
