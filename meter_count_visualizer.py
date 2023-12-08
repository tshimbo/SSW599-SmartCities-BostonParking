import pandas as pd
import matplotlib.pyplot as plt

# load csv into dataframe
file_path = 'Parking_Meters.csv'
data = pd.read_csv(file_path)

# counts the number of parking meters per street
street_meter_counts = data['STREET'].value_counts()

# select streets with the most parking meters
top_streets = street_meter_counts.head(10)  # looking for the top ten

plt.figure(figsize=(10, 6))
top_streets.plot(kind='bar', color='skyblue')
plt.title('Top Streets with Most Parking Meters')
plt.xlabel('Street Names')
plt.ylabel('Number of Parking Meters')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
