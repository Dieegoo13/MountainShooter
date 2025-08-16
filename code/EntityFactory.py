#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'bgg':
                return Background('bgg.jpg', (0, 0))
            case 'Player1':
                return Player('Player1.png', (10, WIN_HEIGHT / 2 - 40), "Player1")
            case 'Player2':
                return Player('Player2.png', (10, WIN_HEIGHT / 2 + 40), "Player2")
            case 'Enemy1':
                return Enemy('Enemy1.png', (WIN_WIDTH + 10, random.randint(30, WIN_HEIGHT - 30)), "Enemy1")
            case 'Enemy2':
                return Enemy('Enemy2.png', (WIN_WIDTH + 10, random.randint(30, WIN_HEIGHT - 30)), "Enemy2")
            case _:
                return None