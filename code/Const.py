import pygame

#C
COLOR_BLUE= (5, 60, 156)
COLOR_WHITE = (255, 255, 255)
COLOR_PINK = (252, 20, 216)

#E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Player1': 3,
    # 'Player1Shot': 1,
    'Player2': 3,
    # 'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
# PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
#                     'Player2': pygame.K_LCTRL}

#S
SPAWN_TIME = 3000


#W
WIN_WIDTH = 576

WIN_HEIGHT = 324