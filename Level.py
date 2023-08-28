import pygame.sprite

from Map import Map
from Character import Character


class Level:

    def __init__(self, background, sprite_group: pygame.sprite.Group, character_position):
        self.main_character = Character(64, 64, character_position)
        sprite_group.add(self.main_character)
        self.map = Map(background, sprite_group, (1600, 900))

    def update_level(self):
        self.map.update_map()
        self.main_character.update_character_after_move()
        self.map.blit_map()
