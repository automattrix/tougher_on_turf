from tougher_on_turf import prepare
from tougher_on_turf.utils import load_context
from pathlib import Path


def main():
    load_context(Path.cwd())
    prepare.main()


if __name__ =='__main__':
    main()

