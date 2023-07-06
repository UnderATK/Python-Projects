import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
VERSION = '1.0.0'
pygame.display.set_caption('CheckersAI - v' + VERSION)
pygame.display.set_icon(pygame.image.load('assets/checkers.png'))

def get_position_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    running = True
    clock = pygame.time.Clock()
    game = Game(SCREEN)

    while running:
        clock.tick(FPS)

        if game.turn == RED:
            value, new_board = minimax(game.get_board(), 4, RED, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            running = False

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()