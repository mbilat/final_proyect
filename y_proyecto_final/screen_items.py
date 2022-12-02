import pygame
from constantes import *

class Items:
    def __init__(self) -> None:

        self.life= 100
        self.rect_life = pygame.Rect(7,ALTO_VENTANA-103,106,25)
        self.rect_life_content = pygame.Rect(10,ALTO_VENTANA-100,self.life,20)

    def draw_on_game(self,screen,imagen_fondo,player,seconds,minutes):

        font = pygame.font.SysFont("Times New Roman", 15)
        if not self.life == player.lives:
            self.life = player.lives
            self.rect_life_content = pygame.Rect(10,ALTO_VENTANA-100,self.life,20)

        screen.blit(imagen_fondo,imagen_fondo.get_rect())
        text = font.render("AMMUNITION : {0}".format(player.municion), True, (0, 0, 0))
        screen.blit(text,(10,ALTO_VENTANA-125))
        text = font.render(("{0}:".format(minutes).zfill(2)+"{0}".format(seconds).zfill(2)), True, (0, 0, 0))
        screen.blit(text,(1150,ALTO_VENTANA-100))
        pygame.draw.rect(screen,color=(120,120,120),rect=self.rect_life)
        pygame.draw.rect(screen,color=(0,255,0),rect=self.rect_life_content)
