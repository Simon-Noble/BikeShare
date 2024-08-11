"""
This class is run to collect and save data for future use

This should run at the given interval and save the data using the output boundary
"""
import time
import datetime

from DataCollection.DataGatherer import DataGatherer
from DataCollection.SaveToFileOutputBoundary import SaveToFileOutputBoundary
from DataCollection.TextOutputReceiver import TextOutputReceiver


class CollectionManager:
    data_gatherer: DataGatherer
    text_receiver: TextOutputReceiver
    output_boundary: SaveToFileOutputBoundary
    interval_seconds: int
    max_duration_seconds: int

    def __init__(self, data_gatherer: DataGatherer, text_receiver: TextOutputReceiver,
                 output_boundary: SaveToFileOutputBoundary, interval_seconds: int, max_duration_seconds: int,
                 ):
        self.data_gatherer = data_gatherer
        self.text_receiver = text_receiver
        self.output_boundary = output_boundary
        self.interval_seconds = interval_seconds
        self.max_duration_seconds = max_duration_seconds

    def run(self):
        start_time = datetime.datetime.now()

        while True:
            time.sleep(self.interval_seconds)
            current_time = datetime.datetime.now()

            self.data_gatherer.gather()

            self.output_boundary.send(self.text_receiver.message)

            if (current_time - start_time) > datetime.timedelta(seconds=self.max_duration_seconds):
                return

