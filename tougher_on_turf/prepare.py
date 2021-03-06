from tougher_on_turf.lib import Player
from tougher_on_turf.lib.utils import load_configs, load_csv, save_pickle, load_pickle
from tougher_on_turf.lib.prepare_data import get_playerkeys, get_playkeys, get_player_df, get_player_injury_df
from tougher_on_turf.lib.preprocess_playdata import datastore

import os
import contextlib


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

        player.join_injury_data(player_injury_df=player_injury_df)
        # Save player to pickle
        preprocess_data = load_configs(conf_key='preprocess')
        overwrite = preprocess_data['overwrite']
        overwrite_keys = preprocess_data['playerkey_list']
        current_key = str(player.playerkey)

        pickle_out_base = data_paths['intermediate']
        player_pickle_path = f"{pickle_out_base}/{player.playerkey}.pkl"

        # Create if player pickle doesn't exist
        if os.path.exists(player_pickle_path):
            if overwrite is True and len(overwrite_keys) > 0:
                # Overwrite specific player
                if current_key in overwrite_keys:
                    print(f"Overwriting specific player: {player.playerkey}")
                    save_pickle(output_path=player_pickle_path, data=player, overwrite_keys=overwrite_keys)
                else:
                    pass

            # Overwrite all players
            elif overwrite is True and len(overwrite_keys) == 0:
                print(f"Overwriting player: {player.playerkey}")
                save_pickle(output_path=player_pickle_path, data=player, overwrite_keys=overwrite_keys)
            else:
                pass
        else:
            print(f"Saving new player: {player.playerkey}")
            save_pickle(output_path=player_pickle_path, data=player, overwrite_keys=overwrite_keys)

        del player


def preprocess_playdata():
    data_paths = load_configs(conf_key='data')
    preprocess_conf = load_configs(conf_key='preprocess_playdata')
    hdf_output_path = f"{data_paths['intermediate']}/{preprocess_conf['filename']}"
    if os.path.exists(hdf_output_path):
        if preprocess_conf['regenerate']:
            print("Regenerating HDF output file...")

            try:
                os.remove(hdf_output_path)
            except OSError as e:
                print(e)
            except Exception as e:
                print(f"Unexpected exception: {e}")

            datastore.write_h5()
        else:
            print("Not generating new HDF output file")
    else:
        datastore.write_h5()



