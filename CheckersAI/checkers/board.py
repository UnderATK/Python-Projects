import pygame
from .constants import DARKER_BROWN, ROWS, COLS, LIGHT_BROWN, SQUARE_SIZE, BLACK, RED
from .soldier import Soldier
class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.black_left = 12
        self.red_kings = self.black_kings = 0
        self.create_board()

    def draw_squares(self, window):
        window.fill(DARKER_BROWN)

        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, LIGHT_BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.red_left - self.black_left + (self.red_kings * 0.5 - self.black_kings * 0.5)

    def get_all_soldiers(self, color):
        soldiers = []
        for row in self.board:
            for soldier in row:
                if soldier != 0 and soldier.color == color:
                    soldiers.append(soldier)
        return soldiers

    def move(self, soldier, row, col):
        self.board[soldier.row][soldier.col], self.board[row][col] = self.board[row][col], self.board[soldier.row][soldier.col]
        soldier.move(row, col)

        if row == ROWS - 1 or row == 0:
            soldier.make_king()
            if soldier.color == BLACK:
                self.black_kings += 1
            else:
                self.red_kings += 1

    def get_soldier(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Soldier(row, col, RED))
                    elif row > 4:
                        self.board[row].append(Soldier(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                soldier = self.board[row][col]
                if soldier != 0:
                    soldier.draw(window)

    def remove(self, soldiers):
        for soldier in soldiers:
            self.board[soldier.row][soldier.col] = 0
            if soldier != 0:
                if soldier.color == BLACK:
                    self.black_left -= 1
                else:
                    self.red_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return 'The winner is: BLACK'
        elif self.black_left <= 0:
            return 'The winner is: RED (AI)'

        return None

    def get_valid_moves(self, soldier):
        moves = {}
        left = soldier.col - 1
        right = soldier.col + 1
        row = soldier.row

        if soldier.color == BLACK or soldier.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, soldier.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, soldier.color, right))

        if soldier.color == RED or soldier.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, soldier.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, soldier.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, -1)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break

            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
