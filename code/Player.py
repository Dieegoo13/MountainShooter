# no arquivo Player.py
# ...
import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_LEFT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY, ENTITY_HEALTH
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, img_name: str, position: tuple, player_id: str):
        super().__init__(img_name, position)
        self.img_name = img_name
        self.player_id = player_id
        self.speed = ENTITY_SPEED[player_id]
        self.is_shooting = False
        self.shot_delay = ENTITY_SHOT_DELAY[self.player_id]
        self.health = ENTITY_HEALTH[self.player_id]
        self.score = 0

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

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.player_id]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.player_id]]:
                return PlayerShot(
                    img_name=f'{self.player_id}Shot.png',
                    position=(self.rect.centerx, self.rect.centery),
                    player_id=self.player_id
                )
