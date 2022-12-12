import pygame
import json
import sqlite3

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False, step = 1,scale=1):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        fotograma_ancho_scaled = int(fotograma_ancho*scale)
        fotograma_alto_scaled = int(fotograma_alto*scale)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(scale != 1):
                    
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
                lista.append(surface_fotograma)
        return lista

    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(1,quantity+1):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista

    def cargar_json(ruta:str,lvl)->list[dict]:
        '''
        Extracts the information from a .json and returns it as a list of dictionaries.
        '''
        data = []
        with open(ruta,"r") as archivo:
            data = json.load(archivo)
            data = list[dict](data[lvl])
            return data


    def list_draw(list,screen):
        '''
        Loops through a list of objects and draws them on the screen.
        '''
        for x in list:
            x.draw(screen)

    def upload_sql():
        '''
        Create a sql file with a scoreboard.
        '''

        with sqlite3.connect("scores.db") as conexion:
            try:
                sentencia = ''' create table scores
                                (
                                        id integer primary key autoincrement,
                                        player text,
                                        score real
                                )
                            '''
                conexion.execute(sentencia)
                print("the scoreboard list was created.")                       
            except sqlite3.OperationalError:
                print("The scoreboard already exists.")  


    def edit_sql(player):
        '''
        Inserts a new entry in the file, if it is not possible returns "error" by console.
        '''
        with sqlite3.connect("scores.db") as conexion:
            try:
                conexion.execute("insert into scores(player,score) values (?,?)", player)
                conexion.commit()
            except:
                print("Error")

    def get_scores_sql()->list:
        '''
        Extracts the 3 best scores from the file and return a list with these.
        '''

        top_three = []
        with sqlite3.connect("scores.db") as conexion:
            cursor = conexion.execute("select player,score from scores order by score limit 3")
            for fila in cursor:
                name = fila[0]
                score = fila[1]
                top_three.append(name)
                top_three.append(score)
        return top_three
