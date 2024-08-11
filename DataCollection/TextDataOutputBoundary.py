"""
Output boundary that just uses text and holds the information in an output receiver.

"""
import pandas as pd

from DataCollection.DataOutputBoundary import DataOutputBoundary
from DataCollection.TextOutputReceiver import TextOutputReceiver


class TextDataOutputBoundary(DataOutputBoundary):
    receiver: TextOutputReceiver

    def __init__(self, receiver):
        self.receiver = receiver

    def send(self, message: pd.DataFrame):
        self.receiver.accept_message(message)