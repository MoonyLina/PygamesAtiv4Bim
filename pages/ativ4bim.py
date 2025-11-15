import pygame as pg
from sys import exit

pg.init()
w, h = 1200, 1000
screen = pg.display.set_mode((w,h))
pg.display.set_caption("Jogo")
clock = pg.time.Clock()
font = pg.font.Font("", 50)


background = pg.image.load(r"C:\Users\anaca\Desktop\IFSP\Linguagem Técnica\Ativ4BimPygames\images\fundo.jpeg")
background = pg.transform.scale(background, (w, h))
player_walking = pg.image.load(r"C:\Users\anaca\Desktop\IFSP\Linguagem Técnica\Ativ4BimPygames\images\jandando.png")
player_stand = pg.image.load(r"C:\Users\anaca\Desktop\IFSP\Linguagem Técnica\Ativ4BimPygames\images\jparada.png")
text = font.render("Text", False, "Black")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
            
    screen.blit(background, (0,0))
    screen.blit(text, (600, 100))

    pg.display.update()
    clock.tick(60)