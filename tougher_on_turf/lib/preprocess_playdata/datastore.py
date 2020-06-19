from tougher_on_turf.lib.utils import load_configs
from tougher_on_turf.lib.prepare_data import data_wrangler
import contextlib
import os
import pandas as pd


def write_h5():
    data_paths = load_configs(conf_key='data')
    preprocess_conf = load_configs(conf_key='preprocess_playdata')

    for chunk in pd.read_csv(data_paths['play_track_data'], chunksize=preprocess_conf['chunksize']):
        chunk['PlayerKey'] = chunk['PlayKey'].apply(data_wrangler.extract_playerkey)
        unique_players = chunk['PlayerKey'].unique()
        print(f"Writing data for: {unique_players}")

        for player in unique_players:
            keyname = f'player_{player}'
            df = chunk.loc[chunk['PlayerKey'] == player]

            df.to_hdf(f"{data_paths['intermediate']}/{preprocess_conf['filename']}", append=True,
                      key=keyname, min_itemsize=100, complevel=preprocess_conf['compression_level'])
