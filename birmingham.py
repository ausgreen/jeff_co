''' birmingham_maps.py

    Lets build some maps for Birmingham!
    By: ADG 1/2/2018
'''

import json
import matplotlib.pyplot as plt

with open('bham_precincts.json', 'rb') as f:
    data = json.load(f)

# print(data.keys())
# print(len(data['features']))
# print(data['features'][0].keys())
# print(data['features'][0]['attributes'])
# print(data['features'][0]['geometry'].keys())


fig = plt.figure()
ax = fig.gca(xlabel='Longitude', ylabel="Latitude")

from shapely.geometry import asShape
from descartes import PolygonPatch

for feat in data["features"]:
    geom = asShape(feat["geometry"])
    x = geom.centroid.x
    y = geom.centroid.y
    ax.plot(x, y, 'ro')
    ax.add_patch(PolygonPatch(feat["geometry"], fc='orange', ec='blue',
                              alpha=0.5, lw=0.5, ls='--', zorder=2))


ax.clear
plt.show()







#
