#!/bin/python
# -*- coding: utf-8 -*-

import requests

f=open("currentCityID","r")
CITY=f.read().replace('\n','')
f.close()

#CITY = "1070940" # City ID
API_KEY = "d179235a378d7005b408ae177c4e3aa0"
UNITS = "Metric"
UNIT_KEY = "C"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric&lang=fr".format(CITY, API_KEY))
try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
        CURRENT = REQ.json()["weather"][0]["description"].capitalize()
        TEMP = int(float(REQ.json()["main"]["temp"]))
        print("{}, {} °{}".format(CURRENT, TEMP, UNIT_KEY))
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable to print the data")
