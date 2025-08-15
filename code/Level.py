#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode, player_score):
        #self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.player_score = player_score
        self.background = EntityFactory.get_entity('bgg')

    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            self.window.blit(self.background.surf, self.background.rect)
            pygame.display.flip()
