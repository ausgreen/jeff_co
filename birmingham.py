''' birmingham_maps.py

    Lets build some maps for Birmingham!
    By: ADG 1/2/2018
'''

import json
import matplotlib.pyplot as plt
import clean_summary_report as csr


with open('bham_precincts.json', 'rb') as f:
    data = json.load(f)

fig = plt.figure()
ax = fig.gca(xlabel='Longitude', ylabel="Latitude")

from shapely.geometry import asShape
from descartes import PolygonPatch

votes = csr.clean_summary_report("summary_report.txt")

for feat in data["features"]:
    # kinda confusing-> take voting info from votes where precinct is current precinct
    prec_votes = votes[feat["properties"]["PREC"]]
    geom = asShape(feat["geometry"])
    x = geom.centroid.x
    y = geom.centroid.y
    ax.plot(x, y, ',')

    # color differently based upon number of votes
    if prec_votes["votes_jones"] > prec_votes["votes_moore"]:
        ax.add_patch(PolygonPatch(feat["geometry"], fc='blue', ec='blue',
                                  alpha=0.5, lw=0.5, ls='--', zorder=2))

ax.clear
plt.show()

