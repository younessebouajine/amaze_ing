# from cell import create_grid, cell
# from parsing import read_file
# from cell import print_maze


# config = read_file()
# width = config["WIDTH"]
# height = config["HEIGHT"]
# entry = config["ENTRY"]
# exit = config["EXIT"]

# grid = create_grid(width, height)


# print_maze(grid, entry, exit)

# print("\n\n")

# print("═" * 40)
# print("║{:^38}║".format("A-Maze-ing"))
# print("╠" + "═" * 38 + "╣")
# print("║ {:<36} ║".format("1. Re-generate a new maze"))
# print("║ {:<36} ║".format("2. Show/Hide path from entry to exit"))
# print("║ {:<36} ║".format("3. Rotate maze colors"))
# print("║ {:<36} ║".format("4. Quit"))
# print("╚" + "═" * 38 + "╝")
# choice = input("Choice? (1-4): ")
# import os
# def execute_choice(cc):
#     if int(cc)==3:
#         os.system("clear")
# execute_choice(choice)


import os
from colorama import init
from parsing import read_file
from cell import create_grid, print_maze

init()  # Windows support

# ANSI Colors
COLORS = [
    "\033[97m",  # White
    "\033[92m",  # Green
    "\033[94m",  # Blue
    "\033[93m",  # Yellow
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]

color_index = 0

config = read_file()
width = config["WIDTH"]
height = config["HEIGHT"]
entry = config["ENTRY"]
exit = config["EXIT"]

grid = create_grid(width, height)


while True:
    os.system("clear" if os.name != "nt" else "cls")

    print_maze(grid, entry, exit, COLORS[color_index])

    print("\n")
    print("═" * 40)
    print("║{:^38}║".format("A-Maze-ing"))
    print("╠" + "═" * 38 + "╣")
    print("║ {:<36} ║".format("1. Re-generate a new maze"))
    print("║ {:<36} ║".format("2. Show/Hide path from entry to exit"))
    print("║ {:<36} ║".format("3. Rotate maze colors"))
    print("║ {:<36} ║".format("4. Quit"))
    print("╚" + "═" * 38 + "╝")

    choice = input("Choice? (1-4): ")

    try:
        choice = int(choice)
    except ValueError:
        continue

    if choice == 1:
        grid = create_grid(width, height)

    elif choice == 3:
        color_index = (color_index + 1) % len(COLORS)

    elif choice == 4:
        print("Goodbye 👋")
        break