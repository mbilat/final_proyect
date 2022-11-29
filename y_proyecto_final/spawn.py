import pygame
import random
from enemigo import *
from objetos import *

class Spawn:
    def enemy(enemy_list,ubi_list,len_lista,enemy_type,speed=5):
        pos =random.randint(0,(len_lista-1))
        x = ubi_list[pos]["x"]
        y = ubi_list[pos]["y"]
        enemy_list.append(enemy_type(x,y,speed))

    def bonus(bonus_list,ubi_list,len_lista):
        pos =random.randint(0,(len_lista-1))
        x = ubi_list[pos]["x"]
        y = ubi_list[pos]["y"]
        bonus_list.append(Bonus(x,y,50,50))
    
    def keys(key_list,key_ubi_list,len_lista):
        pos =random.randint(0,(len_lista-1))
        x = key_ubi_list[pos]["x"]
        y = key_ubi_list[pos]["y"]
        key_list.append(Flag(x,y,50,50))