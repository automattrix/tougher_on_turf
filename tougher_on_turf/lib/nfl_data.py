import pandas as pd


class Player:
    def __init__(self, playerkey, roster_position):
        self.playerkey = playerkey
        self.roster_position = roster_position


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