from pyqtgraph.Qt import QtGui, QtCore
# from PyQt5.QtCore import pyqtsignal

FREC_MAX = 4000
INTERVALO = 10


class Mi_Slider(QtGui.QWidget):

    def __init__(self):
        super(Mi_Slider, self).__init__()

        self.frec_cambio = QtCore.Signal()
        self.sliderFpb = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.sliderFpa = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.label_Fpb = QtGui.QLabel("4000")
        self.label_nombreFpb = QtGui.QLabel("F. Pasa Bajos [Hz]: ")
        self.label_Fpb.setFixedWidth(60)
        self.label_Fpa = QtGui.QLabel("0")
        self.label_nombreFpa = QtGui.QLabel("F. Pasa Altos  [Hz]: ")
        self.label_Fpa.setFixedWidth(60)
        self.layout_gral = QtGui.QVBoxLayout()
        self.lay_sliderFpb = QtGui.QHBoxLayout()
        self.lay_sliderFpa = QtGui.QHBoxLayout()
        self.layout_gral.addLayout(self.lay_sliderFpb)
        self.layout_gral.addLayout(self.lay_sliderFpa)

        self.sliderFpa.setMinimum(0)
        self.sliderFpa.setMaximum(FREC_MAX)
        self.sliderFpa.setValue(0)
        self.sliderFpa.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sliderFpa.setTickInterval(INTERVALO)
        self.sliderFpb.setMinimum(0)
        self.sliderFpb.setMaximum(FREC_MAX)
        self.sliderFpb.setValue(4000)
        self.sliderFpb.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sliderFpb.setTickInterval(INTERVALO)

        self.setLayout(self.layout_gral)
        self.lay_sliderFpb.addWidget(self.label_nombreFpb)
        self.lay_sliderFpb.addWidget(self.label_Fpb)
        self.lay_sliderFpb.addWidget(self.sliderFpb)
        self.lay_sliderFpa.addWidget(self.label_nombreFpa)
        self.lay_sliderFpa.addWidget(self.label_Fpa)
        self.lay_sliderFpa.addWidget(self.sliderFpa)

        # self.sliderFpa.valueChanged.connect(self.cambio)
        # self.sliderFpb.valueChanged.connect(self.cambio)

        self.sliderFpa.hide()
        self.sliderFpb.hide()
        self.label_Fpa.hide()
        self.label_Fpb.hide()
        self.label_nombreFpa.hide()
        self.label_nombreFpb.hide()

    # def cambio(self):
        # self.frec_cambio.emit()

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