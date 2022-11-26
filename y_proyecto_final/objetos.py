import pygame
from auxiliar import *

class Bonus:
    def __init__(self,x,y,w,h) -> None:
        self.animation = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/y_proyecto_final/resources/Pineapple.png",17,1)
        self.frame = 0
        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y      

    def draw(self,screen):
        
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else:
            self.frame = 0
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)