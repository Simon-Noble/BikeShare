from StationInformation import StationInformation
from StationStatus import StationStatus
from datetime import datetime
from BikeStation import BikeStation


class DifferentStationsError(Exception):
    def __str__(self):
        return "The information and status have different station Ids"


def construct(information: dict, status: dict) -> BikeStation:
    if information['station_id'] != status['station_id']:
        raise DifferentStationsError

    station_info = _construct_information(information)
    station_status = _construct_status(status)

    station = BikeStation(station_id=station_info.station_id,
                          timestamp_raw=station_status.last_reported,
                          time_datetime=None,
                          information=station_info,
                          status=station_status
                          )
    return station


def _construct_information(information: dict) -> StationInformation:
    if 'post_code' in information.keys():
        post_code = information['post_code']
    else:
        post_code = None

    if 'address' in information.keys():
        address = information['address']
    else:
        address = None

    station_information = StationInformation(
        station_id=information['station_id'], name=information['name'],
        physical_configuration=information['physical_configuration'],
        lat=information['lat'], lon=information['lon'], altitude=information['altitude'],
        address=address, post_code=post_code,
        capacity=information['capacity'],
        is_charging_station=information['is_charging_station'],
        rental_methods=information['rental_methods'], groups=information['groups'],
        obcn=information['obcn'], short_name=information['short_name'],
        nearby_distance=information['nearby_distance'],
        _ride_code_support=information['_ride_code_support'],
        rental_uris=information['rental_uris']
    )
    return station_information


def _construct_status(status: dict) -> StationStatus:
    station_status = StationStatus(
        station_id=status['station_id'], num_bikes_available=status['num_bikes_available'],
        num_bikes_available_types=status['num_bikes_available_types'],
        num_bikes_disabled=status['num_bikes_disabled'],
        num_docks_available=status['num_docks_available'],
        num_docks_disabled=status['num_docks_disabled'],
        last_reported=status['last_reported'],
        is_charging_station=status['is_charging_station'],
        status=status['status'], is_installed=status['is_installed'],
        is_renting=status['is_renting'], is_returning=status['is_returning'],
        traffic=status['traffic']
    )
    return station_status
