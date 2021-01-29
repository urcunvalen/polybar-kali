#!/bin/bash

curl ipinfo.io > ipinfos

PAYS=$(grep -E 'country' ipinfos | grep -Eo '[A-Z]{1,3}')

VILLE=$(grep -E 'city' ipinfos | grep -Eo '[A-Z][a-z]{1,50}')

grep -E "$PAYS.*$VILLE" cities_id.csv | grep -Eo '[0-9]{1,9}' > currentCityID

rm ipinfos
