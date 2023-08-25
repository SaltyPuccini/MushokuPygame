import pygame_menu

from GlobalSettings import WINDOW_HEIGHT, WINDOW_WIDTH

settings_difficulties =[('Beginner', 1),
                       ('Intermediate', 2),
                       ('Advanced', 3),
                       ('Saint', 4),
                       ('King', 5),
                       ('Emperor', 6),
                       ('God', 7)]


class SettingsMenu():
    def __init__(self):
        self.settings = pygame_menu.Menu('Settings', WINDOW_HEIGHT, WINDOW_WIDTH)
        self.settings.add.selector('Difficulty :', settings_difficulties)
        self.settings.add.button('Back', pygame_menu.events.BACK)

    def return_settings_menu(self):
        return self.settings
