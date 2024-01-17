import pandas as pd
from detecto.models.encoders_factory import EncoderFactory

class SupervisedTrainer:

    def __init__(self, config):
        
        if config.train_dataset is None:
            raise ValueError("If you want to run training then provide training data!")
        else:
            self.train_dataframe = pd.read_csv(config.train_dataset)
        
        if config.valid_dataset is None:
            print("You have not provided any validation data")
            self.validate = False
        else:
            self.valid_data = pd.read_csv(config.valid_dataset)
            self.validate = True

    def _train_step(self):
        pass

    def _valid_step(self):
        pass

    def run(self):
        pass