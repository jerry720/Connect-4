from addToColumn import add_to_column
from checkWin import check_win
from checkWin import win
from createGrid import create_grid
from minimax import minimax
import pygame as pg
import random

FPS = 50
WIDTH = 800
HEIGHT = 700
pg.init()
font = pg.font.SysFont(None, 80) # score
font_1 = pg.font.SysFont(None, 50) # display text
font_2 = pg.font.SysFont(None, 30, italic=True)
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


def switch_turn():
    return '<<---' if current_colour == allowed_colours[0][0] else '--->>'


# game constants
info = '(E)-Clear Board | (R)-Reset Game | (X)-AI'
message = ''
previous_msg_width = 0 # for completely blotting out previous message
score_1, score_2 = 0, 0

board_width, board_height = 800, 600
allowed_colours = (('R', (250, 0, 0)), ('Y', (250, 210, 0)))
current_colour = random.choice([_[0] for _ in allowed_colours])
message = switch_turn()

num_columns = 7
num_rows = 6
rect_width, rect_height = board_width // num_columns, board_height // num_rows

# initialize the game board
grid, disk_grid = create_grid(screen, num_rows, num_columns, rect_width, rect_height, allowed_colours, board_width)


running = True
clickable = True # disabled until user resets board
ai_enabled = False
game_over = False
while running:
    # screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_e:
                grid, disk_grid = create_grid(screen, num_rows, num_columns, rect_width, rect_height, allowed_colours, board_width)
                clickable = True
                game_over = False
            elif event.key == pg.K_r:
                score_1, score_2 = 0, 0
                grid, disk_grid = create_grid(screen, num_rows, num_columns, rect_width, rect_height, allowed_colours, board_width)
                clickable = True
                game_over = False
            elif event.key == pg.K_x:
                score_1, score_2 = 0, 0
                grid, disk_grid = create_grid(screen, num_rows, num_columns, rect_width, rect_height, allowed_colours, board_width)
                # assuming the AI is always the second colour
                print('AI enabled')
                ai_enabled = not ai_enabled     
            elif event.key == pg.K_RETURN:
                print(f'clickable: {clickable} | ai_enabled: {ai_enabled} | game_over: {game_over} | current_colour: {current_colour}')
        if event.type == pg.MOUSEBUTTONDOWN and clickable:
            pos = pg.mouse.get_pos()
            # get the column player wishes to drop
            if pos[1] > rect_height:
                selected_col = pos[0] // rect_width
                row_number = add_to_column(grid, current_colour, selected_col)
                # display disk
                if row_number != 999:
                    pg.draw.circle(screen, dict(allowed_colours)[current_colour],
                                (selected_col*rect_width+0.5*rect_width, rect_height*3/2+row_number*rect_height),
                                int(min(rect_width, rect_height)*0.9//2))
                    pg.display.update()
                    # update current colour
                    current_colour = tuple(set([_[0] for _ in allowed_colours])-set(current_colour))[0]
                    message = switch_turn()
                    result = check_win(grid)
                    if result != 999:
                        first = result[0] # draw the first connection detected
                        score_1, score_2 = win(screen, first[0], allowed_colours, first[1], first[2], score_1, score_2, rect_width, rect_height)
                        clickable = False
                        game_over = True

    # AI makes a move
    if current_colour == allowed_colours[1][0] and ai_enabled and not game_over: # AI's turn
        move = minimax(grid, 6, True, current_colour, allowed_colours[0][0])[1]
        grid[move[0]][move[1]] = current_colour
        pg.draw.circle(screen, dict(allowed_colours)[current_colour],
                    (move[0]*rect_width+0.5*rect_width, rect_height*3/2+move[1]*rect_height),
                    int(min(rect_width, rect_height)*0.9//2))
        # update current colour
        current_colour = tuple(set([_[0] for _ in allowed_colours])-set(current_colour))[0]
        message = switch_turn()
        clickable = True
        result = check_win(grid)
        if result != 999:
            first = result[0] # draw the first connection detected
            score_1, score_2 = win(screen, first[0], allowed_colours, first[1], first[2], score_1, score_2, rect_width, rect_height)
            clickable = False # prevent user from clicking
    

    # render texts
    score_1_text = font.render(str(score_1), True, (255, 255, 255), (0, 0, 0))
    score_2_text = font.render(str(score_2), True, (255, 255, 255), (0, 0, 0))
    screen.blit(score_1_text, (int(rect_width*1.2), int(rect_height*0.3)))
    screen.blit(score_2_text, (int(board_width-rect_width*1.4), int(rect_height*0.3)))
    chat = font_1.render(message, True, (255, 255, 255), (0, 0, 0))
    text_width = chat.get_width()
    previous_msg_width = text_width
    screen.blit(chat, (board_width//2-text_width//2, int(rect_height//2.5)))
    # display user options
    user_options = font_2.render(info, True, (255, 255, 255))
    user_options_width = user_options.get_width()
    user_options_height = user_options.get_height()
    user_options_bg = pg.Rect((board_width//2-(user_options_width+60)//2, 0), 
                    (user_options_width+60, int(user_options_height*1.5)))
    pg.draw.rect(screen, (57, 1, 87), user_options_bg)
    screen.blit(user_options, (board_width//2-user_options_width//2, 10))


    clock.tick(FPS)
    pg.display.update()



    