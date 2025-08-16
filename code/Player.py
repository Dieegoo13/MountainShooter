# no arquivo Player.py
# ...
import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_LEFT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, img_name: str, position: tuple, player_id: str):
        super().__init__(img_name, position)
        self.img_name = img_name  # agora guardamos o nome da imagem
        self.player_id = player_id  # "Player1" ou "Player2"
        self.speed = ENTITY_SPEED[player_id]
        self.lives = 3
        self.is_shooting = False

    def move(self):
        pressed_key = pygame.key.get_pressed()

        # UP
        if pressed_key[PLAYER_KEY_UP[self.player_id]] and self.rect.top > 0:
            self.rect.y -= self.speed

        # DOWN
        if pressed_key[PLAYER_KEY_DOWN[self.player_id]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed

        # LEFT
        if pressed_key[PLAYER_KEY_LEFT[self.player_id]] and self.rect.left > 0:
            self.rect.x -= self.speed

        # RIGHT
        if pressed_key[PLAYER_KEY_RIGHT[self.player_id]] and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed
