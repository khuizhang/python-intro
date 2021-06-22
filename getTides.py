#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from lxml import html
from time import sleep
import json
import argparse
from random import randint
import requests
from urllib3.exceptions import InsecureRequestWarning


def get_station_id(station_name):
    """
    check zone information at https://tides.gc.ca/eng/find/zone/10
    Get a list of stations with name and ID from https://tides.gc.ca/eng/station/list
    and then return ID by given station_name
    """
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    for retries in range(1):
        try:
            url = "https://tides.gc.ca/eng/station/list"
            response = requests.get(url, verify=False)

            if response.status_code != 200:
                raise ValueError("Invalid Response Received From Webserver")

            # print("Parsing %s" % (url))
            # Adding random delay
            sleep(randint(1, 3))
            tree = html.fromstring(response.content)
            station_name = station_name.title()
            station_id = ""
            for row in tree.xpath("//table[@id='sitesTable']"):
                try:
                    station_url = row.xpath(".//a[.='" + station_name + "']/@href")
                    station_id = station_url[0].split("=")[1]
                except:
                    print(
                        f"Station {station_name} is not found. Pleaes double check the station name."
                    )
            return station_id

        except Exception as e:
            print("Failed to process the request, Exception:%s" % (e))


def parse_tide_tables(station_ID, date_yyyymmdd):
    """
    Grab tide tables from tides.gc.ca by station

    Args:
            station_ID (str), for example, White Rock is 7577

    Returns:
            dict: Scraped data
    """
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    split_date = [date_yyyymmdd[i : i + 2] for i in range(0, len(date_yyyymmdd), 2)]
    target_year = split_date[0] + split_date[1]
    target_month = split_date[2]
    target_day = split_date[3]

    # Retrying for failed request
    for retries in range(1):
        try:
            url = (
                "https://www.tides.gc.ca/eng/data/table/"
                + target_year
                + "/wlev_sec/%s" % (station_ID)
            )
            response = requests.get(url, verify=False)

            if response.status_code != 200:
                raise ValueError("Invalid Response Received From Webserver")

            # print("Parsing %s" % (url))
            # Adding random delay
            sleep(randint(1, 3))
            tree = html.fromstring(response.content)
            print(
                f"Tide height(m) prediction on {target_year}-{target_month}-{target_day}"
            )
            for sel in tree.xpath("//table[@class='width-100']"):
                month_year = sel.xpath("caption/text()")[0]
                month_name = month_year.split()[0]
                month_number = datetime.datetime.strptime(month_name, "%B").month
                if month_number == int(target_month):
                    for row in sel.xpath(".//tr"):
                        contents = row.xpath(".//td/text()")
                        try:
                            day = contents[0]
                            if int(day) == int(target_day):
                                print(contents[1], contents[2])
                        except IndexError:
                            pass

        except Exception as e:
            print("Failed to process the request, Exception:%s" % (e))


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
