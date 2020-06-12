import contextlib
import os
import pandas as pd


def _write_h5(params):
    for chunk in pd.read_csv(params["data_path_in"], chunksize=params["chunksize"]):
        chunk['PlayerKey'] = chunk['PlayKey'].apply(_extract_playerkey)
        unique_players = chunk['PlayerKey'].unique()
        print(unique_players)

        for player in unique_players:
            keyname = f'player_{player}'
            df = chunk.loc[chunk['PlayerKey'] == player]
            df.to_hdf('./data/02_intermediate/nfl_trackdata.h5', append=True,
                      key=keyname, min_itemsize=100, complevel=params["compression_level"])


def generate_h5(params):
    if params["run_h5"]:
        print("Regenerating HDF output file...")
        exit()
        with contextlib.suppress:
            os.remove(params["data_path_out"])

        _write_h5(params=params)

    else:
        print("Not generating new HDF output file")