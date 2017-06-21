#!/usr/bin/python

# import pyaudio
import struct
import math
import sys
from mi_slider_class import *
import numpy as np
# import IPython as ipy

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore

# Audio Format (check Audio MIDI Setup if on Mac)
# FORMAT = pyaudio.paInt16
RATE = 44100
CHANNELS = 2

# Set Plot Range [-RANGE,RANGE], default is nyquist/2
RANGE = 4000  # None
if not RANGE:
    RANGE = RATE / 2

# Set these parameters (How much data to plot per FFT)
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE * INPUT_BLOCK_TIME)

# Which Channel? (L or R)
LR = "l"


class AnalizadorDeEspectro(object):
    def __init__(self):
        # self.pa = pyaudio.PyAudio()
        # self.initMicrophone()
        self.initUI()

    def initUI(self):
        self.app = QtGui.QApplication(sys.argv)
        self.app.quitOnLastWindowClosed()

        self.mainWindow = QtGui.QMainWindow()
        self.mainWindow.setWindowTitle("Spectrum Analyzer")
        self.mainWindow.resize(1000, 1000)
        self.centralWid = QtGui.QWidget()
        self.mainWindow.setCentralWidget(self.centralWid)
        # self.lay_h = QtGui.QHBoxLayout()
        self.lay_v = QtGui.QVBoxLayout()
        # self.lay_h.addLayout(self.lay_v)
        self.centralWid.setLayout(self.lay_v)

        self.espec1 = pg.PlotWidget(name="eTotal", title="Espectro Total")
        self.especTotal = self.espec1.getPlotItem()
        self.especTotal.setMouseEnabled(y=False)
        self.especTotal.setYRange(0, 5)
        self.especTotal.setXRange(0, RANGE, padding=0)
        self.lay_espec_t = QtGui.QVBoxLayout()
        self.lay_espec_t.addWidget(self.espec1)

        self.espec2 = pg.PlotWidget(name="eIndiv", title="Espectro Individual")
        self.especIndiv = self.espec2.getPlotItem()
        self.especIndiv.setMouseEnabled(y=False)
        self.especIndiv.setYRange(0, 5)
        self.especIndiv.setXRange(0, RANGE, padding=0)
        # self.lay_espec_i = QtGui.QVBoxLayout()
        # self.lay_espec_i.addWidget(self.espec2)

        self.ejeX = self.especTotal.getAxis("bottom")
        self.ejeX.setLabel("Frequencia [Hz]")

        self.botonera_layout = QtGui.QHBoxLayout()
        self.reset_zoom_btn = QtGui.QPushButton("Resetear Zooms")
        self.param_btn = QtGui.QPushButton("Setear Parametros")
        self.fil_btn = QtGui.QPushButton("Frecuencias Filtros")
        self.botonera_layout.addWidget(self.reset_zoom_btn)
        self.botonera_layout.addWidget(self.param_btn)
        self.botonera_layout.addWidget(self.fil_btn)

        self.lay_v.addLayout(self.lay_espec_t)
        self.lay_v.addWidget(self.espec2)
        self.lay_v.addLayout(self.botonera_layout)

        self.mainWindow.show()
        self.app.aboutToQuit.connect(self.close)

        self.graf_componentes_t = self.especTotal.plot()
        self.graf_lineaPa = pg.InfiniteLine(movable=True, angle=90, pos=0)
        self.graf_lineaPb = pg.InfiniteLine(movable=True, angle=90, pos=4000)
        self.especTotal.addItem(self.graf_lineaPa)
        self.especTotal.addItem(self.graf_lineaPb)

        # self.graf_lineaPb = self.especTotal.addLine(x=4000)
        # self.graf_lineaPa = self.especTotal.addLine(x=0)

        self.ctrolFrec = Mi_Slider()
        self.lay_espec_t.addWidget(self.ctrolFrec)

        self.fil_btn.clicked.connect(self.ctrolFrec.visualizacion)
        # self.connect(self.ctrolFrec, QtCore.SIGNAL("frec_cambio()"),
                        # self.actualizar_graf_fil)
        self.ctrolFrec.sliderFpb.valueChanged.connect(self.filtrosActSli)
        self.ctrolFrec.sliderFpa.valueChanged.connect(self.filtrosActSli)
        self.graf_lineaPa.sigPositionChanged.connect(self.filtrosActLin)
        self.graf_lineaPb.sigPositionChanged.connect(self.filtrosActLin)

    def actualizar_graf_fil(self):
        self.graf_lineaPb = self.especTotal.addLine(
                                            x=self.ctrolFrec.sliderFpa.value())
        self.graf_lineaPa = self.especTotal.addLine(
                                            x=self.sliderFpa.tickPosition)
        self.label_Fpa = self.sliderFpa.tickPosition
        self.label_Fpb = self.sliderFpb.tickPosition

    def close(self):
        # self.stream.close()
        sys.exit()

    def mostrar_sliders(self):
        if self.sliderFpa.isVisible():
            self.sliderFpa.hide()
            self.sliderFpb.hide()
            self.label_Fpa.hide()
            self.label_Fpb.hide()
            self.label_nombreFpa.hide()
            self.label_nombreFpb.hide()

            # timerF.stop()
        else:
            self.sliderFpa.show()
            self.sliderFpb.show()
            self.label_Fpa.show()
            self.label_Fpb.show()
            self.label_nombreFpa.show()
            self.label_nombreFpb.show()

            # timerF.start(100)

    def filtrosActLin(self):
        self.ctrolFrec.sliderFpa.setValue(self.graf_lineaPa.value())
        self.ctrolFrec.sliderFpb.setValue(self.graf_lineaPb.value())

    def filtrosActSli(self):
        self.Fpa = self.ctrolFrec.sliderFpa.value()
        self.Fpb = self.ctrolFrec.sliderFpb.value()
        self.graf_lineaPb.setValue(self.Fpb)
        self.graf_lineaPa.setValue(self.Fpa)
        self.ctrolFrec.label_Fpb.setText(str(self.Fpb))
        self.ctrolFrec.label_Fpa.setText(str(self.Fpa))

    def mainLoop(self):
        # Sometimes Input overflowed because of mouse events, ignore this
        try:
            # data = self.readData()
            pass
        except IOError:
            pass
        # f, Pxx = self.get_spectrum(data)
        x = np.linspace(0, 4000, 1024)
        data = np.random.normal(loc=0.0, scale=2, size=1024)

        self.graf_componentes_t.setData(x, data)


ads = AnalizadorDeEspectro()
ads.mainLoop()


if __name__ == '__main__':
    timer = QtCore.QTimer()
    timer.timeout.connect(ads.mainLoop)
    timer.start(10)

    # timerF = QtCore.QTimer()
    # timerF.timeout.connect(ads.filtrosAct)
    QtGui.QApplication.instance().exec_()

"""
    def find_input_device(self):
        device_index = None
        for i in range(self.pa.get_device_count()):
            devinfo = self.pa.get_device_info_by_index(i)
            if devinfo["name"].lower() in ["mic","input"]:
                device_index = i

        return device_index

    def initMicrophone(self):
        device_index = self.find_input_device()

        self.stream = self.pa.open(    format = FORMAT,
                                    channels = CHANNELS,
                                    rate = RATE,
                                    input = True,
                                    input_device_index = device_index,
                                    frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

    def readData(self):
        block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
        count = len(block)/2
        format = "%dh"%(count)
        shorts = struct.unpack( format, block )
        if CHANNELS == 1:
            return np.array(shorts)
        else:
            l = shorts[::2]
            r = shorts[1::2]
            if LR == 'l':
                return np.array(l)
            else:
                return np.array(r)"""

"""def get_spectrum(self, data):
        T = 1.0/RATE
        N = data.shape[0]
        Pxx = (1./N)*np.fft.fft(data)
        f = np.fft.fftfreq(N,T)
        Pxx = np.fft.fftshift(Pxx)
        f = np.fft.fftshift(f)

        return f.tolist(), (np.absolute(Pxx)).tolist()
"""