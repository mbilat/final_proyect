import pygame
from constantes import *

class Items:
    def draw_on_game(screen,imagen_fondo,player,seconds,minutes):

        font = pygame.font.SysFont("Times New Roman", 20)
        
        screen.blit(imagen_fondo,imagen_fondo.get_rect())
        text = font.render("VIDAS : {0}".format(player.lives), True, (100, 100, 100))
        screen.blit(text,(10,5))
        text = font.render("MUNICION : {0}".format(player.municion), True, (100, 100, 100))
        screen.blit(text,(10,25))
        text = font.render(("{0}:".format(minutes).zfill(2)+"{0}".format(seconds).zfill(2)), True, (255, 255, 255))
        screen.blit(text,(1150,5))

    def draw_in_init(screen,):

        font = pygame.font.SysFont("Times New Roman", 20)

        screen.fill((0,0,0))
        text = font.render("JUEGO EN PAUSA, ESC PARA REANUDAR", True, (250, 255, 250))
        screen.blit(text,(ALTO_VENTANA/2,ANCHO_VENTANA/2))