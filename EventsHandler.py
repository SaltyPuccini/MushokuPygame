import pygame
from pygame.event import Event

from Game import Game
from GameState import GameState


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
        main_character_position = self.game.level.main_character.position
        if event.key == pygame.K_DOWN:
            main_character_position[1] += 64
        if event.key == pygame.K_UP:
            main_character_position[1] -= 64
        if event.key == pygame.K_RIGHT:
            main_character_position[0] += 64
        if event.key == pygame.K_LEFT:
            main_character_position[0] -= 64
