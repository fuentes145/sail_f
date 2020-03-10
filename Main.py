from PyQt5.QtWidgets import QApplication
from front import Regata
from menu import Menu
import sys



if __name__ == '__main__':
    app = QApplication([])
    menu = Menu()
    menu.show()
    # regata = Regata()
    # regata.show()
    sys.exit(app.exec_())
