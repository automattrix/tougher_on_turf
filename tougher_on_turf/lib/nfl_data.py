import pandas as pd


class Player:
    def __init__(self, playerkey: str, player_df: pd.DataFrame):
        self.playerkey = playerkey
        self.player_df = player_df
        self.roster_position = self.get_roster_position()

    def get_playkeys(self):
        play_keys = self.player_df['PlayKey'].unique()
        return play_keys

    def get_roster_position(self):
        # In case the player has had multiple positions, we will identify them as the most number of plays recorded
        # in at that position
        roster_positions = self.player_df.groupby(['Position']).count().reset_index()
        roster_positions.sort_values(by='PlayKey', ascending=False, inplace=True)  # sort descending
        roster_position = roster_positions['Position'].iloc[0].lower()  # first index is highest num of plays at pos.
        return roster_position


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
