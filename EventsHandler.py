import pygame
from pygame.event import Event

from Game import Game
from GameState import GameState


class EventsHandler:

    def __init__(self, game: Game):
        self.game = game
        self.last_pressed = None

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.handle_menu_key_press_events(event)
                self.last_pressed = event.key
            if event.type == pygame.KEYUP:
                self.last_pressed = None

        if not self.game.level.map.is_animation_ongoing and self.last_pressed is not None:
            self.handle_main_character_movement()

    def handle_menu_key_press_events(self, event):
        if event.key == pygame.K_ESCAPE:
            self.game.gamestate = GameState.MAIN_MENU
        if event.key == pygame.K_q:
            self.game.gamestate = GameState.QUIT

    def handle_main_character_movement(self):
        animation_path = "Resources/Animation/"
        drawn_map = self.game.level.map
        key = self.last_pressed

        if key == pygame.K_DOWN:
            animation_path += "WalkDown"
            drawn_map.animation_path = animation_path
            drawn_map.is_animation_ongoing = True

        if key == pygame.K_UP:
            animation_path += "WalkUp"
            drawn_map.animation_path = animation_path
            drawn_map.is_animation_ongoing = True

        if key == pygame.K_RIGHT:
            animation_path += "WalkRight"
            drawn_map.animation_path = animation_path
            drawn_map.is_animation_ongoing = True

        if key == pygame.K_LEFT:
            animation_path += "WalkLeft"
            drawn_map.animation_path = animation_path
            drawn_map.is_animation_ongoing = True
