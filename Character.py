import pygame.sprite

from GlobalSettings import COLORS, TILE_SIZE


class Sprite(pygame.sprite.Sprite, pygame.sprite.Group):
    def __init__(self, sprite_position_x, sprite_position_y):
        super().__init__()
        self.sprite_position_x = sprite_position_x
        self.sprite_position_y = sprite_position_y

        self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill(COLORS["WHITE"])

        self.rect = self.image.get_rect()
        self.rect.topleft = (sprite_position_x, sprite_position_y)


class Character:
    def __init__(self, character_position_x, character_position_y, sprite):
        self.character_position_x = character_position_x
        self.character_position_y = character_position_y
        self.sprite = sprite

    def update_character_sprite_after_move(self):
        # print("character: " + str(self.character_position))
        # print("sprite: " + str(self.sprite.sprite_position))
        self.sprite.rect.topleft = (self.sprite.sprite_position_x, self.sprite.sprite_position_y)
        self.sprite.rect.update(self.sprite)
