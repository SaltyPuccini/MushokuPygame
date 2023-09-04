import pygame

from EventsHandler import EventsHandler
from Game import Game
from GlobalSettings import WINDOW_HEIGHT, WINDOW_WIDTH

pygame.init()
pygame.event.set_blocked((pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN))
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
game = Game()
events_handler = EventsHandler(game)
while True:

    # Do logical updates here.
    game.process_gamestate()
    events_handler.handle_events()

    # Render the graphics here.

    pygame.display.update()  # Refresh on-screen display
    clock.tick(30)  # wait until next frame (at 60 FPS)
