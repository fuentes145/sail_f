from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton
from front import Regata

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)
        self.main_game_button = QPushButton('Jugar', self)
        self.main_game_button.clicked.connect(self.partir_regata)
        #self.partir_regata()# sacar esta linea para que se abra el menu !!!!!!!!!!!!!!!!

    def partir_regata(self):
        self.hide()
        regata = Regata()# dentro del parentesis se pueden entregar especificaciones de como
        # va a ser la regata que se instancia
        regata.show()

