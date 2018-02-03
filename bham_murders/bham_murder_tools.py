# strip_address.py
# ADG Jan 26, 2018
# strips addresses and adds geo info to csv
# source txt comes from:
# https://www.bhamwiki.com/w/List_of_Birmingham_homicides_in_2017

from geopy.geocoders import Nominatim
import usaddress as usaddress
from datetime import datetime


def strip_address(text):
    '''strip_address: Takes text from bham wiki murder listings page and
            attempts to simplify to more reasonable jumble
        text: string to be simplified
    '''
    garbage_words = [" of ", " in ", " the "]
    lead_in_phrases = ["on the ", "at the ", " at ", " on "]

    location = text.split(lead_in_phrases[0])
    for phrase in lead_in_phrases[1:]:
        if len(location) == 1:
            text.split(phrase)

    if len(location) == 1:
        '''If I wasn't able to simplify the row, mark for manual entry'''
        location = "manual entry"
    else:
        location = location[1]
        if "." in location:
            location = location.split(".")[0]
        for word in garbage_words:
            location = location.replace(word, " ")
    return(location)


def get_ideal_address(text):
    ''' get_ideal_address: builds an ideal address for geolocation
        text: string to be turned "Ideal"
    '''

    usaddress_keys = ['AddressNumber', 'StreetName',
                      'StreetNamePostType', 'StreetNamePostDirectional']

    address_details = usaddress.tag(text)

    if address_details == 'Street Address':
        ideal_address = ""
        for key in usaddress_keys:
            if key in address_details[0]:
                ideal_address += address_details[0][key] + ' '
        ideal_address += ', Birmingham, AL'
    else:
        return("Manual Entry")
    return(ideal_address)


def strip_date(text):
    date = datetime.strptime(text.split[0], "%B %d %Y")
    return(str(date))
