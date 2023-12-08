import pandas as pd
import matplotlib.pyplot as plt

# load csv into dataframe
file_path = 'Parking_Meters.csv'
data = pd.read_csv(file_path)

# grouping the data by street
# calculation for mean meter cost per street
street_meter_costs = data.groupby(
    'STREET')['BASE_RATE'].mean().sort_values(ascending=False).head(20)

# plot the top 20 streets with the highest mean meter costs
plt.figure(figsize=(12, 8))
street_meter_costs.plot(kind='bar', color='skyblue')
plt.title('Top 20 Streets with Highest Mean Meter Costs')
plt.xlabel('Street')
plt.ylabel('Mean Meter Cost')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
