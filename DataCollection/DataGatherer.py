"""
This class acts as the central data gathering component

The function gather should grab the current information from the bike share api,
and send it to the output boundary

"""
import requests
import pandas as pd

from DataCollection.DataOutputBoundary import DataOutputBoundary


class DataGatherer:
    output_boundary: DataOutputBoundary

    def __init__(self, output_boundary: DataOutputBoundary):
        self.output_boundary = output_boundary

    def gather(self):

        station_information = requests.get('https://tor.publicbikesystem.net/ube/gbfs/v1/en'
                                                        '/station_information').json()

        station_status = requests.get("https://tor.publicbikesystem."
                                                   "net/ube/gbfs/v1/en/station_status").json()
        adjusted_information = dict()

        for station in station_information['data']['stations']:
            adjusted_information[station['station_id']] = {"Information": station}

        failures = []
        for station in station_status['data']['stations']:
            if station['station_id'] in adjusted_information:
                adjusted_information[station['station_id']]["Status"] = station
            else:
                failures.append(station)

        final_information = pd.DataFrame(adjusted_information)

        self.output_boundary.send(final_information)