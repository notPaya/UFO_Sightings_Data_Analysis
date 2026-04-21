import pandas as pd
import folium

df = pd.read_csv("ufo_sightings.csv", low_memory=False)

# Convert coordinates to numbers
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# Remove rows with invalid coordinates
df = df.dropna(subset=["latitude", "longitude"])

# Optional: sample rows for speed
df = df.sample(5000)

# Create map
ufo_map = folium.Map(location=[20, 0], zoom_start=2)

for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        popup=row["city"],
        color="red"
    ).add_to(ufo_map)
ufo_map.save("ufo_map.html")