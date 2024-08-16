"""
This class gets data from the FileManager and sends it to the MapGenerationInteractor as required
"""
from FileManager.ReadFileInteractor import ReadFileInteractor
from MapMaker.MapGenerationInputBoundary import MapGenerationInputBoundary


class MapManager:
    file_reader: ReadFileInteractor
    map_generator: MapGenerationInputBoundary

    def __init__(self, file_reader: ReadFileInteractor, map_generation: MapGenerationInputBoundary):
        self.file_reader = file_reader
        self.map_generator = map_generation

    def map_one(self):
        data = self.file_reader.read_next()
        self.map_generator.generate(data)

    def map_all(self):
        while self.file_reader.has_next():
            self.map_one()
