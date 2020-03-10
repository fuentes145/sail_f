from PyQt5.QtCore import QObject
import random
import threading
import time


class Bote(QObject): 

    def __init__(self, front):
        super().__init__()
        self.front = front
        self.N = 4
        self.viento = Viento(self)
        self.direction = "U"
        self.x = 700
        self.y = 600
        self.apretadas = []

    def update_boat(self):
        self.mover(self.apretadas)

    def teclas(self, apretadas):
        self.apretadas = apretadas

    def mover(self, press):

        if len(press) == 1:
            event= press[0]
            if event == 'R':
                self.direction = 'R'
                self.x += self.N/2
            elif event == 'L':
                self.direction = 'L'
                self.x -= self.N/2
            elif event == 'U':
                self.direction = 'U'
                
            elif event == 'D':
                self.direction = 'D'
                self.y += self.N/2
        
        if len(press) == 2:
            event= press[0] + press[1]

            if event == 'RU' or event == 'UR':
                self.direction = 'RU'
                self.x += self.viento.direccion_x
                self.y -= self.viento.direccion_y

            elif event == 'LU' or event == 'UL':
                self.direction = 'LU'
                self.x -= self.viento.direccion_x
                self.y -= self.viento.direccion_y
            
            elif event == 'RD' or event == 'DR':
                self.direction = 'RD'
                self.x += self.viento.direccion_x
                self.y += self.viento.direccion_y
        
            elif event == 'DL' or event == 'LD':
                self.direction = 'LD'
                self.x -= self.viento.direccion_x
                self.y += self.viento.direccion_y

class Boya(QObject):
    def __init__(self, front):
        super().__init__()
        self.front = front

class Viento(QObject): #poner como el viento en general en toda la canch con una flecha
    def __init__(self, bote):
        super().__init__()
        self.bote = bote
        self.direccion_x = self.bote.N /2
        self.direccion_y = self.bote.N /2
        #self.borneo()

    def borneo(self):
        
        b = random.randint(-4, 4)
        self.direccion_x += b 
        self.direccion_y += b       






