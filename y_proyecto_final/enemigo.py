import pygame
from auxiliar import Auxiliar
from constantes import *
from proyectil import *

class Enemy():
    def __init__(self,x,y,speed) -> None:
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/enemies/Run (64x32).png",14,1)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/enemies/Run (64x32).png",14,1,True)
        self.frame = 0
        self.animate = self.walk_l
        self.image = self.animate[self.frame]
        self.speed = speed
        self.move_x = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_alive = True
        self.l_o_r = "L"
        self.start_x = self.rect.x
        self.range_rect_r = pygame.Rect(self.rect.x+20,self.rect.y-15,self.rect.width+130,self.rect.height+30)
        self.range_rect_l = pygame.Rect(self.rect.x-155,self.rect.y-15,self.rect.width+130,self.rect.height+30)
        self.shot_speed = 12
        self.lista_municion = []
        self.shot_timer = 0
        self.shot_interval = 20
        self.pasive = True
        self.pasive_time = 5
        self.seconds_of_life = 0
        self.lives = 1

        self.sound_on = True
        self.shot_sound = pygame.mixer.Sound("resources/sounds/shot_from_enemy.mp3")
        self.shot_on_player_sound = pygame.mixer.Sound("resources/sounds/shot_on_player.mp3")


    def move(self):
        '''
        The enemy moves in one direction until it reaches a range in which it changes direction.
        '''
        if self.l_o_r == "L":
            self.move_x = -self.speed
            self.animate = self.walk_l
            if self.rect.x == (self.start_x-100):
                self.l_o_r = "R"
                self.frame = 0

        elif self.l_o_r == "R":
            self.move_x = self.speed
            self.animate = self.walk_r
            if self.rect.x == (self.start_x+100):
                self.l_o_r = "L"
                self.frame = 0
            
    def shot(self,player):
        '''
        If the range rectangle collides with the player, the enemy fires in the player's direction.
        '''

        if not self.pasive and self.shot_timer ==0 :
            if self.range_rect_l.colliderect(player.rect):

                    if len(self.lista_municion)==0:
                        if self.sound_on:
                            self.shot_sound.play()
                        self.shot_timer = self.shot_interval
                        self.lista_municion.append(Proyectil(self.rect.x,self.rect.y,self.shot_speed,"L"))

            elif self.range_rect_r.colliderect(player.rect):

                    if len(self.lista_municion)==0:
                        if self.sound_on:
                            self.shot_sound.play()
                        self.shot_timer = self.shot_interval
                        self.lista_municion.append(Proyectil(self.rect.x,self.rect.y,self.shot_speed,"R"))

    def shot_timer_update(self):
        '''
        Shot cooldown timer.
        '''
        if self.shot_timer>0: 
            self.shot_timer-=1

    def update(self,player,lista_plataforma,sound_on):
        self.sound_on = sound_on
        self.shot_timer_update()

        if self.pasive: 
            self.seconds_of_life+=1
        if self.seconds_of_life== self.pasive_time:
            self.pasive=False

        for index,proyectil in enumerate(self.lista_municion):

            if proyectil.colision(player.rect):
                if self.sound_on:
                    self.shot_on_player_sound.play()
                self.lista_municion.pop(index)
                player.lives -=10
            elif proyectil.rect.x < 0 or proyectil.rect.x > ANCHO_VENTANA:
                self.lista_municion.pop(index)
            else:
                for block in lista_plataforma:
                    if proyectil.colision(block.rect):
                        self.lista_municion.pop(index)
            proyectil.update()

        self.range_rect_l.x +=self.move_x
        self.range_rect_r.x +=self.move_x
        self.rect.x += self.move_x

        self.frame += 1
        if self.frame == len(self.animate):
            self.frame = 0
        
    def draw(self,screen):
        '''
        Draw the character, his shots on the screen if he is alive. if debug is true it also draws its collision rectangles.
        '''
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.range_rect_r)
            pygame.draw.rect(screen,color=(0,250 ,0),rect=self.range_rect_l)
        for proyectil in self.lista_municion:
            proyectil.draw(screen)        
        if self.is_alive:
            self.image = self.animate[self.frame]
            screen.blit(self.image,self.rect)


class Runner(Enemy):
    def __init__(self, x, y, speed) -> None:
        super().__init__(x, y, speed)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/enemies/Run (36x30).png",12,1)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/enemies/Run (36x30).png",12,1,True)
        self.walk = True
        self.lives = 2
    
    def move(self):
        if self.walk:
            return super().move()

    def pursuit(self,player):
        '''
        If the range rectangle collides with the player, the enemy's direction changes to the player's direction.
        '''

        if self.range_rect_l.colliderect(player.rect):
            self.move_x = -self.speed
            self.animate = self.walk_l

        elif self.range_rect_r.colliderect(player.rect):
            self.move_x = self.speed
            self.animate = self.walk_r
        else:
            self.walk = True
        
        if self.rect.colliderect(player.rect):
            if self.sound_on:
                self.shot_on_player_sound.play()
            if self.is_alive:
                player.lives-=20
            self.is_alive = False

    def update(self,sound_on):

        self.sound_on = sound_on
        self.range_rect_l.x +=self.move_x
        self.range_rect_r.x +=self.move_x
        self.rect.x += self.move_x

        self.frame += 1
        if self.frame == len(self.animate):
            self.frame = 0
        