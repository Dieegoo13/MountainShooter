# !/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, img_name: str, position: tuple, enemy_id: str):
        super().__init__(img_name, position)
        self.name = enemy_id

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        pass
