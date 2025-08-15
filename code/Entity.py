import os
import pygame
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        base_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(base_path, "..", "asset", name + ".jpg")
        self.surf = pygame.image.load(img_path)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
