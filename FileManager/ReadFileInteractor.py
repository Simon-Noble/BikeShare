"""
This class manages the reading of information for later data analysis or other uses


"""
import json

import pandas as pd


class ReadFileInteractor:
    directory: str
    index: int
    max_index: int

    def __init__(self, directory: str):
        """

        :param directory:
        """
        self.directory = directory
        self.index = 0

        with open(self.directory+'directory', 'r') as f:
            data = f.readlines()
        self.max_index = len(data) - 1

    def has_next(self) -> bool:
        if self.max_index >= self.index:
            return False
        return True

    def read_next(self):
        """
        read the next file in the directory and return it
        """

        with open(self.directory+'directory', 'r') as f:
            file = f.readlines()
            file_name = file[self.index]
            self.index += 1

        with open(self.directory + file_name[:-1], 'r') as f:
            values = json.load(f)

        return values
