import pandas as pd

def get_cebl_schedule(seasons=[]):
    schedule = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/schedule/cebl_schedule.csv")
    schedule = schedule[schedule['season'].isin(seasons)]
    return schedule

def get_cebl_team_boxscore(seasons=[]):
    team_boxscore = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/team-boxscore/cebl_teams.csv")
    team_boxscore = team_boxscore[team_boxscore['season'].isin(seasons)]
    return team_boxscore

def get_cebl_player_boxscore(seasons=[]):
    player_boxscore = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/player-boxscore/cebl_players.csv")
    player_boxscore = player_boxscore[player_boxscore['season'].isin(seasons)]
    return player_boxscore

def get_cebl_officials(seasons=[]):
    officials = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/officials/cebl_officials.csv")
    officials = officials[officials['season'].isin(seasons)]
    return officials

def get_cebl_coaches(seasons=[]):
    coaches = pd.read_csv("https://github.com/ryanndu/cebl-data/releases/download/coaches/cebl_coaches.csv")
    coaches = coaches[coaches['season'].isin(seasons)]
    return coaches

def get_cebl_pbp(seasons=[]):
    pbp = pd.DataFrame()
    for season in seasons:
        pbp = pd.concat([pbp, pd.read_csv(f"https://github.com/ryanndu/cebl-data/releases/download/pbp/cebl_pbp_{season}.csv")])
    return pbp


# Notes:
# - Naming convention, do i include cebl in the function name?
# - Validate seasons, should I just remove invalid or let the user know they put an invalid season?