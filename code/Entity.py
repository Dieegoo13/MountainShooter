import os
import pygame
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, img_name: str, position: tuple):
        self.name = img_name
        base_path = os.path.dirname(os.path.abspath(__file__))

        img_path = os.path.join(base_path, "..", "asset", img_name)
        self.surf = pygame.image.load(img_path)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass