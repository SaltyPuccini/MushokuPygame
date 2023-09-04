import pygame

from Character import Character
from GlobalSettings import WIDTH_CENTER, HEIGHT_CENTER


class Map:

    def __init__(self, background, sprite_group, main_hero_group, map_size):
        self.background = background
        self.main_hero_group = main_hero_group
        self.sprite_group = sprite_group
        self.surface = pygame.Surface(map_size)

    def update_map(self, main_character: Character):
        self.surface.blit(pygame.image.load(self.background), (
            WIDTH_CENTER - main_character.character_position_x,
            HEIGHT_CENTER - main_character.character_position_y))

        self.sprite_group.draw(self.surface)
        self.main_hero_group.draw(self.surface)

    def blit_map(self):
        pygame.display.get_surface().blit(self.surface, (0, 0))
