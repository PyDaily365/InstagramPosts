def kinetic_energies():
    velocities = [2,3,4] #m/s
    #Lambda + map: inline KE calc
    ke_lamda = lambda v: 0.5 * 2.0 * (v**2)
    lambda_result = list(map(ke_lamda, velocities))
    # Regular func + loop: explicit KE calc
    def ke_func(v): return 0.5 * 2.0 * (v**2)
    loop_result = []
    for v in velocities:
        loop_result.append(ke_func(v))
    print("Lambda + map:", lambda_result)
    print("Loop + func:", loop_result)
kinetic_energies()
# Learn: lambda + map vs loop