import pygame
from constantes import *
from proyectil import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,w,h,speed_walk,speed_run,jump_power,frame_rate_ms,move_rate_ms,jump_height,interval_time_jump=100) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/y_proyecto_final/resources/player1/Run (32x32).png",12,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/y_proyecto_final/resources/player1/Run (32x32).png",12,1,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/y_proyecto_final/resources/player1/Idle (32x32).png",11,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/y_proyecto_final/resources/player1/Idle (32x32).png",11,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/y_proyecto_final/resources/player1/Jump (32x32).png",1,1,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/backup/ArchivosUTN/primercuatri/y_proyecto_final/resources/player1/Jump (32x32).png",1,1,True)
        self.w = w
        self.h = h
        self.frame = 0
        self.lives = 5
        self.is_alive = True
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = GRAVITIY
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.l_or_r = "R"
        self.jump_power = jump_power
        self.is_jump = False
        self.jump_timer = 0

        self.rect_collide_foot = pygame.Rect((self.rect.x+2),self.rect.y+self.rect.height-2,self.rect.width-4,self.rect.height/8)
        self.municion = 5
        self.lista_municion = []
        self.shot_timer = 0
        self.score = 0

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.is_on_ladder = True
        self.is_climbing = False
        self.climb_speed = 15

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 
        self.interval_time_jump = interval_time_jump

    def colision(self,objeto)->bool:
        if self.rect.colliderect(objeto):
            return True


    def events(self,delta_ms,keys,ladder_list):

        self.tiempo_transcurrido += delta_ms
        self.detect_ladder(ladder_list)

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.move_x = -self.speed_walk
            if not self.animation == self.walk_l:
                self.animation = self.walk_l
                self.frame = 0
            self.l_or_r = "L"

        if (keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
            self.move_x = self.speed_walk
            if not self.animation == self.walk_r:
                self.animation = self.walk_r
                self.frame = 0
            self.l_or_r = "R"

        if(keys[pygame.K_UP] and self.is_on_ladder and not keys[pygame.K_DOWN]):
            self.is_climbing = True
            self.climb_ladder("UP",ladder_list)
        elif(not keys[pygame.K_UP] and self.is_on_ladder and keys[pygame.K_DOWN]):
            self.is_climbing =True
            self.climb_ladder("DOWN",ladder_list)
        else:
            self.is_climbing = False

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  
        '''   
        if(keys[pygame.K_SPACE]) and (self.jump_timer== 0 ) and not self.is_jump:
            self.jump_timer= 100
            self.is_jump= True
            self.jump()
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.tiempo_last_jump = self.tiempo_transcurrido
        '''      
        if(keys[pygame.K_x]) and self.shot_timer==0:
            self.shot_timer = 20
            if self.municion>0:
                self.lista_municion.append(Proyectil((self.rect.x+30),(self.rect.y+16),5,self.l_or_r))
                self.municion-=1
                print(self.rect.x,self.rect.y)

    def municion_update(self,list_enemy,list_enemy_type_2,list_block):

        if len(self.lista_municion)>0:
            for index,bullet in enumerate(self.lista_municion):
                for enemy in list_enemy:
                    if bullet.colision(enemy.rect):
                        print("pego")
                        self.lista_municion.pop(index)
                        enemy.is_alive = False
                        break

        if len(self.lista_municion)>0:
            for index,bullet in enumerate(self.lista_municion):
                for enemy in list_enemy_type_2:
                    if bullet.colision(enemy.rect):
                        print("pego")
                        enemy.lives -=1
                        if enemy.lives == 0:
                            self.lista_municion.pop(index)
                            enemy.is_alive = False
                            break

            for index,bullet in enumerate(self.lista_municion):
                for block in list_block:
                    if bullet.colision(block.rect):
                        self.lista_municion.pop(index)
                        break
                bullet.update()

    def stay(self):
        if self.l_or_r == "R":
            self.animation = self.stay_r
        else:
            self.animation= self.stay_l
        if not self.is_climbing:
            self.move_y = 0
        self.move_x = 0
        self.frame = 0        

    def detect_ladder(self,list_ladder):

        self.is_touch_ladder=len(list_ladder)
        for ladder in list_ladder:
            if self.colision(ladder):
                self.is_touch_ladder -=1
                print("ladder")
        if self.is_touch_ladder == len(list_ladder):
            self.is_on_ladder = False
        else:
            self.is_on_ladder = True

    def climb_ladder(self,climb_up_down,list_ladder):

        self.detect_ladder(list_ladder)
        
        if self.is_on_ladder and climb_up_down == "UP" and self.is_climbing:
            self.move_y = -self.climb_speed
        elif self.is_on_ladder and climb_up_down == "DOWN" and self.is_climbing:
            if not self.rect.y== GROUND_LEVEL:
                self.move_y = self.climb_speed
        elif not self.is_on_ladder:
            print("bajaa")
            self.move_y = 0
        if self.is_climbing:
            self.gravity = 0
        else: 
            self.gravity = GRAVITIY
        self.is_on_ladder = False

    def jump(self,on_off = True):
        '''
        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if(self.l_or_r == "R"):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
                self.frame = 0
            self.is_jump = True
        '''

        if self.is_jump == True:
            if self.jump_power >= -(self.jump_power):
                if self.jump_power < 0:
                    self.move_y +=(self.jump_power**2)*0.5
                else:
                    print("salta")
                    self.move_y -=(self.jump_power**2)*0.5
                self.jump_power-=1           
            else:
                self.is_jump = False
                self.jump_power = 25

            if(on_off == False):
                self.is_jump = False
                self.stay()


    def shot_timer_update(self):
        if self.shot_timer>0: 
            self.shot_timer-=1

    def jump_timer_update(self):
        if (self.jump_timer> 0): 
            self.jump_timer-= 1

    def do_movement(self,delta_ms,plataform_list):

        self.tiempo_transcurrido_move += delta_ms

        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0       
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
     

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_collide_foot.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.rect_collide_foot.y += delta_y

    def is_on_plataform(self,plataform_list):

        retorno = False
        
        if(self.rect.y>= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.rect_collide_foot.colliderect(plataforma.rect_collide)):
                    retorno = True
                    break       
        return retorno 

    def update(self,delta_ms,list_enemy,list_enemy_2,list_block):

        self.jump_timer_update()
        self.shot_timer_update()
        if self.lives <= 0:
            self.is_alive = False

        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0
            if(self.is_jump == True):
                self.is_jump = False

        self.municion_update(list_enemy,list_enemy_2,list_block)
        self.do_movement(delta_ms,list_block)
        
    
    def draw(self,screen):
        if self.is_alive:
            if(DEBUG):
                pygame.draw.rect(screen,color=(0,0 ,255),rect=self.rect_collide_foot)
            for bullet in self.lista_municion:
                bullet.draw(screen)
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
            


