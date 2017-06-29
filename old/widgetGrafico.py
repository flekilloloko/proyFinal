from PyQt4.QtGui import *
import pyqtgraph as pg
import numpy as np
# from PyQt4 import QtCore
from PyQt4.QtCore import *


class ClaseGrafico(QWidget):
    def __init__(self, titulo):  # , bins):
        super().__init__()
        #no funca   self.grafico.setWindowTitle("Titulo dos")
        self.grafico = pg.PlotWidget(title=titulo)
        self.rango = 8000
        self.muestras = 1024
        #
        self.y_ = np.random.normal(loc=0.0, scale=2, size=1024)
        # self.actualizar_grafico(1000, 1618)
        self.layout_principal = QVBoxLayout()

        self.setLayout(self.layout_principal)
        self.x_ = np.linspace(0, 4000, 1024)
        # self.fpa = 2000
        # self.fpb = 4000

        self.layout_principal.addWidget(self.grafico)

    def actualizar_grafico(self, data, fpa, fpb):
        lineaPaAl = self.grafico.plotItem.addLine(x=fpa)
        lineaPaBa = self.grafico.plotItem.addLine(x=fpb)
        lineaPaAl.setPen(pg.mkPen((0, 0, 255), width=4, style=Qt.DotLine))
        lineaPaBa.setPen(pg.mkPen((255, 0, 0), width=4, style=Qt.DotLine))
        self.grafico.plotItem.plot(self.x_, data)
