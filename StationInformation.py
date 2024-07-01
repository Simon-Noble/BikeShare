from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class StationInformation:
    station_id: str
    name: str
    physical_configuration: str
    lat: float
    lon: float
    altitude: any
    address: str
    post_code: str
    capacity: int
    is_charging_station: bool
    rental_methods: list
    groups: list
    obcn: str
    short_name: str
    nearby_distance: float
    _ride_code_support: bool
    rental_uris: dict
