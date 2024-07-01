from dataclasses import dataclass
from StationInformation import StationInformation
from StationStatus import StationStatus
from datetime import datetime


@dataclass(frozen=True, kw_only=True)
class BikeStation:
    station_id: str
    timestamp_raw: int
    time_datetime: datetime
    information: StationInformation
    status: StationStatus
