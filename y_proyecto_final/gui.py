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
        self.rect_1 = pygame.Rect(200,70,self.w,self.h)
        self.rect_1_content = pygame.Rect(210,80,self.w-20,self.h-20)
        self.rect_1_is_select = True

        self.text_2 = self.font.render(("LEVEL 1"), True, (255, 255, 255))
        self.rect_2 = pygame.Rect(200,240,self.w,self.h)
        self.rect_2_content = pygame.Rect(210,250,self.w-20,self.h-20)
        self.rect_2_is_select = False

        self.text_3 = self.font.render(("LEVEL 1"), True, (255, 255, 255))
        self.rect_3 = pygame.Rect(200,410,self.w,self.h)
        self.rect_3_content = pygame.Rect(210,420,self.w-20,self.h-20)
        self.rect_3_is_select = False


    def move_in_menu_down(self):
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

    def move_in_menu_up(self):
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

    def run_(self,screen)->str:
        retorno = "lvl_1"
        while self.initing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.move_in_menu_down()
                    if event.key == pygame.K_UP:
                        self.move_in_menu_up()
                    if event.key == pygame.K_RETURN:
                        if self.rect_1_is_select:
                            retorno = "lvl_1"
                        elif self.rect_2_is_select:
                            retorno = "lvl_2"
                        elif self.rect_3_is_select:
                            retorno = "lvl_1"
                        self.initing = False
                        return retorno
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

        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_1)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_1_content)
        screen.blit(self.text_1,(280,100))
        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_2)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_2_content)
        screen.blit(self.text_2,(280,270))
        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_3)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_3_content)
        screen.blit(self.text_3,(280,440))


class PauseMenu(InitMenu):
    def __init__(self) -> None:
        super().__init__()
        self.in_pause = False
        self.text_1 = self.font.render(("CONTINUE"), True, (255, 255, 255))
        self.text_2 = self.font.render(("CONFIG"), True, (255, 255, 255))
        self.text_3 = self.font.render(("QUIT"), True, (255, 255, 255))
        self.config = ConfigMenu()

    def run_(self,screen,music):
        self.in_pause=True
        while self.in_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.move_in_menu_down()
                    if event.key == pygame.K_UP:
                        self.move_in_menu_up()
                    if event.key == pygame.K_ESCAPE:
                        self.in_pause = False
                    if event.key == pygame.K_RETURN:
                        if self.rect_1_is_select:
                            self.in_pause = False
                        elif self.rect_2_is_select:
                            self.config.run_(screen,music)
                        elif self.rect_3_is_select:
                            pygame.quit()

            self.draw(screen)
            pygame.display.flip()

class ConfigMenu(InitMenu):
    def __init__(self) -> None:
        super().__init__()
        self.in_config = False
        self.color_green = (96,169,23)
        self.color_red = (162,0,37)

        self.color_1 = self.color_green
        self.text_1 = self.font.render(("SOUNDS"), True,(255, 255, 255))

        self.w_2 =680
        self.color_2 = self.color_green
        self.text_2 = self.font.render(("MUSIC"), True, (255, 255, 255)) 
        self.rect_2_content = pygame.Rect(210,250,self.w_2,self.h-20)
        self.volume = 1.0

        self.text_3 = self.font.render(("BACK"), True, (255, 255, 255))
    
    def run_(self,screen,music):
        self.in_config =True
        while self.in_config :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.move_in_menu_down()
                    if event.key == pygame.K_UP:
                        self.move_in_menu_up()

                    if event.key == pygame.K_ESCAPE:
                        self.in_pause = False
                    if event.key == pygame.K_RETURN:
                        if self.rect_1_is_select:
                            if self.color_1 == self.color_red:
                                self.color_1= self.color_green
                            else:
                                self.color_1=self.color_red

                        elif self.rect_2_is_select:
                            if self.color_2 == self.color_red:
                                self.color_2= self.color_green
                                music.play()
                            else:
                                self.color_2=self.color_red
                                music.stop()
                        elif self.rect_3_is_select:
                            self.in_config = False
                    if event.key == pygame.K_LEFT and self.rect_2_is_select:
                        if self.color_2 == self.color_green and not self.w_2<=0:
                                self.w_2 -= 68
                                self.rect_2_content = pygame.Rect(210,250,self.w_2,self.h-20)
                                self.volume-=0.1
                                music.set_volume(self.volume)

                    if event.key == pygame.K_RIGHT and self.rect_2_is_select:            
                            if self.color_2 == self.color_green and not self.w_2>=680:
                                self.w_2 += 68
                                self.rect_2_content = pygame.Rect(210,250,self.w_2,self.h-20)
                                self.volume+=0.1
                                music.set_volume(self.volume)

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

        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_1)
        pygame.draw.rect(screen,color=self.color_1,rect=self.rect_1_content)
        screen.blit(self.text_1,(280,100))
        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_2)
        pygame.draw.rect(screen,color=self.color_2,rect=self.rect_2_content)
        screen.blit(self.text_2,(280,270))
        pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_3)
        pygame.draw.rect(screen,color=(0,0,0),rect=self.rect_3_content)
        screen.blit(self.text_3,(280,440))


class EndGameMenu(InitMenu):
    def __init__(self) -> None:
        super().__init__()
        self.is_ending = False
        self.in_end_screen = False
        self.is_lose = False
        self.is_win = False
        self.text_1 = self.font.render(("PLAY AGAIN"), True, (255, 255, 255))
        self.text_2 = self.font.render(("SCORE LIST"), True, (255, 255, 255))
        self.text_3 = self.font.render(("QUIT"), True, (255, 255, 255))

        #SEGUIR->

    def run_(self,screen,win,points,new_game):

        if win:
            self.is_win = True
        self.in_end_screen = True
        self.is_ending = True
        while self.is_ending:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.in_end_screen:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.in_end_screen= False
                else :
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            self.move_in_menu_down()
                        if event.key == pygame.K_UP:
                            self.move_in_menu_up()
                        if event.key == pygame.K_RETURN:
                            self.initing = False
                            self.init_level = True
                        if event.key == pygame.K_RETURN:
                            if self.rect_1_is_select:
                                new_game = True
                            elif self.rect_2_is_select:
                                pass
                            elif self.rect_3_is_select:
                                pygame.quit()
            self.draw(screen,points)
            pygame.display.flip()
    
    def draw(self,screen,points):
        if self.in_end_screen:
            font = font = pygame.font.SysFont("Arial Narrow", 80)
            screen.fill((0,0,0))
            if self.is_win:   
                text = font.render("YOU WIN! - Your time : {0}".format(points), True, (255, 255, 255))
                screen.blit(text,(100,200))
            else:
                text = font.render(("GAME OVER :("), True, (255, 255, 255))
                screen.blit(text,(200,200))
            text = font.render(("Press SPACE to continue."), True, (255, 255, 255))
            screen.blit(text,(200,400))
        else:
            return super().draw(screen)
