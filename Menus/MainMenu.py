from typing import List

import pygame_menu

from GameState import GameState
from GlobalSettings import WINDOW_WIDTH, WINDOW_HEIGHT
from Menus.SettingsMenu import SettingsMenu
from Menus.AboutSection import AboutSection

class MainMenu:
    def __init__(self, screen, game):
        self.main_entries: List[str] = ["New Game", "Settings", "About", "Quit"]
        self.screen = screen
        self.game = game
        self.menu = pygame_menu.Menu('Main Menu', WINDOW_HEIGHT, WINDOW_WIDTH)
        self.menu.enable()

    def handle_main_menu(self):
        self.menu.add.button(self.main_entries[0], self.start_new_game)
        self.menu.add.button(self.main_entries[1], SettingsMenu().return_settings_menu())
        self.menu.add.button(self.main_entries[2], AboutSection().return_about_section())
        self.menu.add.button(self.main_entries[3], pygame_menu.events.EXIT)
        if self.menu.is_enabled():
            self.menu.mainloop(self.screen)

    def start_new_game(self):
        self.menu.disable()
        self.game.gamestate = GameState.GAME
