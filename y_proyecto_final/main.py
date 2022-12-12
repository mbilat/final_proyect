import pygame
import sys
from constantes import *
from screen_items import *
from gui import *
from constructor import *
from changes_in_game import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

tick_1s = pygame.USEREVENT+0
pygame.time.set_timer(tick_1s,1000)

init_game = True
while True:

    if init_game:
        menu = InitMenu()
        level = menu.run_(screen,True)
        pause=PauseMenu()
        end=EndGameMenu()
        current_level = Level(level)
        init_game = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == tick_1s:
            if not current_level.new_game and not pause.in_pause:
                current_level.seconds+=1
                if current_level.seconds ==60:
                    current_level.minutes+=1
                    current_level.seconds=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause.in_pause = True

    keys = pygame.key.get_pressed() 
    delta_ms = clock.tick(FPS)

    if pause.in_pause and menu.init_level:
        current_level.sound_on = pause.run_(screen,current_level.music,current_level.sound_on)
        
    elif menu.init_level and not pause.in_pause:
        if current_level.new_game:
            current_level.init_level()
            if current_level.music_on:
                current_level.music.play()
            current_level.new_game = False
            items = Items()

        if current_level.player_1.is_alive and not current_level.player_1.is_win:
            Changes.draws_and_updates(screen,current_level,items,delta_ms,keys)
            
        elif current_level.player_1.is_alive and current_level.player_1.is_win:
            current_level.music.stop()
            init_game = end.run_(screen,True,current_level.player_1.score,current_level.sound_on)

        elif not current_level.player_1.is_alive:
            current_level.music.stop()
            init_game = end.run_(screen,False,current_level.player_1.score,current_level.sound_on)

    pygame.display.flip()
     