from typing import List

import pygame_menu
import webbrowser

from GameState import GameState
from GlobalSettings import WINDOW_WIDTH, WINDOW_HEIGHT, MAIN_MENU_THEME
from Menus.SettingsMenu import SettingsMenu


def about_section():
    webbrowser.open("https://github.com/SaltyPuccini/MushokuPygame/blob/master/README.md")


class MainMenu:
    def __init__(self, screen, game):
        self.main_entries: List[str] = ["New Game", "Settings", "About", "Quit"]
        self.screen = screen
        self.game = game
        self.main_menu = pygame_menu.Menu('', WINDOW_WIDTH, WINDOW_HEIGHT, theme=MAIN_MENU_THEME)
        self.main_menu.enable()

    def handle_main_menu(self):
        self.main_menu.add.button(self.main_entries[0], self.start_new_game)
        self.main_menu.add.button(self.main_entries[1], SettingsMenu().return_settings_menu())
        self.main_menu.add.button(self.main_entries[2], about_section)
        self.main_menu.add.button(self.main_entries[3], pygame_menu.events.EXIT)
        if self.main_menu.is_enabled():
            self.main_menu.mainloop(self.screen)

    def start_new_game(self):
        self.main_menu.disable()
        self.game.gamestate = GameState.GAME
