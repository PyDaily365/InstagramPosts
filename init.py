class Planet:
    def __init__(self, name, distance_from_sun, moons):
        self.name = name
        self.distance_from_sun = distance_from_sun # in million km
        self.moons = moons
        self.probe_visits = []

    def add_probe_visit(self, probe_name):
        self.probe_visits.append(probe_name)
        return f"{probe_name} visited {self.name}"
    
    def get_moon_count(self):
        return f"{self.name} has {self.moons} known moons."
    
# Distances and moon counts as of 2025
mars = Planet ("Mars", 227.9, 2) # 227.9 km, 2 moons (Phobos, Deimos)
saturn = Planet("Saturn", 1427, 83) # 1427M km, 83 confirmed moons

mars.add_probe_visit("Perseverance") # Landed 2021
saturn.add_probe_visit("Cassini") # Orbited 2004-2017
print(mars.get_moon_count())
print(f"{saturn.name}'s distance: {saturn.distance_from_sun}")