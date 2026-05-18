import pandas as pd

class Dataframe:
    def __init__(self, imported_dataframe):
        self.imported_dataframe = imported_dataframe

    def read_csv(self):
        df = pd.read_csv(self.imported_dataframe)
        return df