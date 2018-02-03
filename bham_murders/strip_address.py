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

# Extract rows from file and try to split/select on address header keywords
with open(fn) as f:
    for i, row in enumerate(f):
        location = row.split("on the ")
        if len(location) == 1:
            location = row.split("at the ")
        if len(location) == 1:
            location = row.split(" at ")
        if len(location) == 1:
            location = row.split(" on ")
        if len(location) == 1:
            print("Irregular formatting, must manually format entry number : ", i)
            location = "None"
        else:
            location = location[1]
            if "." in location:
                location = location.split(".")[0]
            for word in garbage_words:
                location = location.replace(word, " ")
        address_strings.append(location)


# Build
address_details = []
for i,a in enumerate(address_strings):
    # builds orderedDict
    address_details.append("")
    try:
        address_details[i] = usa.tag(a)
    except:
        print("Unable to create detailed address")
        address_details[i] = "None"

actual_address = []
usa_keys = ['AddressNumber', 'StreetName', 'StreetNamePostType', 'StreetNamePostDirectional']
for i,a in enumerate(address_details):
    try:
        actual_address.append("")
        if address_details[i][1] == 'Street Address':
            for key in usa_keys:
                if key in address_details[i][0]:
                    actual_address[i] += address_details[i][0][key] + ' '
            actual_address[i] += ',Birmingham, AL'
        else:
            actual_address[i] += 'NA'
    except:
        print("Error building address")
        actual_address[i] += "None"


locations = []
for i,a in enumerate(actual_address):
    if a is not "NA":
        gl = geolocater.geocode(a)
        locations.append(gl)
    else:
        locations.append(f"{i} - NA")

for l in locations:
    print(l)