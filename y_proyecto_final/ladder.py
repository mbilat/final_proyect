import pygame
from constantes import *

class Ladder:
    def __init__(self,x,y,w,h) -> None:
        self.image = pygame.image.load("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/y_proyecto_final/resources/ladder.png")
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y      
        self.rect_collide = pygame.Rect((self.rect.x),(self.rect.y+8),(self.rect.width-2),(self.rect.height))
        self.rect_bottom =  pygame.Rect((self.rect.x-10),(self.rect.y+self.rect.height+10),(self.rect.width+20),(40))

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,255 ,0),rect=self.rect_bottom)
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.rect_collide)
        screen.blit(self.image,self.rect)