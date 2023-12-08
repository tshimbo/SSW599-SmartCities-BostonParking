import pandas as pd
import folium
from folium.plugins import MarkerCluster

# parse through csv data
csv_file_path = "Parking_Meters.csv"
df = pd.read_csv(csv_file_path)

# error checking 
df = df.dropna(subset=['LATITUDE', 'LONGITUDE', 'OBJECTID'])

# error checking
if df[['LATITUDE', 'LONGITUDE', 'OBJECTID']].isnull().values.any():
    print("Warning: There are still missing values in LATITUDE, LONGITUDE, or OBJECTID columns.")

# folium map is made using the mean of the csv data
map_center = [df['LATITUDE'].mean(), df['LONGITUDE'].mean()]
mymap = folium.Map(location=map_center, zoom_start=12)


marker_cluster = MarkerCluster().add_to(mymap)

# add markers for every CSV data point
for index, row in df.iterrows():
    coordinates = [row['LATITUDE'], row['LONGITUDE']]

    # map pointer data showing specific things
    popup_text = f"Object ID: {row['OBJECTID']}<br>Base Rate: {row['BASE_RATE']}<br>Vendor: {row['VENDOR']}"

    # create marker with the popup data
    marker = folium.Marker(location=coordinates, popup=popup_text)
    marker.add_to(marker_cluster)

# saving map as HTML
mymap.save("Boston_Parking_Map.html")
