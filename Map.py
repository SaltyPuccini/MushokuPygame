import pygame


class Map:

    def __init__(self, background, sprite_group, map_size: tuple[int, int]):
        self.background = background
        self.sprite_group = sprite_group
        self.surface = pygame.Surface(map_size)

    def update_map(self):
        self.surface.blit(pygame.image.load(self.background), (0, 0))
        self.sprite_group.draw(self.surface)

    def blit_map(self):
        pygame.display.get_surface().blit(self.surface, (0, 0))
