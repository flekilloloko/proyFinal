#!/usr/bin/python

# import pyaudio
import struct
import math
import sys
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
        # self.app.quitOnLastWindowClosed()

        self.mainWindow = QtGui.QMainWindow()
        self.mainWindow.setWindowTitle("Spectrum Analyzer")
        self.mainWindow.resize(800, 300)
        self.centralWid = QtGui.QWidget()
        self.mainWindow.setCentralWidget(self.centralWid)
        self.lay = QtGui.QVBoxLayout()
        self.centralWid.setLayout(self.lay)

        self.specWid = pg.PlotWidget(name="spectrum")
        self.specItem = self.specWid.getPlotItem()
        self.specItem.setMouseEnabled(y=False)
        self.specItem.setYRange(0, 5)
        self.specItem.setXRange(0, RANGE, padding=0)

        self.specAxis = self.specItem.getAxis("bottom")
        self.specAxis.setLabel("Frequency [Hz]")
        self.lay.addWidget(self.specWid)

        self.mainWindow.show()
        self.app.aboutToQuit.connect(self.close)

    def close(self):
        # self.stream.close()
        sys.exit()

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

        self.specItem.plot(x=x, y=data, clear=True)


ads = AnalizadorDeEspectro()
ads.mainLoop()


if __name__ == '__main__':
    timer = QtCore.QTimer()
    timer.timeout.connect(ads.mainLoop)
    timer.start(10)
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