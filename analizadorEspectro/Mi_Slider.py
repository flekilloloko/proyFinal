from pyqtgraph.Qt import QtGui, QtCore

FREC_MAX = 4000


class Mi_Slider(QtGui.QWidget):

    def __init__(self):
        super().__init__()

        self.sliderFpb = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.sliderFpa = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.label_Fpb = QtGui.QLabel("4000")
        self.label_nombreFpb = QtGui.QLabel("F. Pasa Bajos [Hz]")
        self.label_Fpb.setFixedWidth(60)
        self.label_Fpa = QtGui.QLabel("0")
        self.label_nombreFpa = QtGui.QLabel("F. Pasa Altos  [Hz]")
        self.label_Fpa.setFixedWidth(60)
        self.lay_sliderFpb = QtGui.QHBoxLayout()
        self.lay_sliderFpa = QtGui.QHBoxLayout()
        self.lay_sliderFpb.addWidget(self.label_nombreFpb)
        self.lay_sliderFpb.addWidget(self.sliderFpb)
        self.lay_sliderFpb.addWidget(self.label_Fpb)
        self.lay_sliderFpa.addWidget(self.label_nombreFpa)
        self.lay_sliderFpa.addWidget(self.sliderFpa)
        self.lay_sliderFpa.addWidget(self.label_Fpa)
        self.visualizacion()

    def visualizacion(self):
        if self.sliderFpa.isVisible():
            self.sliderFpa.hide()
            self.sliderFpb.hide()
            self.label_Fpa.hide()
            self.label_Fpb.hide()
            self.label_nombreFpa.hide()
            self.label_nombreFpb.hide()
        else:
            self.sliderFpa.show()
            self.sliderFpb.show()
            self.label_Fpa.show()
            self.label_Fpb.show()
            self.label_nombreFpa.show()
            self.label_nombreFpb.show()