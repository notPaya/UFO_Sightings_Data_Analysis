import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# -----------------------------
# 1. UCITAVANJE PODATAKA
# -----------------------------
df = pd.read_csv("ufo_sightings.csv", low_memory=False)

# -----------------------------
# 2. ČIŠĆENJE DATUMA I VREMENA
# -----------------------------
df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")

# -----------------------------
# 3. IZDVAJANJE GODINE, MJESECA, SATA
# -----------------------------
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["hour"] = df["datetime"].dt.hour

# -----------------------------
# 4. ANALIZA PODATAKA
# -----------------------------

# 4.1 Viđenja godišnje
year_counts = df["year"].value_counts().sort_index()

plt.figure()
year_counts.plot()
plt.title("UFO Sightings per Year")
plt.xlabel("Year")
plt.ylabel("Number of Sightings")
plt.show()

# -----------------------------
# 4.2 Viđenja po državi
country_counts = df["country"].value_counts().head(10)

plt.figure()
country_counts.plot(kind="bar")
plt.title("Top 10 Countries with UFO Sightings")
plt.xlabel("Country")
plt.ylabel("Number of Sightings")
plt.show()

# -----------------------------
# 4.3 Najčešći oblici NLO-a
shape_counts = df["shape"].value_counts().head(10)

plt.figure()
shape_counts.plot(kind="bar")
plt.title("Most Common UFO Shapes")
plt.xlabel("Shape")
plt.ylabel("Number of Sightings")
plt.show()

# -----------------------------
# 5. MAPA SVIJETA (Plotly)
# -----------------------------

# Čišćenje koordinata
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

df = df.dropna(subset=["latitude", "longitude"])

# (opcionalno) uzorak zbog brzine
df_sample = df.sample(5000)
plt = px.scatter_geo(
    df_sample,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    title="UFO Sightings Around the World",
)

plt.show()