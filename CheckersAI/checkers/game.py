import pygame
from .constants import RED, BLACK, LIGHT_GREY, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self, window):
        self._init()
        self.window = window

    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        soldier = self.board.get_soldier(row, col)
        if soldier != 0 and soldier.color == self.turn:
            self.selected = soldier
            self.valid_moves = self.board.get_valid_moves(soldier)
            return True

        return False

    def _move(self, row, col):
        soldier = self.board.get_soldier(row, col)
        if self.selected and soldier == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]

            if skipped:
                self.board.remove(skipped)

            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, LIGHT_GREY, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 10)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = RED
        else:
            self.turn = BLACK

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()