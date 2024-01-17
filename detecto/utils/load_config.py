import yaml
from dotmap import DotMap

def load_config(config_path:str)->DotMap:
    with open(config_path) as file:
        content = yaml.load(file, Loader=yaml.FullLoader)
    return DotMap(content)