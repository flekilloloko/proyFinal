import sys
import pyqtgraph as pg
import numpy as np
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class VentanaGraficos(QMainWindow):
    """this class creates a main window to observe the grouth of a simulation"""
    #marca_frec
   #constructor
    def __init__(self):
        super().__init__() #call super class constructor
        self.setWindowTitle("Marisoll y Pancha las amoooo <3") #set window title
        self.create_layout()
        self.actFiltroPA(10)

    def actFiltroPA(self,frecu):
        global marca_frec
        #marca_frec.setData(frecu)

    def create_layout(self):
        global marca_frec        
        self.widget = pg.PlotWidget(title="Some Plotting")
        self.widget2 = pg.PlotWidget(title="Some Plotting 2")
        self.widget.setWindowTitle("random Plotting")
        y = np.linspace( 0, 4000, 100 )
        x = np.random.normal(loc=0.0,scale=2,size=100)
        self.widget.plotItem.plot(y,x)
        x = np.random.normal(loc=0.0,scale=2,size=100)
        self.widget.plotItem.plot(np.random.normal(size=100), pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')
        x = np.random.normal(loc=0.0,scale=2,size=100)
        self.widget2.plotItem.plot(x)
        marca_frec = self.widget2.plotItem.addLine(x=25)
        self.ordenador = QWidget()
        

        
	
        #create layout to hold the widgets
        self.initial_layout = QVBoxLayout()
        self.botonera = QHBoxLayout()
        self.cambiarPar= QPushButton("Comandos")
        self.resetearVista = QPushButton("Vistas Reset")
        self.botonera.addWidget(self.cambiarPar)
        self.botonera.addWidget(self.resetearVista)
        self.ordenador.setLayout(self.initial_layout)
        self.initial_layout.addWidget(self.widget)
        self.initial_layout.addWidget(self.widget2)
        self.initial_layout.addLayout(self.botonera)
        
        self.setCentralWidget(self.ordenador)
       
        #self.initial_layout.addWidget(self.widget2)

        
        #self.instantiate_button.clicked.connect(self.instantiate_crop)

    
       
def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = VentanaGraficos() #create new instance of main window
    crop_window.show() #make instance visible
    crop_window.raise_() #raise instance to top of window stack
    crop_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
