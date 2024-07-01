import datetime

import StationConstructor


def main():
    import requests

    station_information = requests.get('https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_information').json()

    station_status = requests.get("https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_status").json()

    print(station_information)
    print(station_status)
    # 1716245522
    # 1716246862
    adjusted_information = dict()

    for station in station_information['data']['stations']:
        adjusted_information[station['station_id']] = {"Information":  station}

    print(adjusted_information)
    failures = []

    for station in station_status['data']['stations']:
        if station['station_id'] in adjusted_information:
            adjusted_information[station['station_id']]["Status"] = station
        else:
            failures.append(station)

    stations = {}
    for key in adjusted_information.keys():
        stations[key] = StationConstructor.construct(adjusted_information[key]['Information'],
                                                     adjusted_information[key]['Status'])

    print(stations)
    time_raw = stations['7000'].timestamp_raw
    time_datetime = datetime.datetime(1970, 1, 1, 0)
    today = time_datetime + datetime.timedelta(seconds=time_raw)
    print(today)
    print(datetime.datetime.now(tz=datetime.UTC))


if __name__ == "__main__":
    main()
