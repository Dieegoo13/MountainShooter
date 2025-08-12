import pygame as  pg

print('Iniciou o jogo')
pg.init()
screen = pg.display.set_mode((800, 600))
windows = pg.display.set_mode(size=(600, 400))
print('Encerrou o jogo')

while True:
    #Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT: #Close Window
            pg.quit() #end pygame
