import pygame.sprite

from Entity import Entity
from GlobalSettings import WIDTH_CENTER, HEIGHT_CENTER
from Map import Map
from Character import Character, Sprite


class Level:

    def __init__(self, background):
        self.sprite_group = pygame.sprite.Group()
        self.main_hero_group = pygame.sprite.Group()

        self.main_character = Character(WIDTH_CENTER, HEIGHT_CENTER, Sprite(WIDTH_CENTER, HEIGHT_CENTER))
        self.entities = []
        self.entities.append(Entity(128, 128))

        self.main_hero_group.add(self.main_character.sprite)
        for entity in self.entities:
            self.sprite_group.add(entity.sprite)

        self.map = Map(background, self.sprite_group, self.main_hero_group, (1600, 900))

    def update_all_entities_position(self):
        for entity in self.entities:
            entity.update_entity_sprite_after_move(
                WIDTH_CENTER - self.main_character.character_position_x,
                HEIGHT_CENTER - self.main_character.character_position_y)

    def update_level(self):
        self.map.update_map(self.main_character)
        self.main_character.update_character_sprite_after_move()
        self.update_all_entities_position()
        self.map.blit_map()
