import pandas as pd
from typing import List, AnyStr


class Player:
    def __init__(self, playerkey: AnyStr, player_df: pd.DataFrame):
        self.playerkey = str(playerkey)
        self.player_df = player_df
        self.roster_position = self.get_roster_position()
        self.is_injured = False

    def get_playkeys(self) -> List:
        play_keys = self.player_df['PlayKey'].unique()
        return play_keys

    def get_roster_position(self) -> AnyStr:
        # In case the player has had multiple positions, we will identify them as the most number of plays recorded
        # in at that position
        roster_positions = self.player_df.groupby(['Position']).count().reset_index()
        roster_positions.sort_values(by='PlayKey', ascending=False, inplace=True)  # sort descending
        roster_position = roster_positions['Position'].iloc[0].lower()  # first index is highest num of plays at pos.
        return roster_position

    def check_is_injured(self, injury_keys: List) -> bool:
        if str(self.playerkey) in injury_keys:
            self.is_injured = True
        else:
            self.is_injured = False

    def join_injury_data(self, player_injury_df):
        player_injury_df = player_injury_df.copy()
        df = self.player_df.copy()
        player_injury_df.set_index("PlayKey", inplace=True)
        df.set_index("PlayKey", inplace=True)

        # Re-assign self
        df = df.join(player_injury_df, rsuffix="_test")
        self.player_df = df


class Play(Player):
    def __init__(self,
                 playerkey,
                 roster_position):
        super().__init__(playerkey, roster_position)


class Stadium:
    def __init__(self, stadiumtype, fieldtype, weather, temperature):
        self.stadiumtype = stadiumtype
        self.fieldtype = fieldtype
        self.weather = weather
        self.temperature = temperature
