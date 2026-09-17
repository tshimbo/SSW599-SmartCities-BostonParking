# Boston Parking Finder — SSW599 Smart Cities

Maps every public parking meter in Boston using the city's open data, to make finding parking faster and cut down on traffic from drivers circling for a spot.

**Data source:** [Analyze Boston — Parking Meters](https://bostonopendata-boston.opendata.arcgis.com/datasets/boston::parking-meters/about)

## What it does
- `SSW599BostonParking.py` — builds an interactive map (`Boston_Parking_Map.html`) with a popup for each meter
- `rate_visualizer.py` — visualizes meter pricing
- `meter_count_visualizer.py` — visualizes meter density by area

## Run it locally
```bash
pip install pandas folium
python3 SSW599BostonParking.py
```
Then open the generated `Boston_Parking_Map.html` in your browser.

## Tech
Python · pandas · folium · GeoJSON
