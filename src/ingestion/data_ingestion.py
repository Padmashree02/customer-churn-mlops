import pandas as pd
from src.utils.common import read_yaml

class DataIngestion:
    def __init__(self):
        self.config=read_yaml('configs/config.yaml')

    def load_data(self):
        path=self.config['data_path']
        df=pd.read_csv(path)
        return df