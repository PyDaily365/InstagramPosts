def mission_log():
    # String: space mission log
    log = "Apollo 11: Moon, 1969, Success"
    # Split by spaces (default)
    by_space = log.split() #uses whitespace
    print("By spaces:", by_space)
    # Split by commas (explicit delimiter)
    by_comma = log.split(',') # Keeps spaces
    print("By commas:", by_comma)
    # Clean commas with strip()
    clean = [x.strip() for x in by_comma]
    print("Cleaned:", clean)
mission_log()
# Learn: .split() with commas