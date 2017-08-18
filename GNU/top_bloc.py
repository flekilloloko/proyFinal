#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Bloc
# Generated: Wed Aug 16 21:13:20 2017
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import sip
import sys

from distutils.version import StrictVersion
class top_bloc(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Bloc")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Bloc")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_bloc")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.rango_l = rango_l = 24000
        self.range_h = range_h = 1

        ##################################################
        # Blocks
        ##################################################
        self._rango_l_layout = Qt.QVBoxLayout()
        self._rango_l_tool_bar = Qt.QToolBar(self)
        self._rango_l_layout.addWidget(self._rango_l_tool_bar)
        self._rango_l_tool_bar.addWidget(Qt.QLabel("rango_low"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._rango_l_counter = qwt_counter_pyslot()
        self._rango_l_counter.setRange(0, 24000, 100)
        self._rango_l_counter.setNumButtons(2)
        self._rango_l_counter.setValue(self.rango_l)
        self._rango_l_tool_bar.addWidget(self._rango_l_counter)
        self._rango_l_counter.valueChanged.connect(self.set_rango_l)
        self._rango_l_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._rango_l_slider.setRange(0, 24000, 100)
        self._rango_l_slider.setValue(self.rango_l)
        self._rango_l_slider.setMinimumWidth(200)
        self._rango_l_slider.valueChanged.connect(self.set_rango_l)
        self._rango_l_layout.addWidget(self._rango_l_slider)
        self.top_layout.addLayout(self._rango_l_layout)
        self._range_h_layout = Qt.QVBoxLayout()
        self._range_h_tool_bar = Qt.QToolBar(self)
        self._range_h_layout.addWidget(self._range_h_tool_bar)
        self._range_h_tool_bar.addWidget(Qt.QLabel("range_h"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._range_h_counter = qwt_counter_pyslot()
        self._range_h_counter.setRange(0, 24000, 100)
        self._range_h_counter.setNumButtons(2)
        self._range_h_counter.setValue(self.range_h)
        self._range_h_tool_bar.addWidget(self._range_h_counter)
        self._range_h_counter.valueChanged.connect(self.set_range_h)
        self._range_h_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._range_h_slider.setRange(0, 24000, 100)
        self._range_h_slider.setValue(self.range_h)
        self._range_h_slider.setMinimumWidth(0)
        self._range_h_slider.valueChanged.connect(self.set_range_h)
        self._range_h_layout.addWidget(self._range_h_slider)
        self.top_layout.addLayout(self._range_h_layout)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(True)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	12000, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, rango_l, 100, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, range_h, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/usr/share/sounds/alsa/Front_Center.wav", True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.05, ))
        self.audio_sink_0 = audio.sink(samp_rate, "hw", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.high_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_bloc")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(12000, self.samp_rate)
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.range_h, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.rango_l, 100, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)

    def get_rango_l(self):
        return self.rango_l

    def set_rango_l(self, rango_l):
        self.rango_l = rango_l
        Qt.QMetaObject.invokeMethod(self._rango_l_counter, "setValue", Qt.Q_ARG("double", self.rango_l))
        Qt.QMetaObject.invokeMethod(self._rango_l_slider, "setValue", Qt.Q_ARG("double", self.rango_l))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.rango_l, 100, firdes.WIN_HAMMING, 6.76))

    def get_range_h(self):
        return self.range_h

    def set_range_h(self, range_h):
        self.range_h = range_h
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.range_h, 100, firdes.WIN_HAMMING, 6.76))
        Qt.QMetaObject.invokeMethod(self._range_h_counter, "setValue", Qt.Q_ARG("double", self.range_h))
        Qt.QMetaObject.invokeMethod(self._range_h_slider, "setValue", Qt.Q_ARG("double", self.range_h))

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_bloc()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
