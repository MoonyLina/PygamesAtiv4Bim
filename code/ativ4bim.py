import pygame as pg
from sys import exit

pg.init()
w, h = 1200, 1000
screen = pg.display.set_mode((w,h))
pg.display.set_caption("Nacbar's Chamber")
clock = pg.time.Clock()
font = pg.font.Font(r"fonts\Pixeltype.ttf", 50)

game_active = True
player_fall_animation = False   # novo
fall_gravity = 1                # novo

background = pg.image.load(r"images\fundo.jpeg")
background_sfc = pg.transform.scale(background, (w, h))

denis_move = pg.image.load(r"images\D1.png")
denis_stand = pg.image.load(r"images\Dparado.png")
largura_D, altura_D = denis_stand.get_size()
nova_larguraD = largura_D // 1.5
nova_alturaD = altura_D // 1.5
denis_rect = denis_stand.get_rect(topleft = (900, 610))
denis_move_sfc = pg.transform.scale(denis_move, (nova_larguraD, nova_alturaD)) 
denis_stand_sfc = pg.transform.scale(denis_stand, (nova_larguraD, nova_alturaD))

regua = pg.image.load(r"images\regua.png")
regua_largura, regua_altura = regua.get_size()
nova_larguraR = regua_largura // 1.3
nova_alturaR = regua_altura // 1.3
regua_sfc = pg.transform.scale(regua, (nova_larguraR, nova_alturaR))
regua_sfc = pg.transform.rotate(regua_sfc, 90)
regua_rect = regua_sfc.get_rect(topleft=(denis_rect.left, denis_rect.centery - 25))

player_walking = pg.image.load(r"images\jandando.png")
player_stand = pg.image.load(r"images\jparada.png")

largura_playerW, altura_playerW = player_walking.get_size()
nova_larguraW = largura_playerW // 2
nova_alturaW = altura_playerW // 2

largura_playerS, altura_playerS = player_stand.get_size()
nova_larguraS = largura_playerS // 2
nova_alturaS = altura_playerS // 2

player_walking_right_sfc = pg.transform.scale(player_walking, (nova_larguraW, nova_alturaW))
player_walking_left_sfc = pg.transform.flip(player_walking_right_sfc, True, False)
playerW_rect = player_walking_right_sfc.get_rect(topleft=(200, 600))

player_stand_right_sfc = pg.transform.scale(player_stand, (nova_larguraS, nova_alturaS))
player_stand_left_sfc = pg.transform.flip(player_stand_right_sfc, True, False)
playerS_rect = player_stand_right_sfc.get_rect(topleft=(200, 600))

text_sfc = font.render("Text", False, "Black")

# animação
player_walk_right = [player_walking_right_sfc, player_stand_right_sfc]
player_walk_left = [player_walking_left_sfc, player_stand_left_sfc]

denis_attack = False
denis_anim = 0
anim_duration = 50

frame = 0
vel_anim = 0.10
direction = "R"

vel = 5
regua_vel = -7

vidas = 3

grav = 1
pulo = -23
vel_y = 0
no_chao = True
chao_y = 600

initial_time = pg.time.get_ticks()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    key = pg.key.get_pressed()

    act_time = pg.time.get_ticks()
    sec_time = (act_time - initial_time) // 1000

    
    if player_fall_animation:
        vel_y += fall_gravity
        playerS_rect.y += vel_y

        if playerS_rect.top > h:
            game_active = False

    else:
        if key[pg.K_SPACE] and no_chao:
            vel_y = pulo
            no_chao = False
        
        vel_y += grav
        playerS_rect.y += vel_y

        if playerS_rect.y >= chao_y:
            playerS_rect.y = chao_y
            vel_y = 0
            no_chao = True

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
        
        # Denis atacando
        if denis_attack:
            current_denis_sfc = denis_move_sfc 
            denis_anim -= 1
            if denis_anim <= 0:
                denis_attack = False
        else: 
            current_denis_sfc = denis_stand_sfc
        
        regua_rect.x += regua_vel
        
        if regua_rect.right < 0:
            regua_rect.midleft = (denis_rect.left, denis_rect.centery - 25)
            denis_attack = True
            denis_anim = anim_duration

        if playerS_rect.colliderect(regua_rect):
            vidas -= 1
            regua_rect.midleft = (denis_rect.left, denis_rect.centery - 25)
            print(f"Vidas: {vidas}")

        if vidas <= 0 and not player_fall_animation:
            player_fall_animation = True
            vel_y = -15 
            no_chao = False 
    
    if game_active:
        screen.blit(background_sfc, (0, 0))
        screen.blit(text_sfc, (600, 100))
        screen.blit(regua_sfc, regua_rect)
        screen.blit(current_denis_sfc, denis_rect)
        screen.blit(current_player_sfc, playerS_rect)

        vidas_text = font.render(f"Vidas: {vidas}", False, "Black")
        screen.blit(vidas_text, (50, 50))

        time_text = font.render(f"Tempo: {sec_time}s", False, "Black")
        screen.blit(time_text, (900, 50))

    else:
        # mudança de tela final
        background_over = pg.image.load(r"images\if.jpeg")
        background_over_sfc = pg.transform.scale(background_over, (w, h))
        screen.blit(background_over_sfc, (0, 0))
        denis_over = pg.image.load(r"images\deninho.png")
        largura_DO, altura_DO = denis_over.get_size() 
        nova_larguraDO = largura_DO // 2.5
        nova_alturaDO = altura_DO // 2.5
        denis_over_sfc = pg.transform.scale(denis_over, (nova_larguraDO, nova_alturaDO))
        denis_over_rect = denis_over_sfc.get_rect(topleft = (445, 360))
        screen.blit(denis_over_sfc, denis_over_rect)
        gameover_text = font.render("Game Over", True, "White")
        restart_text = font.render("Pressione R para reiniciar", True, "White")
        screen.blit(restart_text, (435, 300))
        screen.blit(gameover_text, (540, 200))
    
        keys = pg.key.get_pressed()
        if keys[pg.K_r]:
            # reiniciar a chamber
            game_active = True
            player_fall_animation = False
            vel_y = 0
            no_chao = True
            playerS_rect.topleft = (200, 600)
            vidas = 3
            regua_rect.midleft = (denis_rect.left, denis_rect.centery - 25)
            initial_time = pg.time.get_ticks()
    pg.display.update()
    clock.tick(60)