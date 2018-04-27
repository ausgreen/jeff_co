import pandas as pd
import os
import glob
import dateutil.parser as dparser

file_location = '../gun-violence-data/intermediate/*'
files = glob.glob(file_location)

df = pd.read_csv(files[0])
alabama = df[df['state'] == 'Alabama']

for i, file in enumerate(files[:]):
    df = pd.read_csv(file)
    alabama = pd.concat([alabama, df[df['state'] == 'Alabama']])

# goal here is to build a CSV file of ALL Alabama incidents
print(alabama.head(3))

dates = list(alabama['date'])

for i, d in enumerate(dates):
    dates[i] = dparser.parse(d).date()

alabama['date'] = dates
alabama.to_csv('./alabama_gun_violence.csv')