from tougher_on_turf.lib.utils import data_loader
import pandas as pd
from typing import Any, List


def get_playerkeys(df: pd.DataFrame) -> List:
    player_keys = df['PlayerKey'].unique()
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


def get_isinjured():
    tmp = ''