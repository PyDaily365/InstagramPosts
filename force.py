def calc_force(mass,accel):
    if mass == 0:
        return "No mass, no force!"
    else:
        return f"{mass * accel}N"
print(f'Force = {calc_force(2,5)}')