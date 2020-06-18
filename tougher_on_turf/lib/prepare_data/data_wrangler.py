import pandas as pd
from typing import Any, List


def get_playerkeys(df: pd.DataFrame) -> List:
    player_keys = df['PlayerKey'].unique().tolist()
    return player_keys


def get_player_df(df: pd.DataFrame, player_key: str):
    player_df = None
    try:
        player_df = df.loc[df['PlayerKey'] == player_key]
    except Exception as e:
        print(e)
    return player_df


def get_playkeys(df: pd.DataFrame) -> pd.DataFrame:
    player_keys = get_playerkeys(df=df)
    for player_key in player_keys:
        player_df = df.loc[df['PlayerKey'] == player_key]
        play_keys = player_df['PlayKey'].unique()
        yield play_keys


def get_player_injury_df(playerkey, isinjured, injury_data):
    # ['PlayerKey', 'GameID', 'PlayKey', 'BodyPart', 'Surface', 'DM_M1', 'DM_M7', 'DM_M28', 'DM_M42']
    include_keys = ['PlayerKey', 'GameID', 'PlayKey', 'BodyPart', 'Surface', 'DM_M1', 'DM_M7', 'DM_M28', 'DM_M42']
    if isinjured is True:
        player_injury_df = injury_data.loc[injury_data['PlayerKey'] == playerkey]
    else:
        player_injury_df = pd.DataFrame()
        player_injury_df[include_keys] = pd.DataFrame([[None for x in include_keys]])

    return player_injury_df
