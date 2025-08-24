import os, sys, pygame
from abc import ABC, abstractmethod

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # Quando rodar pelo .exe (cx_Freeze)
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(base_path, "..")  # pq sua pasta asset tá fora de code/
    return os.path.join(base_path, relative_path)


class Entity(ABC):
    def __init__(self, img_name: str, position: tuple):
        self.name = img_name

        img_path = resource_path(os.path.join("asset", img_name))
        self.surf = pygame.image.load(img_path)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH.get(self.name, None)
        self.damage = ENTITY_DAMAGE.get(self.name, 0)
        self.score = ENTITY_SCORE.get(self.name)
        self.last_dmg = "None"

    @abstractmethod
    def move(self):
        pass
