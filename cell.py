
class cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"W": True, "S": True, "N": True, "E": True}



def create_grid(width, height):

    row = []
    result: list[list[cell]] = []


    for y in range(height):
        for x in range(width):
            obj = cell(x, y)
            row.append(obj)
        result.append(row)
        row = []
    return result



def print_maze(grid):
    height = len(grid)
    width = len(grid[0])

    for y in range(height):

        # --- Print top walls of current row ---
        top_line = "+"
        for x in range(width):
            if grid[y][x].walls["N"]:
                top_line += "----+"
            else:
                top_line += "    +"
        print(top_line)

        # --- Print side walls of current row ---
        middle_line = ""
        for x in range(width):
            if grid[y][x].walls["W"]:
                middle_line += "|"
            else:
                middle_line += " "

            middle_line += "    "  # cell interior space

        # Last right wall of the row
        if grid[y][width - 1].walls["E"]:
            middle_line += "|"
        else:
            middle_line += " "

        print(middle_line)

    # --- Print bottom border ---
    bottom_line = "+"
    for x in range(width):
        if grid[height - 1][x].walls["S"]:
            bottom_line += "----+"
        else:
            bottom_line += "    +"
    print(bottom_line)





# def get_hexa(c: cell):

#     res = 0

#     if (c.walls["N"]):
#         res |= 1
    
#     if (c.walls["E"]):
#         res |= 2
    
#     if (c.walls["S"]):
#         res |= 4
    
#     if (c.walls["W"]):
#         res |= 8
    
#     return format(res, 'X')





# def write_to_file(grid):

#     height = len(grid)
#     width = len(grid[0])

#     for y in range(height):
#         for x in range(width):
#             print(get_hexa(grid[y][x]), end='')
#         print()










grid = create_grid(10, 15)


# grid[1][1].walls = {"W": True, "S": True, "N": True, "E": False}


print_maze(grid)




# write_to_file(grid)