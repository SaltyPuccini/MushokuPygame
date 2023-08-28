import pygame.sprite

from GlobalSettings import COLORS


class Character(pygame.sprite.Sprite, pygame.sprite.Group):
    def __init__(self, width: int, height: int, position):
        super().__init__()
        self.position = position
        self.image = pygame.Surface([width, height])
        self.image.fill(COLORS["WHITE"])
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update_character_after_move(self):
        self.rect.topleft = self.position
        self.rect.update(self)
