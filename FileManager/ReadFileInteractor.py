"""
This class manages the reading of information for later data analysis or other uses


"""
import pandas as pd


class ReadFileInteractor:
    directory :str
    index: int

    def __init__(self, directory: str):
        self.directory = directory
        self.index = 0

    def read_next(self):
        """
        read the next file in the directory and return it
        """

        with open(self.directory+'directory', 'r') as f:
            file_name = f.readline()
            for _ in range(self.index):
                file_name = f.readline()

        with open(self.directory+file_name, 'r') as f:
            values = pd.read_json(f)

        return values
