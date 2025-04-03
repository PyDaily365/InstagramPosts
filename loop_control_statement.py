def find_number(target):
    numbers = [3,7,12,19,25]
    for num in numbers:
        if num == target:
            print(f"Found {target}!")
            break
        print(f"Checking {num}...")
    else:
        print(f"{target} not found.")
find_number(12)
#Learn: break stops loop early