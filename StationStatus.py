from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class StationStatus:
    station_id: str
    num_bikes_available: int
    num_bikes_available_types: dict[str:int]
    num_bikes_disabled: int
    num_docks_available: int
    num_docks_disabled: int
    last_reported: int
    is_charging_station: bool
    status: str
    is_installed: int
    is_renting: int
    is_returning: int
    traffic: any
