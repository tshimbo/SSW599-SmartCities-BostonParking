import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Read CSV data
csv_file_path = "Parking_Meters.csv"
df = pd.read_csv(csv_file_path)

# Drop rows with missing latitude or longitude values
df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

# Check if there are any remaining missing values
if df[['LATITUDE', 'LONGITUDE']].isnull().values.any():
    print("Warning: There are still missing values in LATITUDE or LONGITUDE columns.")

# Create a folium map centered at the mean coordinates of your data
map_center = [df['LATITUDE'].mean(), df['LONGITUDE'].mean()]
mymap = folium.Map(location=map_center, zoom_start=12)

# Create a MarkerCluster to group markers
marker_cluster = MarkerCluster().add_to(mymap)

# Add markers for each data point
for index, row in df.iterrows():
    coordinates = [row['LATITUDE'], row['LONGITUDE']]

    # Customize the popup content based on your CSV columns
    popup_text = f"Meter ID: {row['METER_ID']}<br>Vendor: {row['VENDOR']}"

    # Create a marker with popup
    marker = folium.Marker(location=coordinates, popup=popup_text)
    marker.add_to(marker_cluster)

# Save the map as an HTML file
mymap.save("interactive_map_with_popup.html")
