import pygame



class Proyectil:
    def __init__(self,x,y,speed,direccion) -> None:
        self.image = pygame.image.load("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/player1/Spiked Ball.png")
        self.image = pygame.transform.scale(self.image,(10,10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.move_x = 0
        self.move_y = 0
        self.direccion = direccion

    def update(self):

        if self.direccion == "L":
            self.move_x = -self.speed
        else:
            self.move_x = self.speed
        self.rect.x += self.move_x

    def colision(self,objeto)->bool:
        if self.rect.colliderect(objeto):
            return True

    def draw(self,screen):
        screen.blit(self.image,self.rect)