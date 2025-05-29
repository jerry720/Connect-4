import pygame as pg


# scan the board for 4-in-a-row of a given colour
# returns the first and last coordinate in the 4-in-a-row sequence
# starting from left, top and top-left respectively
def check_win(grid) -> list:

    # check horizontal
    def check_horizontal():
        connections = [] # collect all instances of connect-4
        for i in range(len(grid[0])): # iterate over each row
            count = 0
            current = ''
            for j in range(len(grid)):
                if bool(grid[j][i].strip()): # non-space character
                    if current != grid[j][i]:
                        current = grid[j][i]
                        count = 1
                    else:
                        count += 1
                        if count >= 4:
                            connections.append((current, (j-3, i), (j, i))) # (<win_colour>, <column>, <row>)
                else: # found a discontinuity
                    current = 0
        return connections
    
    def check_vertical():
        connections = []
        for i in range(len(grid)):
            count = 0
            current = ''
            for j in range(len(grid[i])):
                if bool(grid[i][j].strip()):
                    if current != grid[i][j]:
                        current = grid[i][j]
                        count = 1
                    else:
                        count += 1
                        if count >= 4:
                            connections.append((current, (i, j-3), (i, j)))
                else:
                    current = 0
        return connections
                    
    def check_diagonal():
        connections = []
        # checking from top-left to bottom-right
        for i in range(len(grid)-3):
            for j in range(len(grid[0])-3):
                if bool(grid[i][j].strip()):
                    # iterate horizontally-down by 3 squares
                    for k in range(1, 4):
                        if grid[i+k][j+k] != grid[i][j]:
                            k -= 1
                            break
                    if k == 3:
                        connections.append((grid[i][j], (i, j), (i+k, j+k)))
        # check from bottom-left to top-right
        for i in range(len(grid)-3):
            for j in range(len(grid[0])-1, 2, -1):
                if bool(grid[i][j].strip()):
                    # iterate horizontally-up by 3 squares
                    for k in range(1, 4):
                        if grid[i+k][j-k] != grid[i][j]:
                            k -= 1
                            break
                    if k == 3:
                        connections.append((grid[i][j], (i, j), (i+k, j-k)))
        return connections

    result = check_horizontal() + check_vertical() + check_diagonal()
    if result: return result
    else: return 999


def win(screen, colour, allowed_colours, start_coord, end_coord, score_1, score_2, rect_width, rect_height):
    # draw line from start coord to end cord (connect 4)
    # display win message
    if start_coord[0] == end_coord[0]:
        pos_1 = (int(start_coord[0]*rect_width+0.5*rect_width), 
                 int(start_coord[1]*rect_height+rect_height))
        pos_2 = (int(end_coord[0]*rect_width+0.5*rect_width),
                 int(end_coord[1]*rect_height+2*rect_height))
    elif start_coord[1] == end_coord[1]:
        pos_1 = (int(start_coord[0]*rect_width),
                 int(start_coord[1]*rect_height+1.5*rect_height))
        pos_2 = (int(end_coord[0]*rect_width+rect_width),
                 int(end_coord[1]*rect_height+1.5*rect_height))
    else: # connection is diagnal
        if start_coord[1] < end_coord[1]:
            pos_1 = (int(start_coord[0]*rect_width),
                    int(start_coord[1]*rect_height+rect_height))
            pos_2 = (int(end_coord[0]*rect_width+rect_width),
                    int(end_coord[1]*rect_height+2*rect_height))
        elif start_coord[1] > end_coord[1]:
            pos_1 = (int(start_coord[0]*rect_width),
                     int(start_coord[1]*rect_height+2*rect_height))
            pos_2 = (int(end_coord[0]*rect_width+rect_width),
                     int(end_coord[1]*rect_height+rect_height))
    pg.draw.line(screen, (255, 255, 255), pos_1, pos_2, 4)
    if colour == allowed_colours[0][0]:
        return score_1+1, score_2
    else: return score_1, score_2+1




# test_grid = [
#     ['', '', '', '', 'Y', 'Y'], 
#     ['', '', '', 'Y', 'R', 'R'], 
#     ['', '', '', '', 'Y', 'R'], 
#     ['', '', 'Y', '', 'R', 'Y'], 
#     ['', '', '', 'R', '', 'R'], 
#     ['', '', 'R', '', 'Y', ''], 
#     ['R', 'R', '', '', '', '']
# ]
# print(check_win(test_grid))

