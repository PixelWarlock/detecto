from argparse import ArgumentParser
from detecto.utils.load_config import load_config
from detecto.runners.supervised_trainer import SupervisedTrainer

def run(mode:str, config:str)->None:
    """Runs training (supervised or reinforced) or inference on a dataset defined in the config"""

    config = load_config(config_path=config)
    if mode == "supervised":
        SupervisedTrainer(config)
    elif mode == "reinforced":
        pass
    elif mode == "inference":
        pass
    else:
        raise ValueError("Incorrect mode - choose one of: supervised | reinfroced | inference")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-m', '--mode', type=str, default='supervised')
    parser.add_argument('-c', '--config', type=str, default='configs/supervised_training_config.yml')
    args = parser.parse_args().__dict__
    
    run(**args)