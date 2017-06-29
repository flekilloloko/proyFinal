import sys
import pyqtgraph as pg
import numpy as np
import widgetGrafico
from PyQt4.QtCore import *  # QtCore import *
from PyQt4.QtGui import *


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Análisis de espectro")
        self.crear_layout()

    def crear_layout(self):
        self.espectroTotal = widgetGrafico.ClaseGrafico("Espectro Total")

        self.sectoresPantalla = QVBoxLayout()
        self.espacio = QWidget()
        self.sectoresPantalla.addWidget(self.espectroTotal)
        self.espacio.setLayout(self.sectoresPantalla)

        self.setCentralWidget(self.espacio)
        timer = QTimer(self)
        timer.timeout.connect(self.proximo_frame)
        timer.start(50)

    def proximo_frame(self):
        data = np.random.normal(loc=0.0, scale=2, size=1024)
        self.espectroTotal.actualizar_grafico(data, 1000, 1608)

        # proximo_frame()


def main():
    simulacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    ventana.raise_()
    simulacion.exec()  # lint:ok

if __name__ == "__main__":
    main()
