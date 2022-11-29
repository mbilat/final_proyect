import pygame
from constantes import *

class Items:
    def draw_on_game(screen,imagen_fondo,player,seconds,minutes):

        font = pygame.font.SysFont("Times New Roman", 20)
        
        screen.blit(imagen_fondo,imagen_fondo.get_rect())
        text = font.render("VIDAS : {0}".format(player.lives), True, (0, 0, 0))
        screen.blit(text,(10,ALTO_VENTANA-100))
        text = font.render("MUNICION : {0}".format(player.municion), True, (0, 0, 0))
        screen.blit(text,(10,ALTO_VENTANA-125))
        text = font.render(("{0}:".format(minutes).zfill(2)+"{0}".format(seconds).zfill(2)), True, (0, 0, 0))
        screen.blit(text,(1150,ALTO_VENTANA-100))

    def end_game(screen,points):
        screen.fill((0,0,0))

        font = font = pygame.font.SysFont("Arial Narrow", 80)
        text = font.render("Your time : {0}".format(points), True, (255, 255, 255))
        screen.blit(text,(320,ALTO_VENTANA/2))

        font = font = pygame.font.SysFont("Arial Narrow", 100)
        text = font.render("You Win!", True, (255, 255, 255))
        screen.blit(text,(300,200))


    def game_over(screen):
        screen.fill((0,0,0))
        font = font = pygame.font.SysFont("Arial Narrow", 150)
        text = font.render(("GAME OVER"), True, (255, 255, 255))
        screen.blit(text,(320,ALTO_VENTANA/2))