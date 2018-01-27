# strip_address.py
# ADG Jan 26, 2018
# strips addresses and adds geo info to csv
# source txt comes from:
# https://www.bhamwiki.com/w/List_of_Birmingham_homicides_in_2017

from geopy.geocoders import Nominatim
import usaddress as usa

geolocater = Nominatim()

fn = "2017_raw.txt"
city_name = "Birmingham"
state_name = "AL"
garbage_words = [" of ", " in ", " the "]
address_strings = []

with open(fn) as f:
    total_sep = 0
    row_count = 0
    for i, row in enumerate(f):
        row_count += 1
        location = row.split("on the ")
        if len(location) == 1:
            location = row.split("at the ")
        if len(location) == 1:
            location = row.split(" at ")
        if len(location) == 1:
            location = row.split(" on ")
        if len(location) == 1:
            print("Irregular formatting, must manually format entry number : ", i)
        else:
            location = location[1]
            if "." in location:
                location = location.split(".")[0]
            for word in garbage_words:
                location = location.replace(word, " ")
        address_strings.append(location)


with open("bham_murder_addresses.csv", "a") as fn:
    """ take the address strings, and format them in a way that will be 
        understandable by geopy.  best case is 
        address number streetname city state"""
    usaddress_keys = ["AddressNumber", "StreetName",
                    'StreetNamePostType', 'StreetNamePostDirectional']
    address_details = []
    refined_addresses = []
    for i, address in enumerate(address_strings):
        details = usa.tag(address)[0]

        # create an entry so there aren't errors if address is unparsable, or
        # some other error
        refined_addresses.append("")
        # Build ideal addresses
        for key in usaddress_keys:
            if key in details:
                refined_addresses[i] += details[key]

            refined_addresses[i] += f', {city_name}, {state_name}'

    for ra in refined_addresses:
        print(refined_addresses)