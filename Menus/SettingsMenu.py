import pygame
import pygame_menu

from GlobalSettings import WINDOW_HEIGHT, WINDOW_WIDTH, MAIN_MENU_THEME

settings_difficulties = [('Beginner', 1),
                         ('Intermediate', 2),
                         ('Advanced', 3),
                         ('Saint', 4),
                         ('King', 5),
                         ('Emperor', 6),
                         ('God', 7)]

settings_fullscreen = [('No', 0),
                       ('Yes', 1)]


def handle_fullscreen(value, is_fullscreen):
    if is_fullscreen:
        pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
    else:
        pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


class SettingsMenu:
    def __init__(self):
        self.settings_menu = pygame_menu.Menu('', WINDOW_WIDTH, WINDOW_HEIGHT, theme=MAIN_MENU_THEME)
        self.settings_menu.add.selector('Difficulty :', settings_difficulties)
        self.settings_menu.add.selector('Full screen :', settings_fullscreen,
                                        onchange=handle_fullscreen,
                                        selector_id="change_fullscreen")
        self.settings_menu.add.button('Back', pygame_menu.events.BACK)

    def return_settings_menu(self):
        return self.settings_menu
