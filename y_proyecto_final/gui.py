import pygame
import sys
from constantes import *
from auxiliar import *

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

        self.text_2 = self.font.render(("LEVEL 2"), True, (255, 255, 255))
        self.rect_2 = pygame.Rect(200,240,self.w,self.h)
        self.rect_2_content = pygame.Rect(210,250,self.w-20,self.h-20)
        self.rect_2_is_select = False

        self.text_3 = self.font.render(("LEVEL 3"), True, (255, 255, 255))
        self.rect_3 = pygame.Rect(200,410,self.w,self.h)
        self.rect_3_content = pygame.Rect(210,420,self.w-20,self.h-20)
        self.rect_3_is_select = False
        
        self.sound = pygame.mixer.Sound("y_proyecto_final/resources/sounds/menu_sound.mp3")

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

    def run_(self,screen,sound_on)->str:
        retorno = "lvl_1"
        while self.initing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if sound_on:
                            self.sound.play()
                        self.move_in_menu_down()
                    if event.key == pygame.K_UP:
                        if sound_on:
                            self.sound.play()
                        self.move_in_menu_up()
                    if event.key == pygame.K_RETURN:
                        if sound_on:
                            self.sound.play()
                        if self.rect_1_is_select:
                            retorno = "lvl_1"
                        elif self.rect_2_is_select:
                            retorno = "lvl_2"
                        elif self.rect_3_is_select:
                            retorno = "lvl_3"
                        self.init_level = True
                        self.initing = False
                        
            self.draw(screen)
            pygame.display.flip()
        return retorno
        

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

    def run_(self,screen,music,sound_on):
        self.in_pause=True
        while self.in_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if sound_on:
                            self.sound.play()
                        self.move_in_menu_down()
                    if event.key == pygame.K_UP:
                        if sound_on:
                            self.sound.play()
                        self.move_in_menu_up()
                    if event.key == pygame.K_ESCAPE:
                        self.in_pause = False
                    if event.key == pygame.K_RETURN:
                        if sound_on:
                            self.sound.play()
                        if self.rect_1_is_select:
                            self.in_pause = False
                        elif self.rect_2_is_select:
                            sound_on = self.config.run_(screen,music,sound_on)
                        elif self.rect_3_is_select:
                            pygame.quit()
                retorno = sound_on

            self.draw(screen)
            pygame.display.flip()
        return retorno

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
    
    def run_(self,screen,music,sound_on):
        retorno = sound_on
        self.in_config =True
        while self.in_config :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if sound_on:
                            self.sound.play()
                        self.move_in_menu_down()
                    if event.key == pygame.K_UP:
                        if sound_on:
                            self.sound.play()
                        self.move_in_menu_up()
                    if event.key == pygame.K_ESCAPE:
                        self.in_pause = False
                    if event.key == pygame.K_RETURN:
                        if sound_on:
                            self.sound.play()
                        if self.rect_1_is_select:
                            if self.color_1 == self.color_red:
                                self.color_1= self.color_green
                                sound_on = True
                                retorno = True
                            else:
                                self.color_1=self.color_red
                                sound_on = False
                                retorno = False
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
                        if sound_on:
                            self.sound.play()
                        if self.color_2 == self.color_green and not self.w_2<=0:
                                self.w_2 -= 68
                                self.rect_2_content = pygame.Rect(210,250,self.w_2,self.h-20)
                                self.volume-=0.1
                                music.set_volume(self.volume)

                    if event.key == pygame.K_RIGHT and self.rect_2_is_select:
                        if sound_on:
                            self.sound.play()            
                        if self.color_2 == self.color_green and not self.w_2>=680:
                            self.w_2 += 68
                            self.rect_2_content = pygame.Rect(210,250,self.w_2,self.h-20)
                            self.volume+=0.1
                            music.set_volume(self.volume)

            self.draw(screen)
            pygame.display.flip()
        return retorno
        
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
        self.win_tuple = ("",0.0)
        self.text_1 = self.font.render(("PLAY AGAIN"), True, (255, 255, 255))
        self.text_2 = self.font.render(("SCORE LIST"), True, (255, 255, 255))
        self.text_3 = self.font.render(("QUIT"), True, (255, 255, 255))

    def run_(self,screen,win,points,sound_on):
        new_game = False
        self.is_lose = True
        if win:
            self.is_win = True
            self.is_lose = False
            winner = EnterScore(points)
        self.in_end_screen = True
        self.is_ending = True

        while self.is_ending:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.in_end_screen and self.is_win:
                    self.win_tuple,self.in_end_screen = winner.run_(screen,sound_on)
                    Auxiliar.upload_sql()
                    Auxiliar.edit_sql(self.win_tuple)
                elif not self.in_end_screen:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            if sound_on:
                                self.sound.play()
                            self.move_in_menu_down()
                        if event.key == pygame.K_UP:
                            if sound_on:
                                self.sound.play()
                            self.move_in_menu_up()
                        if event.key == pygame.K_RETURN:
                            if sound_on:
                                self.sound.play()
                            self.initing = False
                            self.init_level = True
                        if event.key == pygame.K_RETURN:
                            if self.rect_1_is_select:
                                new_game = True
                                self.is_ending = False
                            elif self.rect_2_is_select:
                                top_three = []
                                top_three = Auxiliar.get_scores_sql()
                                scores= HighScore(top_three)
                                scores.run_(screen,sound_on)
                            elif self.rect_3_is_select:
                                pygame.quit()
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.in_end_screen = False
            self.draw(screen,points)
            pygame.display.flip()
        return new_game

    def draw(self,screen,points):

        if self.in_end_screen:
            font  = pygame.font.SysFont("Arial Narrow", 80)
            screen.fill((0,0,0))
            if self.is_win:
                text = font.render("YOU WIN! Insert your name!",True,(255,255,255))
                screen.blit(text,(220,300))
                text = font.render("Your time : {0}".format(points), True, (255, 255, 255))
                screen.blit(text,(400,400))
            elif self.is_lose:
                text = font.render(("GAME OVER :("), True, (255, 255, 255))
                screen.blit(text,(400,200))
            font  = pygame.font.SysFont("Arial Narrow", 50)
            text = font.render(("Press ENTER to continue."), True, (255, 255, 255))
            screen.blit(text,(400,500))
        else:
            return super().draw(screen)

class EnterScore():
    def __init__(self,score) -> None:
        self.rect_text = pygame.Rect(250,70,700,150)
        self.player_name = ""
        self.score = float(score)
        self.is_enter = False
        self.sound = pygame.mixer.Sound("y_proyecto_final/resources/sounds/menu_sound.mp3")
        self.sound_on = True

    def run_(self,screen,sound_on):
        self.sound_on = sound_on
        self.is_enter = True

        while self.is_enter:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if len(self.player_name)>=0 and len(self.player_name)<6 :
                        if sound_on:
                            self.sound.play()
                        if event.key == pygame.K_BACKSPACE:
                            self.player_name = self.player_name[:-1]
                        else:
                            if not len(self.player_name) == 5 and str(event.unicode).isalpha():
                                self.player_name += event.unicode
                        if event.key == pygame.K_RETURN:
                            self.is_enter= False
                        self.player_name = self.player_name.upper()
                        if not self.is_enter:    
                            return (self.player_name,self.score),False

            self.draw(screen)
            pygame.display.flip()  

    def draw(self,screen):
        pygame.draw.rect(screen,color=(255,255,255),rect=self.rect_text)
        font  = pygame.font.SysFont("Arial Narrow", 180)
        text = font.render(("{0}".format(self.player_name)), True, (0,0,0))
        screen.blit(text,(390,90))

class HighScore(InitMenu): 
    def __init__(self,list_top) -> None:
        super().__init__()
        self.text_1 = self.font.render("1° {0} - {1}".format(str(list_top[0]),str(list_top[1])).zfill(4),True,(255,255,255))
        self.text_2 = self.font.render("2° {0} - {1}".format(str(list_top[2]),str(list_top[3])).zfill(4),True,(255,255,255))
        self.text_3 = self.font.render("3° {0} - {1}".format(str(list_top[4]),str(list_top[5])).zfill(4),True,(255,255,255))