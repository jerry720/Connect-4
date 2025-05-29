from copy import deepcopy
from checkWin import check_win
import random
import pprint


'''# max_ai is a boolean value
def minimax(board, depth, max_ai, ai_colour, player_colour, alpha=float('-inf'), beta=float('inf')) -> tuple:
    result = check_win(board)
    if result != 999:
        # AI win: large positive, Player win: large negative
        result_colours = [_[0] for _ in result]
        if ai_colour in result_colours:
            return (1000000 + depth, tuple())  # Prefer faster wins
        elif player_colour in result_colours:
            return (-1000000 - depth, tuple()) # Prefer slower losses
    if depth == 0 or not get_all_moves(board):
        return evaluate(board, ai_colour, player_colour), tuple()
    else:
        best_move = None
        if max_ai: # ai wants to maximise their score
            max_eval = float('-inf')
            for move in get_all_moves(board):
                evaluation = minimax(simulate_move(board, ai_colour, move), depth-1, False, ai_colour, player_colour, alpha, beta)[0]
                max_eval = max(max_eval, evaluation)
                if max_eval == evaluation:
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else: # ai wants to minimise player score
            min_eval = float('inf')
            for move in get_all_moves(board):
                evaluation = minimax(simulate_move(board, player_colour, move), depth-1, True, ai_colour, player_colour, alpha, beta)[0]
                min_eval = min(min_eval, evaluation)
                if min_eval == evaluation:
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_eval, best_move'''
        

def minimax(board, depth, max_ai, ai_colour, player_colour, alpha=float('-inf'), beta=float('inf')) -> tuple:
    result = check_win(board)
    if result != 999:
        # AI win: large positive, Player win: large negative
        result_colours = [_[0] for _ in result]
        if ai_colour in result_colours:
            return (1000000 + depth, tuple())  # Prefer faster wins
        elif player_colour in result_colours:
            return (-1000000 - depth, tuple()) # Prefer slower losses
    if depth == 0 or not get_all_moves(board):
        return evaluate(board, ai_colour, player_colour), tuple()
    else:
        best_move = None
        if max_ai:
            max_eval = float('-inf')
            moves = get_all_moves(board)
            random.shuffle(moves)
            for move in moves:
                evaluation = minimax(simulate_move(board, ai_colour, move), depth-1, False, ai_colour, player_colour, alpha, beta)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, max_eval)  # Use max_eval, not evaluation
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            moves = get_all_moves(board)
            random.shuffle(moves)
            for move in moves:
                evaluation = minimax(simulate_move(board, player_colour, move), depth-1, True, ai_colour, player_colour, alpha, beta)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, min_eval)  # Use min_eval, not evaluation
                if beta <= alpha:
                    break
            return min_eval, best_move


# returns list of coordinates of allowed moves
# connect-4 is simple in that both colours have the same allowed moves
def get_all_moves(board) -> list:
    allowed_moves = []
    for i in range(len(board)):
        for j in range(len(board[0])-1, -1, -1):
            if not bool(board[i][j]):
                allowed_moves.append((i, j))
                break
    return allowed_moves


# returns a copy of the grid after a hypothetical move has been made
# the move parameter: (<col>, <row>), where <col> is a 1D array
def simulate_move(board, colour, move) -> list:
    temp_board = deepcopy(board)
    if not temp_board[move[0]][move[1]]: # only move is current square is not empty
        temp_board[move[0]][move[1]] = colour
    return temp_board


# calculates the minimax score based on the number of connections formed
def evaluate(board, ai_colour, player_colour) -> int:
    result = check_win(board)
    if result == 999:
        return 0
    else:
        result = [_[0] for _ in result] # get all the colours
        return result.count(ai_colour) - result.count(player_colour)




if __name__ == '__main__':
    from checkWin import check_win
    test_grid = [
        ['', '', '', '', '', ''], 
        ['', '', '', '', '', ''], 
        ['', '', 'Y', '', '', ''], 
        ['', 'Y', '', '', '', 'R'], 
        ['Y', '', '', '', 'R', ''], 
        ['', '', '', 'R', '', 'Y'], 
        ['', '', 'R', '', '', '']
    ]

    print(check_win(test_grid))

    # test_grid_1 = [
    #     ['', '', '', '', '', ''], 
    #     ['', '', '', '', '', ''], 
    #     ['Y', 'Y', 'Y', '', '', ''], 
    #     ['', 'Y', 'Y', '', '', ''], 
    #     ['Y', 'R', 'R', '', '', ''], 
    #     ['', '', '', '', '', ''], 
    #     ['', '', '', '', '', ''], 
    # ]
    # print(check_win(test_grid_1))

