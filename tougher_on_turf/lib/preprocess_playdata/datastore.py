from tougher_on_turf.lib.utils import load_configs
from tougher_on_turf.lib.prepare_data import data_wrangler
import contextlib
import os
import pandas as pd


def write_h5():
    data_paths = load_configs(conf_key='data')
    preprocess_conf = load_configs(conf_key='preprocess_playdata')

    for chunk in pd.read_csv(data_paths['play_track_data'], chunksize=preprocess_conf['chunksize']):
        chunk['GameKeyClean'] = chunk['PlayKey'].apply(data_wrangler.clean_gamekey)
        unique_player_games = chunk['GameKeyClean'].unique()
        print(f"Writing data for: {unique_player_games}")

        for game in unique_player_games:
            keyname = f'game_{game}'
            df = chunk.loc[chunk['GameKeyClean'] == game]

            df.to_hdf(f"{data_paths['intermediate']}/{preprocess_conf['filename']}", append=True,
                      key=keyname, min_itemsize=100, complevel=preprocess_conf['compression_level'])
            df = None
