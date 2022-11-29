import pygame
import sys
from constantes import *

class InitMenu:
    def __init__(self) -> None:
        self.initing = True
        self.init_level = False
        self.w = 700
        self.h = 150
        self.font = pygame.font.SysFont("Comic Sans", 60)
        self.text_1 = self.font.render(("LEVEL 1"), True, (255, 255, 255))
        self.rect_rect_1 = pygame.Rect(200,70,self.w,self.h)
        self.rect_rect_1_content = pygame.Rect(210,80,self.w-20,self.h-20)
        self.rect_1_is_select = True

        self.text_2 = self.font.render(("LEVEL 1"), True, (255, 255, 255))
        self.rect_rect_2 = pygame.Rect(200,240,self.w,self.h)
        self.rect_rect_2_content = pygame.Rect(210,250,self.w-20,self.h-20)
        self.rect_2_is_select = False

        self.text_3 = self.font.render(("LEVEL 1"), True, (255, 255, 255))
        self.rect_rect_3 = pygame.Rect(200,410,self.w,self.h)
        self.rect_rect_3_content = pygame.Rect(210,420,self.w-20,self.h-20)
        self.rect_3_is_select = False


    def run_(self,screen):
        while self.initing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.rect_1_is_select:
                            self.rect_1_is_select = False
                            self.rect_2_is_select = True
                            self.rect_3_is_select = False
                        elif self.rect_2_is_select:
                            self.rect_1_is_select = False
                            self.rect_2_is_select = False
                            self.rect_3_is_select = True
                        elif self.rect_3_is_select:
                            self.rect_1_is_select = True
                            self.rect_2_is_select = False
                            self.rect_3_is_select = False
                    if event.key == pygame.K_UP:
                        if self.rect_1_is_select:
                            self.rect_1_is_select = False
                            self.rect_2_is_select = False
                            self.rect_3_is_select = True
                        elif self.rect_2_is_select:
                            self.rect_1_is_select = True
                            self.rect_2_is_select = False
                            self.rect_3_is_select = False
                        elif self.rect_3_is_select:
                            self.rect_1_is_select = False
                            self.rect_2_is_select = True
                            self.rect_3_is_select = False
                    if event.key == pygame.K_RETURN:
                        self.initing = False
                        self.init_level = True
            self.draw(screen)
            pygame.display.flip()
        

    def draw(self,screen):
        screen.fill((0,0,0))
        if self.rect_1_is_select and not self.rect_2_is_select and not self.rect_3_is_select:
            y_selected = 60
        elif self.rect_2_is_select and not self.rect_1_is_select and not self.rect_3_is_select:
            y_selected = 230
        elif self.rect_3_is_select and not self.rect_1_is_select and not self.rect_2_is_select:
            y_selected = 400
        self.rect_selected = pygame.Rect(190,y_selected,self.w+20,self.h+20)
        pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_selected)

        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_rect_1)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_rect_1_content)
        screen.blit(self.text_1,(280,100))
        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_rect_2)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_rect_2_content)
        screen.blit(self.text_2,(280,270))
        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_rect_3)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_rect_3_content)
        screen.blit(self.text_3,(280,440))


class PauseMenu(InitMenu):
    def __init__(self) -> None:
        super().__init__()
        self.in_pause = False
        self.text_1 = self.font.render(("CONTINUE"), True, (255, 255, 255))
        self.text_2 = self.font.render(("CONFIG"), True, (255, 255, 255))
        self.text_3 = self.font.render(("QUIT"), True, (255, 255, 255))

    def run_(self,screen):
        self.in_pause=True
        while self.in_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.rect_1_is_select:
                            self.rect_1_is_select = False
                            self.rect_2_is_select = True
                            self.rect_3_is_select = False
                        elif self.rect_2_is_select:
                            self.rect_1_is_select = False
                            self.rect_2_is_select = False
                            self.rect_3_is_select = True
                        elif self.rect_3_is_select:
                            self.rect_1_is_select = True
                            self.rect_2_is_select = False
                            self.rect_3_is_select = False
                    if event.key == pygame.K_UP:
                        if self.rect_1_is_select:
                            self.rect_1_is_select = False
                            self.rect_2_is_select = False
                            self.rect_3_is_select = True
                        elif self.rect_2_is_select:
                            self.rect_1_is_select = True
                            self.rect_2_is_select = False
                            self.rect_3_is_select = False
                        elif self.rect_3_is_select:
                            self.rect_1_is_select = False
                            self.rect_2_is_select = True
                            self.rect_3_is_select = False
                    if event.key == pygame.K_RETURN:
                        if self.rect_1_is_select:
                            self.in_pause = False
                        elif self.rect_2_is_select:
                            pass
                        elif self.rect_3_is_select:
                            pygame.quit()
            self.draw(screen)
            pygame.display.flip()