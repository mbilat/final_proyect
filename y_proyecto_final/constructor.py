import pygame
from auxiliar import*
from player import *
from plataforma import *
from ladder import *
from objetos import *

class Level:
   def __init__(self) -> None:
        self.ruta = "y_proyecto_final/resources/level1.json"
        self.lvl = "lvl_1"
        self.wallpaper =  pygame.image.load("C:/Users/bilix/OneDrive/Escritorio/final_proyect/y_proyecto_final/resources/all.png")
        self.wallpaper = pygame.transform.scale(self.wallpaper,(ANCHO_VENTANA,ALTO_VENTANA))
        self.new_game = True
        self.is_running = True
        self.data = Auxiliar.cargar_json(self.ruta,self.lvl)
        self.player_1 = None
        self.time_keys = 0
        self.list_platforms = []
        self.ladder_list = []
        self.list_enemy = []
        self.list_enemy_spawn  = []
        self.list_bonus = []
        self.list_bonus_spawn = []
        self.list_runner = []
        self.list_runner_spawn = []
        self.list_keys = []
        self.list_keys_spawn = []
        self.portal = None
        self.music = pygame.mixer.Sound("y_proyecto_final/resources/passionfruit.mp3")
        self.music_on = True
        self.minutes = 0
        self.seconds = 0

   def init_level(self):        
        for i in self.data:
            if i["type"] == "player":
                self.player_1 = Player(i["x"],i["y"],i["w"],i["h"],i["speed_walk"],i["speed_run"],i["jump_power"],i["frame_rate_ms"],i["move_rate_ms"])
            elif i["type"] == "runner_spawn":
                self.list_runner_spawn = i["list_spawn"]
            
            elif i["type"] == "enemy_1_spawn":
                self.list_enemy_spawn = i["list_spawn"]

            elif i["type"] == "bonus_spawn":
                self.list_bonus_spawn = i["list_spawn"]

            elif i["type"] == "ladder_list":
                for e in i["list_spawn"]:
                    self.ladder_list.append(Ladder(e["x"],e["y"],e["w"],e["h"]))

            elif i["type"] == "platform_list":
                for e in i["list_spawn"]:
                    self.list_platforms.append(Plataforma(e["x"],e["y"],e["w"],e["h"]))

            elif i["type"] == "keys_spawn":
                self.list_keys_spawn = i["list_spawn"]

            elif i["type"] == "portal":
                self.portal = Portal(i["x"],i["y"],i["w"],i["h"])
            
            elif i["type"] == "music":
                if i["on"] == "True":
                    self.music_on = True
                else: 
                    self.music_on = False
                  
            pygame.mixer.init()
            pygame.mixer.music.set_volume(1.0)


