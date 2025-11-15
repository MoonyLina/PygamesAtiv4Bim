import pygame as pg
from sys import exit

pg.init()
w, h = 1200, 1000
screen = pg.display.set_mode((w,h))
pg.display.set_caption("Nacbar's Chamber")
clock = pg.time.Clock()
font = pg.font.Font(None, 50)



background = pg.image.load(r"C:\Users\anaca\Desktop\IFSP\Linguagem Técnica\Ativ4BimPygames\images\fundo.jpeg")
background_sfc = pg.transform.scale(background, (w, h))

player_walking = pg.image.load(r"C:\Users\anaca\Desktop\IFSP\Linguagem Técnica\Ativ4BimPygames\images\jandando.png")
player_stand = pg.image.load(r"C:\Users\anaca\Desktop\IFSP\Linguagem Técnica\Ativ4BimPygames\images\jparada.png")

largura_playerW, altura_playerW = player_walking.get_size()
nova_larguraW = largura_playerW // 2
nova_alturaW = altura_playerW // 2

largura_playerS, altura_playerS = player_stand.get_size()
nova_larguraS = largura_playerS // 2
nova_alturaS = altura_playerS // 2

player_walking_right_sfc = pg.transform.scale(player_walking, (nova_larguraW, nova_alturaW))
player_walking_left_sfc = pg.transform.flip(player_walking_right_sfc, True, False)
playerW_rect = player_walking_right_sfc.get_rect(topleft = (200, 600))

player_stand_right_sfc = pg.transform.scale(player_stand,(nova_larguraS, nova_alturaS))
player_stand_left_sfc = pg.transform.flip(player_stand_right_sfc, True, False)
playerS_rect = player_stand_right_sfc.get_rect(topleft = (200, 600))

text_sfc = font.render("Text", False, "Black")

# animação
player_walk_right = [player_walking_right_sfc, player_stand_right_sfc]
player_walk_left = [player_walking_left_sfc, player_stand_left_sfc]


frame = 0
vel_anim = 0.10
direction = "R"

vel = 5


vidas = 3
gravidade = 1
pulo = -20



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    key = pg.key.get_pressed()

    if key[pg.K_RIGHT]:
        direction = "R"
        playerS_rect.x += vel
        frame += vel_anim
        if frame >= len(player_walk_right):
            frame = 0
        current_player_sfc = player_walk_right[int(frame)]
    elif key[pg.K_LEFT]:
        direction = "L"
        playerS_rect.x -= vel
        frame += vel_anim
        if frame >= len(player_walk_left):
            frame = 0
        current_player_sfc = player_walk_left[int(frame)]
    else:
        frame = 0
        if direction == "R":
            current_player_sfc = player_stand_right_sfc
        else:
            current_player_sfc = player_stand_left_sfc
    
    
    
    screen.blit(background_sfc, (0,0))
    screen.blit(text_sfc, (600, 100))
    screen.blit(current_player_sfc, playerS_rect)
    
    pg.display.update()
    clock.tick(60)