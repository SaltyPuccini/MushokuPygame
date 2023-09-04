import pygame.sprite

from Entity import Entity
from GlobalSettings import WIDTH_CENTER, HEIGHT_CENTER, COLORS, TEST_CHARACTER_PATH, TEST_NPC_SPRITE_PATH, TILE_SIZE
from Map import Map
from Character import Character, Sprite


class Level:

    def __init__(self, background):
        self.entities = []

        self.sprite_group = pygame.sprite.Group()
        self.main_hero_group = pygame.sprite.Group()

        self.main_character = Character(640, 640, Sprite(WIDTH_CENTER, HEIGHT_CENTER, sprite_image=TEST_CHARACTER_PATH))

        self.entities.append(Entity(18 * TILE_SIZE, 18 * TILE_SIZE,
                                    Sprite(WIDTH_CENTER, HEIGHT_CENTER, sprite_image=TEST_NPC_SPRITE_PATH)))
        self.entities.append(Entity(29 * TILE_SIZE, 10 * TILE_SIZE,
                                    Sprite(WIDTH_CENTER, HEIGHT_CENTER, sprite_image=TEST_NPC_SPRITE_PATH)))

        self.main_hero_group.add(self.main_character.sprite)
        for entity in self.entities:
            self.sprite_group.add(entity.sprite)

        self.map = Map(background, self.sprite_group, self.main_hero_group, (1600, 900))

    def update_level(self):
        self.map.update_map(self.main_character, self.entities)
