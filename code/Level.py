#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random

import pygame
from pygame import Surface, Rect

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_BLUE, COLOR_GREEN
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.Player import Player


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

            for entity in list(self.entity_list):
                entity.move()

                if isinstance(entity, (Player, Enemy)):
                    shot = entity.shoot()
                    if shot:
                        self.entity_list.append(shot)

                self.window.blit(entity.surf, entity.rect)

                if entity.name == 'Player1.png':
                    self.level_text(20, f'Player1 - Health: {entity.health} ', COLOR_GREEN, (10, 10))
                if entity.name == 'Player2.png':
                    self.level_text(20, f'Player2 - Health: {entity.health}', COLOR_BLUE, (10, 40))
                # if entity.name == 'Player1.png':
                #     self.level_text(20, f'Player1 - Health: {entity.health} | Score: {entity.score}', COLOR_GREEN, (10, 10))
                # if entity.name == 'Player2.png':
                #     self.level_text(20, f'Player2 - Health: {entity.health} | Score: {entity.score}', COLOR_BLUE, (10, 40))


            #self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(20, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            pygame.display.flip()
            # Collisions

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)