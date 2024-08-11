"""
Receives data from a TextDataOutputBoundary.

TODO: consider making this an input boundary
"""
import pandas as pd


class TextOutputReceiver:
    message: pd.DataFrame | None

    def __init__(self):
        self.message = None

    def accept_message(self, message: pd.DataFrame):
        self.message = message
