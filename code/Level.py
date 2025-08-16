#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random

import pygame
from pygame import Surface, Rect

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.EntityFactory import EntityFactory
from pygame.font import Font

#LEVEL

class Level:
    def __init__(self, window, name, game_mode, player_score):
        self.timeout = 2000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.player_score = player_score
        self.background = EntityFactory.get_entity('bgg')
        self.entity_list = []
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)



    def run(self):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.window.blit(self.background.surf, self.background.rect)

            for entity in self.entity_list:
                entity.move()
                self.window.blit(entity.surf, entity.rect)

            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(20, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            pygame.display.flip()
            # Collisions

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)