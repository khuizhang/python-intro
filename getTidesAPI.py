#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import requests
import json


def get_station_id(station_name):

    response = requests.get("https://api-iwls.dfo-mpo.gc.ca/api/v1/stations")
    stationsList = response.json()
    station_name = station_name.title()
    print(station_name)
    for station in stationsList:
        if station["officialName"] == station_name:
            station_id = station["id"]
    return station_id


def parse_tide_tables(station_ID, date_yyyymmdd):
    response = requests.get(
        "https://api-iwls.dfo-mpo.gc.ca/api/v1/stations/5cebf1de3d0f4a073c4bb933/data?time-series-code=wlp&from=2020-10-01T00:00:00Z&to=2020-10-02T00:00:00Z"
    )
    print(type(response.json()))


if __name__ == "__main__":

    argparser = argparse.ArgumentParser()
    argparser.add_argument("station", help="tide station")
    argparser.add_argument("date_yyyymmdd", help="date in format of yyyymmdd")
    args = argparser.parse_args()
    station = args.station
    date_yyyymmdd = args.date_yyyymmdd
    station_ID = get_station_id(station)
    print("Fetching data for %s" % (station))
    parse_tide_tables(station_ID, date_yyyymmdd)
