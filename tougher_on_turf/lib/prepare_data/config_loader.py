import yaml
import os

conf_path = "./tougher_on_turf/conf/conf.yml"


def load_configs(conf_key):
    print(os.getcwd())
    with open(conf_path, 'r') as f:
        confs = yaml.load(f, Loader=yaml.FullLoader)[conf_key]
        return confs
