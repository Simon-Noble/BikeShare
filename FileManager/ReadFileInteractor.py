"""
This class manages the reading of information for later data analysis or other uses


"""


class ReadFileInteractor:
    directory :str
    def __init__(self, directory: str):
        self.directory = directory

    def read(self):