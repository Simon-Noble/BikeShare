"""
Takes a compatable input string and graphs the desired values

Features argument allows for customization of output
"""
import pandas as pd
import plotly.express as px

from MapMaker.MapGenerationInputBoundary import MapGenerationInputBoundary


class MapGenerationInteractor(MapGenerationInputBoundary):
    features: list

    def __init__(self, features):
        self.features = features

    def generate(self, data: pd.DataFrame):
        """
        First collect the desired features from the data, then graph them
        """

        featurefied_data = []

        for station in data:
            new_entry = {}
            for feature in self.features + ['lat', 'lon']:
                new_entry[feature] = data[station]['Information'][feature]
            featurefied_data.append(new_entry)

        fig = px.scatter_mapbox(featurefied_data, lat='lat',lon='lon',  title='Toronto Bike Share Locations',
                                mapbox_style="open-street-map", )
        for feature in self.features:
            fig.update_layout(feature=feature)
        fig.write_html('maptest.html')
        fig.show()
