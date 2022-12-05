import pygame
from constantes import *
from proyectil import *
from auxiliar import Auxiliar

class Player:
    def __init__(self,x,y,w,h,speed_walk,speed_run,jump_power,frame_rate_ms,move_rate_ms,interval_time_jump=100) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/player1/Run (32x32).png",12,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/player1/Run (32x32).png",12,1,True)
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/player1/Idle (32x32).png",11,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/player1/Idle (32x32).png",11,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/player1/Jump (32x32).png",1,1,False)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/player1/Jump (32x32).png",1,1,True)
        self.w = w
        self.h = h
        self.frame = 0
        self.lives = 100
        self.is_alive = True
        self.not_alive_sound = pygame.mixer.Sound("y_proyecto_final/resources/sounds/portal.mp3")
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = GRAVITY
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.l_or_r = "R"

        self.sound_on = True

        self.jump_power = jump_power
        self.is_jump = False
        self.jump_timer = 0

        self.keys = 0
        self.rect_collide_foot = pygame.Rect((self.rect.x+2),self.rect.y+self.rect.height-2,self.rect.width-4,self.rect.height/8)
        self.municion = 5
        self.lista_municion = []
        self.shot_sound = pygame.mixer.Sound("y_proyecto_final/resources/sounds/shot_from_player.mp3")
        self.shot_in_enemy_sound = pygame.mixer.Sound("y_proyecto_final/resources/sounds/shot_on_enemy.mp3")
        self.shot_timer = 0
        self.score = 0
        self.is_win = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0

        self.is_on_ladder = True
        self.is_climbing = False
        self.is_on_ground = True
        self.climb_speed = 10
        self.is_touch_bottom = True

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 
        self.interval_time_jump = interval_time_jump

    def colision(self,objeto)->bool:
        if self.rect.colliderect(objeto):
            return True


    def events(self,delta_ms,keys,ladder_list,sound_on):

        self.tiempo_transcurrido += delta_ms
        self.detect_ladder(ladder_list)
        self.sound_on = sound_on

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

        if(keys[pygame.K_UP] and self.is_on_ladder and not keys[pygame.K_DOWN]and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
            self.is_climbing = True
            self.climb_ladder("UP",ladder_list)
        elif(not keys[pygame.K_UP] and self.is_on_ladder and keys[pygame.K_DOWN]and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
            self.is_climbing =True
            self.climb_ladder("DOWN",ladder_list)
        
        else:
            self.is_climbing = False
            self.gravity = GRAVITY

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
                if self.sound_on:
                    self.shot_sound.play()
                self.lista_municion.append(Proyectil((self.rect.x+30),(self.rect.y+16),12,self.l_or_r))
                self.municion-=1
                print(self.rect.x,self.rect.y)

    def municion_update(self,list_enemy,list_block):

        if len(self.lista_municion)>0:
            for index,bullet in enumerate(self.lista_municion):
                for enemy in list_enemy:
                    if bullet.colision(enemy.rect):
                        if self.sound_on:
                            self.shot_in_enemy_sound.play()
                        enemy.lives -=1
                        self.lista_municion.pop(index)
                        if enemy.lives == 0:
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
        
        self.is_touch_ladders=len(list_ladder)
        self.is_climb_ladders=len(list_ladder)
        self.bottom_ladders=len(list_ladder)

        for ladder in list_ladder:
            if self.colision(ladder):
                self.is_touch_ladders -=1
            if self.rect_collide_foot.colliderect(ladder.rect_collide):
                self.is_climb_ladders -=1
            if self.rect_collide_foot.colliderect(ladder.rect_bottom):
                self.bottom_ladders -=1

        if self.is_touch_ladders == len(list_ladder):
            self.is_on_ladder = False
        else:
            self.is_on_ladder = True

        if self.is_climb_ladders== len(list_ladder):
            self.is_on_ground = True
        else:
            self.is_on_ground = False
        
        if self.bottom_ladders== len(list_ladder):
            self.is_touch_bottom = False
        else:
            self.is_touch_bottom = True
        
        if self.is_on_ladder:
            self.gravity = 0
        else :
            self.gravity = GRAVITY
        


    def climb_ladder(self,climb_up_down,list_ladder):

        self.detect_ladder(list_ladder)
        
        if self.is_on_ladder and climb_up_down == "UP" and self.is_climbing:
            self.move_y = -self.climb_speed
        elif self.is_on_ladder and climb_up_down == "DOWN" and self.is_climbing:
            if not self.is_touch_bottom:
                self.move_y = self.climb_speed
            else:
                self.move_y = 0
        elif not self.is_on_ladder:
            self.move_y = 0
        if self.is_climbing:
            self.gravity = 0
        else: 
            self.gravity = GRAVITY
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

    def do_movement(self,delta_ms,plataform_list):

        self.tiempo_transcurrido_move += delta_ms

        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0 

            if self.is_on_ground:
                self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.gravity = GRAVITY
                    self.change_y(self.gravity)
            
     
    def change_x(self,delta_x):
        proof_x = self.rect.x
        proof_x += delta_x
        if proof_x > 5 and proof_x < (ANCHO_VENTANA-5):
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

        self.shot_timer_update()
        if self.lives <= 0:
            if self.sound_on:
                self.not_alive_sound.play()
            self.is_alive = False

        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0
            if(self.is_jump == True):
                self.is_jump = False

        self.municion_update(list_enemy,list_block)
        self.municion_update(list_enemy_2,list_block)
        self.do_movement(delta_ms,list_block)
        
    
    def draw(self,screen):
        if self.is_alive:
            if(DEBUG):
                pygame.draw.rect(screen,color=(0,0 ,255),rect=self.rect_collide_foot)
            for bullet in self.lista_municion:
                bullet.draw(screen)
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
            