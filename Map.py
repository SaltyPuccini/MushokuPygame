import pygame

from Character import Character
from GlobalSettings import WIDTH_CENTER, HEIGHT_CENTER, TILE_SIZE


class Map:

    def __init__(self, background, sprite_group, main_hero_group, map_size):
        self.is_animation_ongoing = False
        self.animation_path = ""
        self.animation_counter = 1
        self.background = background
        self.main_hero_group = main_hero_group
        self.sprite_group = sprite_group
        self.surface = pygame.Surface(map_size)
        self.distance_covered = 0

    def update_map(self, main_character: Character, entities: []):

        if self.is_animation_ongoing:
            if self.animation_counter <= 8:
                match self.animation_path.split('/')[-1]:
                    case "WalkDown":
                        main_character.character_position_y += TILE_SIZE / 8
                        self.distance_covered += TILE_SIZE / 8
                        main_character.sprite.change_sprite_image(self.animation_path, self.animation_counter)
                        self.animation_counter += 1
                    case "WalkUp":
                        main_character.character_position_y -= TILE_SIZE / 8
                        self.distance_covered += TILE_SIZE / 8
                        main_character.sprite.change_sprite_image(self.animation_path, self.animation_counter)
                        self.animation_counter += 1
                    case "WalkRight":
                        main_character.character_position_x += TILE_SIZE / 8
                        self.distance_covered += TILE_SIZE / 8
                        main_character.sprite.change_sprite_image(self.animation_path, self.animation_counter)
                        self.animation_counter += 1
                    case "WalkLeft":
                        main_character.character_position_x -= TILE_SIZE / 8
                        self.distance_covered += TILE_SIZE / 8
                        main_character.sprite.change_sprite_image(self.animation_path, self.animation_counter)
                        self.animation_counter += 1
                    case other:
                        pass
            else:
                self.animation_counter = 1
                if self.distance_covered == TILE_SIZE:
                    self.distance_covered = 0
                    self.is_animation_ongoing = False

        main_character.update_character_sprite_after_move(self.surface)

        blit_cord_x = WIDTH_CENTER - main_character.character_position_x
        blit_cord_y = HEIGHT_CENTER - main_character.character_position_y

        if -768 < blit_cord_x < 0 and -320 < blit_cord_y < 0:

            for entity in entities:
                entity.update_entity_sprite_after_move(
                    blit_cord_x,
                    blit_cord_y)

        else:
            if blit_cord_x >= 0:
                blit_cord_x = 0
                main_character.sprite.sprite_position_x = main_character.character_position_x

            elif blit_cord_x <= -768:
                blit_cord_x = -768
                main_character.sprite.sprite_position_x = main_character.character_position_x - 768

            if blit_cord_y >= 0:
                blit_cord_y = 0
                main_character.sprite.sprite_position_y = main_character.character_position_y

            elif blit_cord_y <= -320:
                blit_cord_y = -320
                main_character.sprite.sprite_position_y = main_character.character_position_y - 320

            for entity in entities:
                entity.update_entity_sprite_after_move(
                    blit_cord_x,
                    blit_cord_y)

        self.surface.blit(pygame.image.load(self.background), (blit_cord_x, blit_cord_y))

        self.sprite_group.draw(self.surface)
        self.main_hero_group.draw(self.surface)

        pygame.display.get_surface().blit(self.surface, (0, 0))
