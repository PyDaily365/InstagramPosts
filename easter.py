import random, time, os
colors = ["\033[95m", "\033[96m", "\033[93m"]  # Pastel pink, cyan, yellow
reset = "\033[0m"
bunny = r"""
(\(\
(-.-)
O_(")(")
"""
msg = "Happy Easter!"
for _ in range(5):
    os.system("cls" if os.name == "nt" else "clear")  # Clear terminal
    color = random.choice(colors)
    print(f"{color}{msg}{reset}")
    print(bunny)
    time.sleep(0.5)