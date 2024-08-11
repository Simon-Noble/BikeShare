from DataCollection.CollectionManager import CollectionManager
from DataCollection.DataGatherer import DataGatherer
from DataCollection.SaveToFileOutputBoundary import SaveToFileOutputBoundary
from DataCollection.TextDataOutputBoundary import TextDataOutputBoundary
from DataCollection.TextOutputReceiver import TextOutputReceiver


def main():
    gatherer_receiver = TextOutputReceiver()
    gatherer_output_boundary = TextDataOutputBoundary(gatherer_receiver)
    data_gatherer = DataGatherer(gatherer_output_boundary)

    manager_output_boundary = SaveToFileOutputBoundary("data\ ")
    collection_manager = CollectionManager(data_gatherer, gatherer_receiver , manager_output_boundary,
                                           5, 100)

    collection_manager.run()




if __name__ == "__main__":
    main()
