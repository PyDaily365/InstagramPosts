# Newton's Gravitation: F = G * (m1 * m2) / r²
G = 6.67430e-11  # Gravitational constant (m³/kg/s²)

def gravity_force(m1_kg, m2_kg, r_m):
    #Force (N) between two masses (kg) at distance (m)
    return G * (m1_kg * m2_kg) / (r_m ** 2)

# Space examples (NASA, 2025)
earth_moon = (5.972e24, 7.342e22, 384400000)  # Earth, Moon, 384,400 km
mars_phobos = (6.417e23, 1.0659e16, 9378000)  # Mars, Phobos, 9,378 km

# Calculate forces
f_earth_moon = gravity_force(*earth_moon)
f_mars_phobos = gravity_force(*mars_phobos)

# Output as table
print(f"{'Pair':<16} {'Force (N)'}")
print("-" * 28)
print(f"{'Earth-Moon':<16} {f_earth_moon:.2e} N")
print(f"{'Mars-Phobos':<16} {f_mars_phobos:.2e} N")
# Learned: Newton’s law calculates space gravity