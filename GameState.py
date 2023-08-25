from enum import Enum, auto


class GameState(Enum):
    GAME = auto()
    MAIN_MENU = auto()
    QUIT = auto()