# strip_address.py
# ADG Jan 26, 2018
# strips addresses and adds geo info to csv
# source txt comes from:
# https://www.bhamwiki.com/w/List_of_Birmingham_homicides_in_2017

from geopy.geocoders import Nominatim

geolocater = Nominatim()

fn = "2017_raw.txt"
city_state = "birmingham AL"


with open(fn) as f:
    total_sep = 0
    row_count = 0
    for i, row in enumerate(f):
        row_count += 1
        location = row.split("on the")
        if len(location) == 1:
            location = row.split("at the")
        if len(location) == 1:
            location = row.split(" at ")
        if len(location) == 1:
            print(location)
        total_sep += len(location)

    print("PrSeparations : ", (total_sep/row_count) - 1)
    print("Lines in file : ", row_count)
    print("separations : ", total_sep)