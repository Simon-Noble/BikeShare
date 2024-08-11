"""
Output boundary for the DataGatherer




"""
import pandas as pd

class DataOutputBoundary:
    def send(self, message: pd.DataFrame):
        raise NotImplementedError
