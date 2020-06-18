from tougher_on_turf import prepare
from tougher_on_turf.lib.utils import load_context
from pathlib import Path


def main():
    load_context(Path.cwd())
    prepare.preprocess_playlist()
    prepare.preprocess_playdata()


if __name__ =='__main__':
    main()

