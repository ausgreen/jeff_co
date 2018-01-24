import folium

# Folium defaults to OpenStreetMap tiles, but Stamen Terrain, Stamen Toner, Mapbox Bright, and Mapbox Control room tiles are built in:
map_osm = folium.Map(location=[33.5104173, -86.806683], tiles='Stamen Toner', zoom_start=15)

folium.GeoJson(open('bham_precincts.json'), name='geojson').add_to(map_osm)

map_osm.save('birmingham_toner.html')