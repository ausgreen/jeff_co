'''
Google api only allows 2500 api calls to maps.  I want to do this for free,
and I can split it up so that I can continue this project next weekend if I
run near the limit.

This script is to split up my dataset into < 2500 row chunks
'''

import pandas as pd

df = pd.read_csv('guns_subset.csv')


v = len(df)//5
day_1 = df[:v]
day_2 = df[v:2*v]
day_3 = df[2*v:3*v]
day_4 = df[3*v:4*v]
day_5 = df[4*v:]

# print(day_4)
# print(day_5)
print(len(df))

day_1.to_csv('al_gun_01.csv')
day_2.to_csv('al_gun_02.csv')
day_3.to_csv('al_gun_03.csv')
day_4.to_csv('al_gun_04.csv')
day_5.to_csv('al_gun_05.csv')