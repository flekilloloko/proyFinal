import sys
import pyqtgraph as pg
import numpy as np
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class VentanaGraficos(QMainWindow):
    """this class creates a main window to observe the grouth of a simulation"""

   #constructor
    def __init__(self):
        super().__init__() #call super class constructor
        self.setWindowTitle("Marisoll y Pancha las amoooo <3") #set window title
        self.create_layout()

    def create_layout(self):
        
        self.widget = pg.PlotWidget(title="Some Plotting")
        self.widget2 = pg.PlotWidget(title="Some Plotting 2")
        self.widget.setWindowTitle("random Plotting")
        x = np.random.normal(loc=0.0,scale=2,size=100)
        self.widget.plotItem.plot(x)
        self.widget2.plotItem.plot(x)
        self.ordenador = QWidget()
        

        #create layout to hold the widgets
        self.initial_layout = QVBoxLayout()
        self.ordenador.setLayout(self.initial_layout)
        self.initial_layout.addWidget(self.widget)
        self.initial_layout.addWidget(self.widget2)
        
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
