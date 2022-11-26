import pygame
from constantes import *

class Ladder:
    def __init__(self,x,y,w,h) -> None:
        self.image = pygame.image.load("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/y_proyecto_final/resources/ladder.png")
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y      
        self.rect_collide = pygame.Rect((self.rect.x),(self.rect.y+2),(self.rect.width),(self.rect.height-20))
    

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.rect_collide)