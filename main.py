import pygame
from Game import Game
from GameState import GameState
from GlobalSettings import WINDOW_HEIGHT, WINDOW_WIDTH

pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()
game = Game(screen)
while True:

    # Do logical updates here.
    game.process_gamestate()
    screen.fill("black")

    # Render the graphics here.

    pygame.display.update()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)
