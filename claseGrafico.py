from PyQt4.QtGui import *
import pyqtgraph as pg

class ClaseGrafico(QWidget):
    def __init__(self, titulo, bins):
        super().__init__()
        self.grafico=pg.PlotWidget(title="Titulo uno")#titulo)
        self.widget.setWindowTitle("Titulo dos")
        self.rango = 8000
        self.muestras = 1024
        self.x_ = np.linspace(0,4000,1024)
        self.y_ = np.random.normal(loc=0.0,scale=2,size=1024)
        self.actualizar_grafico()

    def actualizar_grafico(self):
        self.grafico.plotItem.plot(x, y)
