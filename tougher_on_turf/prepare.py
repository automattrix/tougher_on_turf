from tougher_on_turf.lib import Player
from tougher_on_turf.lib.utils import load_configs, load_csv
from tougher_on_turf.lib.prepare_data import get_playerkeys, get_playkeys, get_player_df, get_player_injury_df
import pandas as pd


def preprocess_playlist():
    data_paths = load_configs(conf_key="data")
    print(data_paths)

    playlist_data = load_csv(data_path=data_paths['play_list'])  # master playlist
    injury_data = load_csv(data_path=data_paths['injury_record'])

    print(playlist_data.head())
    print(injury_data.head())

    # Get list of all playerkeys
    player_keys = get_playerkeys(df=playlist_data)
    # Instantiate Player class for each player key
    #     - calls get_player_df() to load player related data from playlist_data
    player_list = [Player(playerkey=player_key,
                          player_df=get_player_df(df=playlist_data, player_key=player_key))
                   for player_key in player_keys]

    # Get list of all injury keys
    player_injury_keys = get_playerkeys(df=injury_data)


    for player in player_list:
        # print(player.playerkey)
        # print(player.roster_position)
        # print(player.player_df.head())
        player.check_is_injured(injury_keys=player_injury_keys)
        player_injury_df = get_player_injury_df(
            playerkey=player.playerkey,
            isinjured=player.is_injured,
            injury_data=injury_data)
        if player.is_injured is True:
            player.join_injury_data(player_injury_df=player_injury_df)
            exit()
        else:
            pass

        #print(player.player_df)



