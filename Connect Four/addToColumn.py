
# makes in-place changes on the grid passed in
def add_to_column(grid, colour, column_num):
    for i in range(len(grid[column_num])-1, -1, -1):
        if not bool(grid[column_num][i].strip()): # finds empty square
            grid[column_num][i] = colour
            return i # return row number inserted
    return 999 # column is full
    