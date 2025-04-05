def iss_stats():
    # Variables: ISS stats as of March 28, 2025
    orbits = 141117     # Integer: total orbits
    speed = 28000.0     # Float: km/h (17,500 mph = 28,000 km/h)
    time_years = 26.33  # Float: years in orbit (26y, 4m, 8d = 26.33y)
    status = "Active"   # String: mission status

    # Valid interactions
    orbit_time = orbits / (time_years*365) # Int/Float (orbit/day)
    print(f"Orbits: {orbit_time:.3f} per day")
    cheer = status + " mission" # Str + Str
    print(f"Status: {cheer}")

    # Invalid interaction
    try:
        bad_mix = orbits + status # Int + Str fails
        print(bad_mix)
    except TypeError:
        print("Error: Can't add orbits + status!")

iss_stats()
# Learn variable interactions