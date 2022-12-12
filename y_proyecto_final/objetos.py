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
        self.sound = pygame.mixer.Sound("resources/sounds/bonus_taken.mp3")

    def draw(self,screen):
        '''
        Draw the object depending on its animation. Change the frame of the animation.
        '''
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
        self.take_sound = pygame.mixer.Sound("resources/sounds/flag_catch.mp3")
    
    def is_caught(self,player,sound_on):
        '''
        If is_taken is False and the character collides with the object is_taken becomes True. Add a key to the player.
        Play a sound if sound is on.
        '''
        if not self.is_taken and self.rect.colliderect(player.rect):
            if sound_on:
                self.take_sound.play()
            self.is_taken = True
            player.keys +=1

    def draw(self, screen):
        '''
        Draw the object depending on its animation.
        '''
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
        self.sound = pygame.mixer.Sound("resources/sounds/portal.mp3")

    def activate_draw(self,player,screen,sound_on):
        '''
        If the player meets the requirements, draw the portal.
        '''
        if player.keys >= 4:
            if not self.on:
                if sound_on:
                    self.sound.play()
                self.on = True
            self.draw(screen)

    def draw(self,screen):
        '''
        Draw the object depending on its animation. Change the frame of the animation.
        '''
        if self.on:
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else:
                self.frame = 0
            self.image = self.animation[self.frame]
            screen.blit(pygame.transform.scale(self.image,(self.w,self.h)),self.rect)