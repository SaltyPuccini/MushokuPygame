import pygame
from pygame.event import Event

from Game import Game
from GameState import GameState
from GlobalSettings import TILE_SIZE


class EventsHandler:

    def __init__(self, game: Game):
        self.game = game

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.handle_menu_key_press_events(event)
                self.handle_main_character_movement(event)

    def handle_menu_key_press_events(self, event: Event):
        if event.key == pygame.K_ESCAPE:
            self.game.gamestate = GameState.MAIN_MENU
            print(self.game.gamestate)
        if event.key == pygame.K_q:
            self.game.gamestate = GameState.QUIT

    def handle_main_character_movement(self, event: Event):
        main_character = self.game.level.main_character
        if event.key == pygame.K_DOWN:
            main_character.character_position_y += TILE_SIZE
        if event.key == pygame.K_UP:
            main_character.character_position_y -= TILE_SIZE
        if event.key == pygame.K_RIGHT:
            main_character.character_position_x += TILE_SIZE
        if event.key == pygame.K_LEFT:
            main_character.character_position_x -= TILE_SIZE
