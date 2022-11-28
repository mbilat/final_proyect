import pygame
import sys
from constantes import *

class GUI:
    def __init__(self) -> None:
        self.initing = True
        self.w = 700
        self.h = 150
        self.font = pygame.font.SysFont("Comic Sans", 60)
        self.text_1 = self.font.render(("LEVEL 1"), True, (255, 255, 255))
        self.rect_lvl1 = pygame.Rect(200,70,self.w,self.h)
        self.rect_lvl1_content = pygame.Rect(210,80,self.w-20,self.h-20)
        self.lvl1_is_select = True

        self.text_2 = self.font.render(("LEVEL 1"), True, (255, 255, 255))
        self.rect_lvl2 = pygame.Rect(200,240,self.w,self.h)
        self.rect_lvl2_content = pygame.Rect(210,250,self.w-20,self.h-20)
        self.lvl2_is_select = False

        self.text_3 = self.font.render(("LEVEL 1"), True, (255, 255, 255))
        self.rect_lvl3 = pygame.Rect(200,410,self.w,self.h)
        self.rect_lvl3_content = pygame.Rect(210,420,self.w-20,self.h-20)
        self.lvl3_is_select = False


    def run_(self,screen):
        while self.initing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.lvl1_is_select:
                            self.lvl1_is_select = False
                            self.lvl2_is_select = True
                            self.lvl3_is_select = False
                        elif self.lvl2_is_select:
                            self.lvl1_is_select = False
                            self.lvl2_is_select = False
                            self.lvl3_is_select = True
                        elif self.lvl3_is_select:
                            self.lvl1_is_select = True
                            self.lvl2_is_select = False
                            self.lvl3_is_select = False
                    if event.key == pygame.K_UP:
                        if self.lvl1_is_select:
                            self.lvl1_is_select = False
                            self.lvl2_is_select = False
                            self.lvl3_is_select = True
                        elif self.lvl2_is_select:
                            self.lvl1_is_select = True
                            self.lvl2_is_select = False
                            self.lvl3_is_select = False
                        elif self.lvl3_is_select:
                            self.lvl1_is_select = False
                            self.lvl2_is_select = True
                            self.lvl3_is_select = False
                    if event.key == pygame.K_RETURN:
                        self.initing = False
            self.draw(screen)
            pygame.display.flip()
        

    def draw(self,screen):
        screen.fill((0,0,0))
        if self.lvl1_is_select and not self.lvl2_is_select and not self.lvl3_is_select:
            y_selected = 60
        elif self.lvl2_is_select and not self.lvl1_is_select and not self.lvl3_is_select:
            y_selected = 230
        elif self.lvl3_is_select and not self.lvl1_is_select and not self.lvl2_is_select:
            y_selected = 400
        self.rect_selected = pygame.Rect(190,y_selected,self.w+20,self.h+20)
        pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_selected)

        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_lvl1)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_lvl1_content)
        screen.blit(self.text_1,(280,100))
        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_lvl2)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_lvl2_content)
        screen.blit(self.text_2,(280,270))
        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_lvl3)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_lvl3_content)
        screen.blit(self.text_3,(280,440))