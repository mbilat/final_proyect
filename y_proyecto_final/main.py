from matplotlib import image
import pygame
import sys
from constantes import *
from player import Player
from enemigo import *
from proyectil import *
from plataforma import *
from objetos import *
from spawn import *
from ladder import *
from screen_items import *
from gui import *
from constructor import *
from objetos import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

current_level = Level()

timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

tick_1s = pygame.USEREVENT+0
pygame.time.set_timer(tick_1s,1000)

seconds,minutes = 0,0

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("y_proyecto_final/resources/passionfruit.mp3")
sonido_fondo.set_volume(0.9)

menu = InitMenu()
menu.run_(screen)
pause=PauseMenu()
flag_new_game = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == tick_1s:
            if not flag_new_game and not pause.in_pause:
                seconds+=1
                if seconds ==60:
                    minutes+=1
                    seconds=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause.in_pause = True

    keys = pygame.key.get_pressed()

    delta_ms = clock.tick(FPS)

    if pause.in_pause and menu.init_level:
        pause.run_(screen)
        
    elif menu.init_level and not pause.in_pause:

        if flag_new_game:
            current_level.init_level()
            sonido_fondo.play()
            flag_new_game = False
            last_spawn = 0
            items = Items()

        if current_level.player_1.is_alive and not current_level.player_1.is_win:

            items.draw_on_game(screen,imagen_fondo,current_level.player_1,seconds,minutes)

            last_spawn += 1

            if len(current_level.list_enemy)==0:
                Spawn.enemy(current_level.list_enemy,current_level.list_enemy_spawn,len(current_level.list_enemy_spawn),Enemy)

            if len(current_level.list_enemy)<3 and last_spawn>20:
                Spawn.enemy(current_level.list_enemy,current_level.list_enemy_spawn,len(current_level.list_enemy_spawn),Enemy)
                last_spawn=0
            
            if len(current_level.list_runner)==0 and last_spawn>15:
                Spawn.enemy(current_level.list_runner,current_level.list_runner_spawn,len(current_level.list_runner_spawn),Runner)

            for plataforma in current_level.list_platforms:
                plataforma.draw(screen)

            for ladder in current_level.ladder_list:
                ladder.draw(screen)
            
            if len(current_level.list_keys)<4:
                if current_level.time_keys <=0:
                    current_level.time_keys = 50
                    Spawn.keys(current_level.list_keys,current_level.list_keys_spawn,len(current_level.list_keys_spawn))
                current_level.time_keys -=1
            
            if current_level.player_1.keys >= 4:
                current_level.portal.on = True
                current_level.portal.draw(screen)

            current_level.player_1.events(delta_ms,keys,current_level.ladder_list)
            current_level.player_1.update(delta_ms,current_level.list_enemy,current_level.list_runner,current_level.list_platforms)
            current_level.player_1.draw(screen)

            for flags in current_level.list_keys:
                flags.is_caught(current_level.player_1)
                flags.draw(screen)

            for cantidad,fruta in enumerate(current_level.list_bonus):
                fruta.draw(screen)
                if current_level.player_1.colision(fruta.rect):
                    current_level.player_1.municion += 10
                    current_level.list_bonus.pop(cantidad)

            for indices,enemigo in enumerate(current_level.list_enemy):
                if enemigo.is_alive:
                    enemigo.shot(current_level.player_1)
                    enemigo.move()
                    enemigo.update(current_level.player_1,current_level.list_platforms)
                    enemigo.draw(screen)  
                else:
                    current_level.list_enemy.pop(indices)

            for index,runner in enumerate(current_level.list_runner):
                if runner.is_alive:
                    runner.move()
                    runner.pursuit(current_level.player_1)
                    runner.update()
                    runner.draw(screen)
                else:
                    current_level.list_runner.pop(index)

            if seconds==30 and len(current_level.list_bonus)==0:
                Spawn.bonus(current_level.list_bonus,current_level.list_bonus_spawn,len(current_level.list_bonus_spawn))
        
            if current_level.player_1.rect.colliderect(current_level.portal.rect) and current_level.portal.on:
                current_level.player_1.score = "{0}:".format(minutes).zfill(2)+"{0}".format(seconds).zfill(2)
                current_level.player_1.is_win = True

        elif current_level.player_1.is_alive and current_level.player_1.is_win:
            Items.end_game(screen,current_level.player_1.score)

        elif not current_level.player_1.is_alive:
            Items.game_over(screen)
            sonido_fondo.stop()

    pygame.display.flip()
    