# !/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, img_name: str, position: tuple, enemy_id: str):
        super().__init__(img_name, position)
        self.name = enemy_id
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

            shot_position = (self.rect.left - 15, self.rect.centery)

            return EnemyShot(f'{self.name}Shot.png', shot_position, self.name)
        return None

