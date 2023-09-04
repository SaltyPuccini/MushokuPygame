import pygame.sprite

from GlobalSettings import COLORS, TILE_SIZE


class Sprite(pygame.sprite.Sprite, pygame.sprite.Group):
    def __init__(self, sprite_position_x, sprite_position_y, sprite_color=COLORS["WHITE"], sprite_image=None):
        super().__init__()

        self.sprite_position_x = sprite_position_x
        self.sprite_position_y = sprite_position_y

        if sprite_image is None:
            self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
            self.image.fill(sprite_color)
        else:
            self.image = pygame.image.load(sprite_image)

        self.rect = self.image.get_rect()
        self.rect.topleft = (sprite_position_x, sprite_position_y)

    def change_sprite_image(self, directory, file_name):
        self.image = pygame.image.load(directory+"/"+str(file_name)+".png")


class Character:
    def __init__(self, character_position_x, character_position_y, sprite):
        self.character_position_x = character_position_x
        self.character_position_y = character_position_y
        self.sprite = sprite

    def update_character_sprite_after_move(self, surface: pygame.Surface):
        self.sprite.rect.topleft = (self.sprite.sprite_position_x, self.sprite.sprite_position_y)
        surface.blit(self.sprite.image, self.sprite.rect)

