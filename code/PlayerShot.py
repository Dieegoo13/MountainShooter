from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, img_name: str, position: tuple, player_id: str):
        super().__init__(img_name, position)
        self.player_id = player_id


    def move(self):
        self.rect.x += ENTITY_SPEED[self.player_id]