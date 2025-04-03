def create_planet_dictionary():
    planets = {
        "Earth": "Only known planet with life",
        "Mars": "Known as the Red Planet",
        "Jupiter": "Largest planet in our Solar System"
    }
    #add planet to dictionary
    planets["Pluto"] = "Classified as a dwarf planet"
    for planet, fact in planets.items():
        print(f"{planet}: {fact}")
create_planet_dictionary()
#Learn: dictionaries + key-value pairs