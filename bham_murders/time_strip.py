from datetime import datetime

fn = "2017_raw.txt"
year = "2017"
murder_dates = []
with open(fn) as f:
    for i, row in enumerate(f):
        date = row.split(":")[0]
        murder_dates.append(date + " " + year)

with open("bham_murders.csv", "a") as f:
    for date in murder_dates:
        f.write(str(datetime.strptime(date, "%B %d %Y"))+ ","+"\n")
