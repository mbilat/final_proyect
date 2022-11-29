import pygame
from constantes import *

class Items:
    def __init__(self) -> None:

        self.life= 100
        self.rect_life = pygame.Rect(7,ALTO_VENTANA-103,106,25)
        self.rect_life_content = pygame.Rect(10,ALTO_VENTANA-100,self.life,20)

    def draw_on_game(self,screen,imagen_fondo,player,seconds,minutes):

        font = pygame.font.SysFont("Times New Roman", 20)
        if not self.life == player.lives:
            self.life = player.lives
            self.rect_life_content = pygame.Rect(10,ALTO_VENTANA-100,self.life,20)
            
        #text = font.render("VIDAS : {0}".format(player.lives), True, (0, 0, 0))
        #screen.blit(text,(10,ALTO_VENTANA-100))

        screen.blit(imagen_fondo,imagen_fondo.get_rect())
        text = font.render("MUNICION : {0}".format(player.municion), True, (0, 0, 0))
        screen.blit(text,(10,ALTO_VENTANA-125))
        text = font.render(("{0}:".format(minutes).zfill(2)+"{0}".format(seconds).zfill(2)), True, (0, 0, 0))
        screen.blit(text,(1150,ALTO_VENTANA-100))
        pygame.draw.rect(screen,color=(120,120,120),rect=self.rect_life)
        pygame.draw.rect(screen,color=(0,255,0),rect=self.rect_life_content)

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