import pygame as pg



def create_grid(screen, num_rows, num_columns, rect_width, rect_height, allowed_colours, board_width):
    # initialising game grid
    '''
    Each sub array represents a vertical column...
    grid = [
        ['R', 'Y', 'Y', 'R', 'Y'],
        [' ', ' ', 'R', 'Y', 'Y'],
        [' ', ' ', ' ', 'R', 'R'],
        ...
    ]
    '''
    
    grid = [['' for _ in range(num_rows)] for _ in range(num_columns)] # logical representation of the game board
    # # test
    # grid = [
    #     ['', '', '', 'Y', 'Y', 'Y'], 
    #     ['', '', '', '', '', ''], 
    #     ['', '', '', '', '', 'R'], 
    #     ['', '', '', '', '', 'R'], 
    #     ['', '', '', '', '', 'R'], 
    #     ['', '', '', '', '', ''], 
    #     ['', '', '', '', '', '']
    # ]
    disk_grid = [
            [pg.Rect(
                (i*rect_width, (j+1)*rect_height), 
                (rect_width, rect_height)
            ) for j in range(num_rows)
        ]
        for i in range(num_columns)
    ]

    screen.fill((0, 0, 0))
    for column in disk_grid:
        for tile in column:
            pg.draw.rect(screen, (0, 69, 115), tile, width=5)
    pg.draw.rect(screen, (8, 4, 120), ((0, rect_height), (num_columns*rect_width, num_rows*rect_height)), 10)

    # player score counters
    pg.draw.circle(
        screen, (0, 69, 115),
        (int(0.5*rect_width), int(0.5*rect_height)), int(min(rect_width, rect_height)//2 * 0.8),    
    )
    pg.draw.circle(
        screen, allowed_colours[0][1],
        (int(0.5*rect_width), int(0.5*rect_height)), int(min(rect_width, rect_height)//2 * 0.7),    
    )
    pg.draw.circle(
        screen, (0, 69, 115),
        (int(board_width-0.5*rect_width), int(0.5*rect_height)), int(min(rect_width, rect_height)//2 * 0.8),    
    )
    pg.draw.circle(
        screen, allowed_colours[1][1],
        (int(board_width-0.5*rect_width), int(0.5*rect_height)), int(min(rect_width, rect_height)//2 * 0.7),    
    )
    return grid, disk_grid