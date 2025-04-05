def iss_orbit_log():
    # List: daily ISS orbit counts | Avg orbit 16/day
    orbit_counts = [15, 16, 14, 17]

    #iter(): creates iterator
    orbit_iter = iter(orbit_counts)

    #next(): consumes first two items
    print("Day 1 orbits:", next(orbit_iter)) # Takes 15
    print("Day 2 orbits:", next(orbit_iter)) # Takes 16

    # For loop: starts at next item (14)
    print("Remaining days:")
    for orbits in orbit_iter:
        print(f"Orbits: {orbits}") # Prints 14, 17

iss_orbit_log()
