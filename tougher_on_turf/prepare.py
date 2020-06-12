from tougher_on_turf.lib import Player
from tougher_on_turf.lib.utils import load_configs, load_playlist
from tougher_on_turf.lib.prepare_data import get_playerkeys, get_playkeys, get_player_df


def preprocess_playlist():
    data_paths = load_configs(conf_key="data")
    print(data_paths)

    playlist_data = load_playlist(data_path=data_paths['play_list'])  # master playlist
    print(playlist_data.head())

    player_keys = get_playerkeys(df=playlist_data)
    player_list = [Player(playerkey=player_key,
                          player_df=get_player_df(df=playlist_data, player_key=player_key))
                   for player_key in player_keys]

    for player in player_list:
        print(player.playerkey)
        print(player.roster_position)
        # player.isinjured()
        exit()
