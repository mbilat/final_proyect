import pygame
from auxiliar import *

class Bonus:
    def __init__(self,x,y,w,h) -> None:
        self.animation = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/Pineapple.png",17,1)
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

class Flag(Bonus):
    def __init__(self, x, y, w, h) -> None:
        super().__init__(x, y, w, h)
        self.idle = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/Checkpoint (Flag Idle)(64x64).png",10,1)
        self.caught = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/Checkpoint (No Flag).png",1,1)
        self.animation = self.idle
        self.is_taken = False
    
    def is_caught(self,player):
        if not self.is_taken and self.rect.colliderect(player.rect):
            self.is_taken = True
            player.keys +=1

    def draw(self, screen):
        if self.is_taken:
            self.animation = self.caught
        return super().draw(screen)

class Portal(Bonus):
    def __init__(self, x, y, w, h) -> None:
        super().__init__(x, y, w, h)
        self.animation = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/portal.png",4,1)
        self.on = False
        self.w = w
        self.h = h

    def draw(self,screen):
        if self.on:
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else:
                self.frame = 0
            self.image = self.animation[self.frame]
            screen.blit(pygame.transform.scale(self.image,(self.w,self.h)),self.rect)