from PyQt5.QtGui import *
import pyqtgraph as pg
import numpy as np
from PyQt5.QtCore import *


class ClaseGrafico(QWidget):
    def __init__(self, titulo):  # , bins):
        super().__init__()
        self.grafico = pg.PlotWidget(title=titulo)
        #no funca   self.grafico.setWindowTitle("Titulo dos")
        self.rango = 8000
        self.muestras = 1024
        self.x_ = np.linspace(0, 4000, 1024)
        self.y_ = np.random.normal(loc=0.0, scale=2, size=1024)
        self.actualizar_grafico(1000, 1618)
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.grafico)
        self.setLayout(self.layout_principal)

    def actualizar_grafico(self, fpa, fpb):
        lineaPaAl = self.grafico.plotItem.addLine(x=fpa)
        lineaPaBa = self.grafico.plotItem.addLine(x=fpb)
        lineaPaAl.setPen(pg.mkPen((0, 0, 255), width=4, style=Qt.DotLine))
        lineaPaBa.setPen(pg.mkPen((255, 0, 0), width=4, style=Qt.DotLine))
        self.grafico.plotItem.addLine(x=fpb)
        self.grafico.plotItem.plot(self.x_, self.y_)


def main():
    nuevo_grafico = ClaseGrafico("jeje")  # lint:ok


if __name__ == "__main__":
    main()
