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

    def game_over(screen):
        screen.fill((0,0,0))
        font = font = pygame.font.SysFont("Arial Narrow", 150)
        text = font.render(("GAME OVER"), True, (255, 255, 255))
        screen.blit(text,(320,ALTO_VENTANA/2))