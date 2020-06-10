from tougher_on_turf.lib import load_configs, get_playerkeys
from tougher_on_turf.data import load_playlist


def main():
    data_paths = load_configs(conf_key="data")
    print(data_paths)

    playlist_data = load_playlist(data_path=data_paths['play_list'])
    print(playlist_data.head())
    playkeys = playlist_data['PlayKey'].unique()
    print(playkeys)
    exit()
    playerkeys_list = get_playerkeys()
    for playerkey in playerkeys_list:
        print(playerkey)