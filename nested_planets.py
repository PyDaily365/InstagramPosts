def create_planet_dictionary():
    # Create a dictionary where each planet has its own nested dictionary of details
    planets = {
        "Earth": {"type": "Terrestrial", "moons":1},
        "Mars": {"type": "Terrestrial", "moons":2},
        "Jupiter": {"type": "Gas Giant", "moons":95}
    }
    # Add a new planet (Pluto) with its own nested details dynamically
    planets["Pluto"] = {"type": "Dwarf", "moons":5} #Shows dictionaries are mutable
    # Loop through: planet is key, info is nested dict
    for planet, info in planets.items():
        # Access nested values with keys 'type' and 'moons'
        print(f"{planet}: {info["type"]}, {info["moons"]} moons")

create_planet_dictionary()
#Learn: nested dictionaries