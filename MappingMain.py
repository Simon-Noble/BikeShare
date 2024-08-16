from FileManager.ReadFileInteractor import ReadFileInteractor
from MapMaker.MapGenerationInteractor import MapGenerationInteractor
from MapMaker.MapManager import MapManager


def main():
    map_generator = MapGenerationInteractor(features=[])
    file_reader = ReadFileInteractor('data\ ')
    map_manager = MapManager(file_reader, map_generator)

    map_manager.map_one()




if __name__ == "__main__":
    main()
