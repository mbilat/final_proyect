import pygame
from gui import *
from constructor import *
from spawn import *
from auxiliar import *

class Changes:
    def draws_and_updates(screen,current_level,items,delta_ms,keys):
        '''
        Passes parameters to functions while running the level, updating and drawing everything on the screen.
        '''

        items.draw_on_game(screen,current_level.wallpaper,current_level.player_1,current_level.seconds,current_level.minutes)
        current_level.last_spawn += 1

        if len(current_level.list_enemy)==0:
            Spawn.enemy(current_level.list_enemy,current_level.list_enemy_spawn,len(current_level.list_enemy_spawn),Enemy)

        if len(current_level.list_enemy)<3 and current_level.last_spawn>20:
            Spawn.enemy(current_level.list_enemy,current_level.list_enemy_spawn,len(current_level.list_enemy_spawn),Enemy)
            current_level.last_spawn=0
        
        if len(current_level.list_runner)==0 and current_level.last_spawn>15:
            Spawn.enemy(current_level.list_runner,current_level.list_runner_spawn,len(current_level.list_runner_spawn),Runner)

        Auxiliar.list_draw(current_level.list_platforms,screen)
        Auxiliar.list_draw(current_level.ladder_list,screen)
        
        if len(current_level.list_keys)<4:
            if current_level.time_keys <=0:
                current_level.time_keys = 50
                Spawn.keys(current_level.list_keys,current_level.list_keys_spawn,len(current_level.list_keys_spawn))
            current_level.time_keys -=1

        current_level.portal.activate_draw(current_level.player_1,screen,current_level.sound_on)

        current_level.player_1.events(delta_ms,keys,current_level.ladder_list,current_level.sound_on)
        current_level.player_1.update(delta_ms,current_level.list_enemy,current_level.list_runner,current_level.list_platforms)
        current_level.player_1.draw(screen)

        for flags in current_level.list_keys:
            flags.is_caught(current_level.player_1,current_level.sound_on)
            flags.draw(screen)

        for cantidad,fruta in enumerate(current_level.list_bonus):
            fruta.draw(screen)
            if current_level.player_1.colision(fruta.rect):
                if current_level.sound_on:
                    fruta.sound.play()
                current_level.player_1.municion += 10
                current_level.list_bonus.pop(cantidad)

        for indices,enemigo in enumerate(current_level.list_enemy):
            if enemigo.is_alive:
                enemigo.shot(current_level.player_1)
                enemigo.move()
                enemigo.update(current_level.player_1,current_level.list_platforms,current_level.sound_on)
                enemigo.draw(screen)  
            else:
                current_level.list_enemy.pop(indices)

        for index,runner in enumerate(current_level.list_runner):
            if runner.is_alive:
                runner.move()
                runner.pursuit(current_level.player_1)
                runner.update(current_level.sound_on)
                runner.draw(screen)
            else:
                current_level.list_runner.pop(index)

        if current_level.seconds==30 and len(current_level.list_bonus)==0:
            Spawn.bonus(current_level.list_bonus,current_level.list_bonus_spawn,len(current_level.list_bonus_spawn))
    
        if current_level.player_1.rect.colliderect(current_level.portal.rect) and current_level.portal.on:
            current_level.player_1.score = "{0}.".format(current_level.minutes).zfill(2)+"{0}".format(current_level.seconds).zfill(2)
            current_level.player_1.is_win = True
