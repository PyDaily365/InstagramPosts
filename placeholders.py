def mars_rover():
    # Perseverance as of March 30, 2025
    distance = 33.56    # Float: km traveled
    days_active = 1462  # Integer: Sols since landing
    speed = 0.14        # Float: km/h max speed
    status = "Rolling"  # String: current status (Norther Rim campaign)
    
    # Interaction with placeholders
    km_per_sol = distance / days_active
    print(f"Pace: {km_per_sol:.4f} km/Sol | Distance: {distance:>5.2f} km")
    message = status + " on the rim!"
    print(f"Status: {message}")

mars_rover()