import pygame
from constantes import *

class Menu:
    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Arial Narrow", 50)
        self.text=self.font.render(("PRESS S TO START"), True, (100, 100, 100))
        self.is_starting = True
        
    def init_game(self,key):
        if key[pygame.K_s]:
            self.is_starting = False

    def draw(self,x,y,screen):
        screen.fill((0,0,0))
        screen.blit(self.text,(x,y))
