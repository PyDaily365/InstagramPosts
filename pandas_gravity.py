import pandas as pd
import requests

# Fetch solar system data from API
url = "https://api.le-systeme-solaire.net/rest/bodies/"
response = requests.get(url)
data = response.json()["bodies"]

# Filter planets by englishName
planets = ["Mercury", "Venus", "Earth", "Mars"]
df = pd.DataFrame([
    {"Planet": p["englishName"], "Mass (kg)": p["mass"]["massValue"] * (10 ** p["mass"]["massExponent"]),
     "Distance (AU)": p["semimajorAxis"] / 1.496e8, "Period (days)": p["sideralOrbit"]}
    for p in data if p["englishName"] in planets
])

# Round and sort by Distance (AU)
df["Distance (AU)"] = df["Distance (AU)"].round(3)
df = df.sort_values("Distance (AU)")

# Calculate Sun's gravitational force (N)
G = 6.67430e-11
sun_mass = 1.989e30
df["Force (N)"] = G * (sun_mass * df["Mass (kg)"]) / (df["Distance (AU)"] * 1.496e11) ** 2

# Display table
print(df[["Planet", "Mass (kg)", "Distance (AU)", "Force (N)"]].to_string(index=False))