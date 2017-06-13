import sys
import pyqtgraph as pg
import numpy as np
import widgetGrafico
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Análisis de espectro")
        self.crear_layout()

    def crear_layout(self):
        self.espectroTotal = widgetGrafico.ClaseGrafico('Espectro Total')
        self.sectoresPantalla = QVBoxLayout()
        self.espacio = QWidget()
        self.sectoresPantalla.addWidget(self.espectroTotal)
        self.espacio.setLayout(self.sectoresPantalla)

        self.setCentralWidget(self.espacio)

def main():
    simulacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    ventana.raise_()
    simulacion.exec()

if __name__ == "__main__":
    main()