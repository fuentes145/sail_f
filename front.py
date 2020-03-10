from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from os import path
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from back import Bote
import funciones


class Regata(QWidget):
    senal_update_boat = pyqtSignal(list)

    def __init__(self):
        super().__init__()

        self.bote = Bote(self)
        self.press = []
        self.init_gui()
        self.connect_signals()
        self.tiempo()

    def cronometro(self):
        self.timerc = QTimer(self)
        self.timerc.start(1000) # update every (x) mili second
        self.x = 5
        self.crono = QLabel(self) 
        self.crono.setGeometry(800,100,150,150)
        self.timerc.timeout.connect(self.actualizar_cronometro)

    def actualizar_cronometro(self):
        self.crono.setText(str(self.x))
        self.x -=1
        if self.x == -1:
            self.crono.hide()
            self.timerc.stop()
            self.pasados()




    def tiempo(self):
        timer = QTimer(self)
        timer.start(30) # update every (x) mili second
        timer.timeout.connect(self.acualizar_frame)
        timer.timeout.connect(self.bote.update_boat)

    def pasados(self):
        if self.bote.y < self.coordenadas["boya_1"][1]:
            self.pasado.setText("devuelvete gil qlao, te pasaste")

    def acualizar_frame(self):
        if self.bote.direction == 'D':
            self.anterior
            self.bote.direction = self.anterior+"D"
            self.imagen_bote.setPixmap(QPixmap(path.join('sprites', self.bote.direction+".jpg")))

        if self.bote.direction == 'L' or self.bote.direction == 'R':
            self.anterior = self.bote.direction[0]
            self.imagen_bote.setPixmap(QPixmap(path.join('sprites', self.bote.direction+".jpg")))
            self.imagen_bote.setGeometry(self.bote.x, self.bote.y, 60, 30)
            
        else: 
            self.anterior = self.bote.direction[0]
            self.imagen_bote.setPixmap(QPixmap(path.join('sprites', self.bote.direction+".jpg")))
            self.imagen_bote.setGeometry(self.bote.x, self.bote.y, 30, 60)



    def init_gui(self):
        self.setGeometry(0, 0, 1300, 1500)
        self.fondo = QLabel(self)
        pixeles = QPixmap(path.join("sprites", "fondo"))
        self.fondo.setPixmap(pixeles)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 1300, 1500)
        self.imagen_bote = QLabel(self)
        self.current_sprite = QPixmap(path.join('sprites', 'U.jpg'))
        self.imagen_bote.setPixmap(self.current_sprite)
        self.imagen_bote.setGeometry(600, 550, 30, 60)
        self.imagen_bote.setScaledContents(True)
        self.crear_cancha()
        self.cronometro()
        self.pasado = QLabel(self) 
        self.pasado.setGeometry(50, 50, 300, 50)
        



    def crear_cancha(self):
        self.coordenadas = { "boya_1": [700, 500], "boya_2": [400, 500], "boya_3": [550, 90], "boya_4": [220,130]}

        self.boya_1 = QLabel(self)
        self.imagen_boya = QPixmap(path.join( 'sprites', 'boya.png'))
        self.boya_1.setPixmap(self.imagen_boya)
        self.boya_1.setGeometry(self.coordenadas["boya_1"][0], self.coordenadas["boya_1"][1], 20, 20)
        self.boya_1.setScaledContents(True)

        self.boya_2 = QLabel(self)
        self.boya_2.setPixmap(self.imagen_boya)
        self.boya_2.setGeometry( self.coordenadas["boya_2"][0], self.coordenadas["boya_2"][1], 20, 20)
        self.boya_2.setScaledContents(True)

        self.boya_3 = QLabel(self)
        self.boya_3.setPixmap(self.imagen_boya)
        self.boya_3.setGeometry(self.coordenadas["boya_3"][0], self.coordenadas["boya_3"][1], 20, 20)
        self.boya_3.setScaledContents(True)

        self.boya_4 = QLabel(self)
        self.boya_4.setPixmap(self.imagen_boya)
        self.boya_4.setGeometry(self.coordenadas["boya_4"][0], self.coordenadas["boya_4"][1], 20, 20)
        self.boya_4.setScaledContents(True)


    def connect_signals(self):
        self.senal_update_boat.connect(self.bote.teclas)


    key_event_dict = {
        Qt.Key_W: 'U',
        Qt.Key_S: 'D',
        Qt.Key_D: 'R',
        Qt.Key_A: 'L'
    }


    def keyPressEvent(self, event):
        if event.key() in self.key_event_dict:
            if self.key_event_dict[event.key()] not in self.press:
                self.press.append(self.key_event_dict[event.key()])
                self.senal_update_boat.emit(self.press)
   

    def keyReleaseEvent(self, event):
        if event.key() in self.key_event_dict:
            self.press.remove(self.key_event_dict[event.key()])
            self.senal_update_boat.emit(self.press)






    

