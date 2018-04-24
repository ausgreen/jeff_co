''' gun_locations.py

    By: Austin Green, April 22 2018
    Goal of this file is to map out all locations of gun incidents in alabama

'''
import sys
sys.path.append("../")
import keys
import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key=keys.GOOGLE_API_KEY)
filename = 'al_gun_01.csv'

data = pd.read_csv(filename)
print(data.head())
bad_address_count = 0


test_result = gmaps.geocode(data['address'][0] +
                                   ', ' +
                                   str(data['city_or_county'][0]) +
                                   ', AL')
print(test_result[0]['geometry']['location']['lat'])


for i, addr in enumerate(data['address']):
    if i % 100 == 0:
        print("% complete : ", 100*i/len(data['address']))

    geocode_result = gmaps.geocode(str(addr) +
                                   ', ' +
                                   str(data['city_or_county'][i]) +
                                   ', AL')
    if geocode_result:
        data.loc[i,'latitude'] = geocode_result[0]['geometry']['location']['lat']
        data.loc[i,'longitude'] = geocode_result[0]['geometry']['location']['lng']
    else:
        print("oops, that address didn't work")
        bad_address_count += 1

print('number of bad addresses: ', bad_address_count)
data.to_csv(filename)