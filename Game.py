import pygame

from GameState import GameState
from GlobalSettings import TEST_BG_PATH
from Level import Level
from Menus.MainMenu import MainMenu
from CustomExceptions.GamestateError import UnknownGamestateError


class Game:

    def __init__(self):
        self.gamestate: GameState = GameState.MAIN_MENU
        self.level = Level(TEST_BG_PATH)

    def process_gamestate(self):

        match self.gamestate:
            case self.gamestate.QUIT:
                pygame.quit()
                raise SystemExit

            case self.gamestate.MAIN_MENU:
                main_menu = MainMenu(pygame.display.get_surface(), self)
                main_menu.handle_main_menu()

            case self.gamestate.GAME:
                self.gamestate = GameState.LEVEL

            case self.gamestate.LEVEL:
                self.level.update_level()

            case other:
                raise UnknownGamestateError(self.gamestate)
