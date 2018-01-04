''' birmingham_maps.py

    Lets build some maps for Birmingham!
    By: ADG 1/2/2018
'''

import json
import matplotlib.pyplot as plt
import clean_summary_report as csr
import matplotlib.cm as cm
import matplotlib.colors as colors
import math
import numpy as np
from shapely.geometry import asShape, LineString
from descartes import PolygonPatch


with open('bham_precincts.json', 'rb') as f:
    data = json.load(f)

fig = plt.figure()
ax = fig.gca(xlabel='Longitude', ylabel="Latitude")

votes = csr.clean_summary_report("summary_report.txt")
# print(len(votes), data["features"][0]['properties']['PREC'])

for feat in data["features"]:
    try:
        # kinda confusing-> take voting info from votes where precinct is current precinct
        prec_votes = votes[feat["properties"]["PREC"]]
        geom = asShape(feat["geometry"])
    except Exception:
        print(repr(Exception))

    jones_votes = prec_votes["votes_jones"]
    moore_votes = prec_votes["votes_moore"]
    total_votes = jones_votes + moore_votes + prec_votes["votes_write_in"]

    x = geom.centroid.x
    y = geom.centroid.y
    ax.plot(x, y, 'b,')

    print(jones_votes, moore_votes, total_votes)
    # color differently based upon number of votes
    if jones_votes > moore_votes:
        color = cm.coolwarm

        ax.add_patch(PolygonPatch(feat["geometry"],
                                  fc=color(1 - (jones_votes/total_votes)),
                                  ec='grey',
                                  alpha=1,
                                  lw=0.5,
                                  ls=':',
                                  zorder=2))
    else:
        ax.add_patch(PolygonPatch(feat["geometry"],
                                  fc='black',
                                  ec='black',
                                  alpha=0.5,
                                  lw=0.5,
                                  ls='--',
                                  zorder=2))

with open('interstates.json') as f:
    interstates = json.load(f)

for feat in interstates['features']:
    line = LineString(feat["geometry"]["coordinates"])
    x, y = line.xy
    im = ax.plot(x, y, color='green', alpha=0.3)

ax.set_title("Bham Special Senate Election Voting")
ax.axes.yaxis.set_visible(False)
ax.axes.xaxis.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

cax = fig.add_axes([0.27, 0.1, 0.5, 0.02])
cax.set_title("Voting Percentage")
cax.axes.yaxis.set_ticklabels([])
cax.axes.yaxis.set_visible(False)
cax.axes.xaxis.set_ticklabels(["Jones", "50-50", "Moore"])
cax.set_xlim(0, 100)
major_xticks = np.linspace(0, 100, 3)
cax.set_xticks(major_xticks)

gradient = np.linspace(0, 1, 101)
gradient = np.vstack((gradient, gradient))
cax.imshow(gradient, aspect='auto', cmap=color, alpha=0.9)

labels = ["100% Jones", "50-50", "100% Moore"]

# plt.show()
plt.savefig('bham.png', dpi=130)
