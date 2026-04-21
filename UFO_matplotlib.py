import pandas as pd
import matplotlib.pyplot as plt

#Load database
df = pd.read_csv ("ufo_sightings.csv", low_memory=False)

#Convert datatime column
df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")

# Extract year
df["year"] = df["datetime"].dt.year

# Count sightings per year
year_counts = df["year"].value_counts().sort_index()
plt.figure()
year_counts.plot()

plt.title("UFO Sightings per Year")
plt.xlabel("Year")
plt.ylabel("Number of Sightings")

plt.show()
