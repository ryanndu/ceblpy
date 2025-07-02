import pandas as pd
from . import helpers as h

def load_cebl_schedule(seasons=[]):
    h.validate_seasons(seasons)
    schedule = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/schedule/cebl_schedule.csv")
    schedule = schedule[schedule['season'].isin(seasons)]
    return schedule

def load_cebl_team_boxscore(seasons=[]):
    h.validate_seasons(seasons)
    team_boxscore = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/team-boxscore/cebl_teams.csv")
    team_boxscore = team_boxscore[team_boxscore['season'].isin(seasons)]
    return team_boxscore

def load_cebl_player_boxscore(seasons=[]):
    h.validate_seasons(seasons)
    player_boxscore = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/player-boxscore/cebl_players.csv")
    player_boxscore = player_boxscore[player_boxscore['season'].isin(seasons)]
    return player_boxscore

def load_cebl_officials(seasons=[]):
    h.validate_seasons(seasons)
    officials = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/officials/cebl_officials.csv")
    officials = officials[officials['season'].isin(seasons)]
    return officials

def load_cebl_coaches(seasons=[]):
    h.validate_seasons(seasons)
    coaches = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/coaches/cebl_coaches.csv")
    coaches = coaches[coaches['season'].isin(seasons)]
    return coaches

def load_cebl_pbp(seasons=[]):
    h.validate_seasons(seasons)
    pbp = pd.DataFrame()
    for season in seasons:
        pbp = pd.concat([pbp, pd.read_csv(f"https://github.com/ryanndu/cebl-data/releases/download/pbp/cebl_pbp_{season}.csv")])
    return pbp


# Notes:
# - Naming convention, do i include cebl in the function name?
# - Validate seasons, should I just remove invalid or let the user know they put an invalid season?
# - Haven't done testing yet, but I will figure out a way to test these functions.
