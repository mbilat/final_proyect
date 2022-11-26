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
from menu_start import *
from ladder import *
from screen_items import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()


imagen_fondo = pygame.image.load("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/clase19/CLASE_19_inicio_juego/images/locations/forest/all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=20,y=GROUND_LEVEL,w=32,h=32,speed_walk=10,speed_run=10,jump_power=50   ,frame_rate_ms=100,move_rate_ms=50,jump_height=140)

lista_municion = []

lista_plataformas = []
lista_plataformas.append(Plataforma(0,(250),300,60))
lista_plataformas.append(Plataforma(300,(250),300,60))
lista_plataformas.append(Plataforma(600,(250),300,60))
lista_plataformas.append(Plataforma(900,(250),300,60))
lista_plataformas.append(Plataforma(0,(400),300,60))
lista_plataformas.append(Plataforma(300,(400),300,60))
lista_plataformas.append(Plataforma(600,(400),300,60))
lista_plataformas.append(Plataforma(900,(400),300,60))


list_bonus_spawns = [
                {"x":30,"y":214},
                {"x":602 ,"y":350}]
lista_bonus = []
Spawn.bonus(lista_bonus,list_bonus_spawns,len(list_bonus_spawns))

list_enemy_spawns = [{"x":134,"y":366},
                {"x":134,"y":214},
                {"x":724,"y":372},
                {"x":724 ,"y":219}]

list_ladder = []
list_ladder.append(Ladder(1160,405,30,150))
list_ladder.append(Ladder(20,245,30,150))

list_runner= []
list_runner.append(Runner(826,GROUND_LEVEL,10))

lista_enemy=[]
Spawn.enemy(lista_enemy,list_enemy_spawns,len(list_enemy_spawns))
last_spawn = 0

timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

tick_1s = pygame.USEREVENT+0
pygame.time.set_timer(tick_1s,1000)

seconds,minutes = 0,0

init_of_game = Menu()
running,pause = True,False

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("y_proyecto_final/resources/passionfruit.mp3")
sonido_fondo.set_volume(0.9)

 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == tick_1s:
            if not init_of_game.is_starting and not pause:
                seconds+=1
                if seconds ==60:
                    minutes+=1
                    seconds=0
    
    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    delta_ms = clock.tick(FPS)


    if init_of_game.is_starting == True:
        init_of_game.draw(ALTO_VENTANA/2,ANCHO_VENTANA/2,screen)
        init_of_game.init_game(keys)
        #sonido_fondo.play()
    elif pause and not init_of_game.is_starting:
        Items.draw_in_init(screen)
        #sonido_fondo.stop()

    elif not init_of_game.is_starting and not pause and player_1.is_alive:

        
        Items.draw_on_game(screen,imagen_fondo,player_1,seconds,minutes)

        last_spawn += seconds

        if len(lista_enemy)==0:
            Spawn.enemy(lista_enemy,list_enemy_spawns,len(list_enemy_spawns))

        if len(lista_enemy)<3 and last_spawn>15:
            Spawn.enemy(lista_enemy,list_enemy_spawns,len(list_enemy_spawns))
            last_spawn=0


        for plataforma in lista_plataformas:
            plataforma.draw(screen)

        for ladder in list_ladder:
            ladder.draw(screen)
            
        player_1.events(delta_ms,keys,list_ladder)
        player_1.update(delta_ms,lista_enemy,list_runner,lista_plataformas)
        player_1.draw(screen)


        for cantidad,fruta in enumerate(lista_bonus):
            fruta.draw(screen)
            if player_1.colision(fruta.rect):
                player_1.municion += 10
                lista_bonus.pop(cantidad)

        for indices,enemigo in enumerate(lista_enemy):
            if enemigo.is_alive:
                enemigo.shot(player_1)
                enemigo.move()
                enemigo.update(player_1,lista_plataformas)
                enemigo.draw(screen)  
            else:
                lista_enemy.pop(indices)
        for index,runner in enumerate(list_runner):
            if runner.is_alive:
                runner.move()
                runner.pursuit(player_1)
                runner.update()
                runner.draw(screen)
            else :
                list_runner.pop(index)

        if seconds==30 and len(lista_bonus)==0:
            Spawn.bonus(lista_bonus,list_bonus_spawns,len(list_bonus_spawns))
    
    elif not init_of_game.is_starting and not player_1.is_alive:
        sonido_fondo.stop()
        screen.fill((0,0,0))
        font = font = pygame.font.SysFont("Arial Narrow", 150)
        text = font.render(("GAME OVER"), True, (255, 255, 255))
        screen.blit(text,(280,250))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE and not pause:
            print("in pause")
            pause = True
        elif event.key == pygame.K_ESCAPE and pause:
            print("NO Pause")
            pause = False     


    pygame.display.flip()
    