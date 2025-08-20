from code.Const import ENTITY_SPEED
from code.Entity import Entity
from code.Const import ENTITY_SHOT_DELAY

class EnemyShot(Entity):
    def __init__(self, img_name: str, position: tuple, enemy_id: str):
        super().__init__(img_name, position)
        self.enemy_id = enemy_id

    def move(self):
        self.rect.x -= ENTITY_SPEED[f'{self.enemy_id}Shot']
