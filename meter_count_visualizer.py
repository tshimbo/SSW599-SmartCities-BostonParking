import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'Parking_Meters.csv'
data = pd.read_csv(file_path)

# Count the number of parking meters per street
street_meter_counts = data['STREET'].value_counts()

# Select streets with the most parking meters (you can change the number if desired)
top_streets = street_meter_counts.head(10)  # Top 10 streets

# Plotting the streets with most parking meters
plt.figure(figsize=(10, 6))
top_streets.plot(kind='bar', color='skyblue')
plt.title('Top Streets with Most Parking Meters')
plt.xlabel('Street Names')
plt.ylabel('Number of Parking Meters')
plt.xticks(rotation=45)  # Rotates x-axis labels for better readability
plt.tight_layout()
plt.show()
