import pygame_menu

from GlobalSettings import WINDOW_HEIGHT, WINDOW_WIDTH

about_text = 'Fanmade Mushoku Tensei game in Pokemon Mystery Dungeon style, following the story of Rudeus, Eris and Ruijerd wander through the Demon Continent. Made by Kajetan \"Salty Puccini\" Wojciechowski'


class AboutSection():
    def __init__(self):
        self.about = pygame_menu.Menu('About', WINDOW_HEIGHT, WINDOW_WIDTH)
        self.about.add.label(about_text, max_char=-1, font_size=20)
        self.about.add.button('Back', pygame_menu.events.BACK)

    def return_about_section(self):
        return self.about
