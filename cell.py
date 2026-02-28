
RESET = "\033[0m"


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"W": True, "S": True, "N": True, "E": True}


def create_grid(width, height):
    result = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(Cell(x, y))
        result.append(row)
    return result


def print_maze(grid, entry, exit, color="\033[97m"):
    height = len(grid)
    width = len(grid[0])
    ex, ey = exit
    sx, sy = entry

    # ===== Top Border =====
    top_line = "┌"
    for x in range(width):
        top_line += "───" if grid[0][x].walls["N"] else "   "
        if x < width - 1:
            top_line += "┬"
    top_line += "┐"
    print(color + top_line + RESET)

    for y in range(height):

        # ===== Middle Line =====
        middle_line = ""
        for x in range(width):

            middle_line += "│" if grid[y][x].walls["W"] else " "

            if (x, y) == (sx, sy):
                middle_line += " S "
            elif (x, y) == (ex, ey):
                middle_line += " G "
            else:
                middle_line += "   "

        middle_line += "│" if grid[y][width - 1].walls["E"] else " "
        print(color + middle_line + RESET)

        # ===== Separator =====
        if y < height - 1:
            separator = "├"
            for x in range(width):
                separator += "───" if grid[y][x].walls["S"] else "   "
                if x < width - 1:
                    separator += "┼"
            separator += "┤"
            print(color + separator + RESET)

    # ===== Bottom Border =====
    bottom_line = "└"
    for x in range(width):
        bottom_line += "───" if grid[height - 1][x].walls["S"] else "   "
        if x < width - 1:
            bottom_line += "┴"
    bottom_line += "┘"
    print(color + bottom_line + RESET)

