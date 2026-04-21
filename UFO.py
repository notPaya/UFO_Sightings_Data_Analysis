import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("ufo_sightings.csv")

# Create map
fig = px.scatter_geo(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    title="UFO Sightings Around the World",
)

fig.show()