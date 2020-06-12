import pandas as pd


def load_playlist(data_path):
    df = None
    try:
        df = pd.read_csv(data_path)
    except IOError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected exception: {e}")

    return df