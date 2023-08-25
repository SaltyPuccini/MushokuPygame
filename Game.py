import pygame

from GameState import GameState
from MainMenu import MainMenu
from CustomExceptions.GamestateError import UnknownGamestateError


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.gamestate: GameState = GameState.MAIN_MENU

    def process_gamestate(self):

        match self.gamestate:
            case self.gamestate.QUIT:
                pygame.quit()
                raise SystemExit
            case self.gamestate.MAIN_MENU:
                main_menu = MainMenu(self.screen, self)
                main_menu.handle_main_menu()
            case self.gamestate.GAME:
                pass
            case other:
                raise UnknownGamestateError(self.gamestate)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gamestate = GameState.MAIN_MENU
