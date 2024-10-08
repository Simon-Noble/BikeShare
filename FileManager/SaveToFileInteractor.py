"""
Implementation of the DataOutputBoundary

Saves to a file

Is given a directory and generates file names for said directory

"""
import datetime
import json
from zoneinfo import ZoneInfo

import pandas as pd

from FileManager.DataOutputBoundary import DataOutputBoundary


class SaveToFileInteractor(DataOutputBoundary):
    directory: str

    def __init__(self, directory: str):
        self.directory = directory

    def send(self, message: pd.DataFrame):

        time = datetime.datetime.now(tz=ZoneInfo('EST'))
        file_name = f'{time.year}-{time.month}-{time.day}-{time.hour}-{time.minute}-{time.second}'

        with open(self.directory+"directory", 'a') as f:
            f.writelines(file_name+"\n")


        total_path = self.directory + file_name

        with open(total_path, mode='w') as f:
            f.write(message.to_json())


