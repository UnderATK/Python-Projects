from copy import deepcopy
import pygame

from checkers.constants import BLACK, RED

def minimax(position, depth, player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

def simulate_move(soldier, move, board, game, skip):
    board.move(soldier, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    moves = []

    for soldier in board.get_all_soldiers(color):
        valid_moves = board.get_valid_moves(soldier)
        for move, skip in valid_moves.items():
            #draw_moves(game, board, soldier) # Optional option to see the considering moves
            temp_board = deepcopy(board)
            temp_soldier = temp_board.get_soldier(soldier.row, soldier.col)
            new_board = simulate_move(temp_soldier, move, temp_board, game, skip)
            moves.append(new_board) #Store new board as move

    return moves

def draw_moves(game, board, soldier):
    valid_moves = board.get_valid_moves(soldier)
    board.draw(game.window)
    pygame.draw.circle(game.window, (0,255,0), (soldier.x, soldier.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)
