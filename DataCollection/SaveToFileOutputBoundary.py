"""
Implementation of the DataOutputBoundary

Saves to a file

"""
import json
import pandas as pd
from DataCollection.DataOutputBoundary import DataOutputBoundary


class SaveToFileOutputBoundary(DataOutputBoundary):
    file_name: str

    def __init__(self, file_name:str):
        self.file_name = file_name

    def send(self, message: pd.DataFrame):
        with open(self.file_name) as f:
            json.dump(message, f)
