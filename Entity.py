class Entity:
    def __init__(self, entity_position_x, entity_position_y, sprite):
        self.entity_position_x = entity_position_x
        self.entity_position_y = entity_position_y
        self.sprite = sprite

    def update_entity_sprite_after_move(self, offset_x, offset_y):
        self.sprite.sprite_position_x = self.entity_position_x + offset_x
        self.sprite.sprite_position_y = self.entity_position_y + offset_y

        self.sprite.rect.topleft = (self.sprite.sprite_position_x, self.sprite.sprite_position_y)
        self.sprite.rect.update(self.sprite)
