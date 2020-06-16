import pandas as pd
import _pickle
import os


def load_csv(data_path):
    df = None
    try:
        df = pd.read_csv(data_path)
    except IOError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected exception: {e}")

    return df


def save_pickle(output_path, data, overwrite_keys: bool):
    with open(output_path, 'wb') as output:
        _pickle.dump(data, output, -1)


def load_pickle(input_path):
    with open(input_path, "rb") as f:
        while True:
            try:
                yield _pickle.load(f)
            except EOFError:
                break
