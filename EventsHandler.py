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
            if event.type == pygame.KEYDOWN and not self.game.level.map.is_animation_ongoing:
                self.handle_menu_key_press_events(event)
                self.handle_main_character_movement(event)

    def handle_menu_key_press_events(self, event: Event):
        if event.key == pygame.K_ESCAPE:
            self.game.gamestate = GameState.MAIN_MENU
            print(self.game.gamestate)
        if event.key == pygame.K_q:
            self.game.gamestate = GameState.QUIT

    def handle_main_character_movement(self, event: Event):
        animation_path = "Resources/Animation/"
        drawn_map = self.game.level.map
        if event.key == pygame.K_DOWN:
            animation_path += "WalkDown"
            drawn_map.animation_path = animation_path
            drawn_map.is_animation_ongoing = True

        if event.key == pygame.K_UP:
            animation_path += "WalkUp"
            drawn_map.animation_path = animation_path
            drawn_map.is_animation_ongoing = True

        if event.key == pygame.K_RIGHT:
            animation_path += "WalkRight"
            drawn_map.animation_path = animation_path
            drawn_map.is_animation_ongoing = True

        if event.key == pygame.K_LEFT:
            animation_path += "WalkLeft"
            drawn_map.animation_path = animation_path
            drawn_map.is_animation_ongoing = True
