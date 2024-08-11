"""
Output boundary that just uses text and holds the information in an output receiver.

"""
import pandas as pd

from DataCollection.DataOutputBoundary import DataOutputBoundary


class TextDataOutputBoundary(DataOutputBoundary):
    def __init__(self, receiver):
    def send(self, message: pd.DataFrame):