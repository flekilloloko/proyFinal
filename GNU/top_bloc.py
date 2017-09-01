#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Bloc
# Generated: Thu Aug 31 21:17:06 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

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
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class top_bloc(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Bloc")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Bloc")
        qtgui.util.check_set_qss()
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
        self.sig_graf = sig_graf = 0
        self.samp_rate = samp_rate = 44100
        self.salida_wav = salida_wav = 0
        self.rango_l = rango_l = 20000
        self.range_h = range_h = 1

        ##################################################
        # Blocks
        ##################################################
        self._sig_graf_options = (1, 0, )
        self._sig_graf_labels = ('Microfono', 'Instrumento', )
        self._sig_graf_group_box = Qt.QGroupBox('Mostrar Se\xc3\xb1al')
        self._sig_graf_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._sig_graf_button_group = variable_chooser_button_group()
        self._sig_graf_group_box.setLayout(self._sig_graf_box)
        for i, label in enumerate(self._sig_graf_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._sig_graf_box.addWidget(radio_button)
        	self._sig_graf_button_group.addButton(radio_button, i)
        self._sig_graf_callback = lambda i: Qt.QMetaObject.invokeMethod(self._sig_graf_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._sig_graf_options.index(i)))
        self._sig_graf_callback(self.sig_graf)
        self._sig_graf_button_group.buttonClicked[int].connect(
        	lambda i: self.set_sig_graf(self._sig_graf_options[i]))
        self.top_layout.addWidget(self._sig_graf_group_box)
        self._salida_wav_options = (1, 0, )
        self._salida_wav_labels = ('Mute', 'Salida ON', )
        self._salida_wav_group_box = Qt.QGroupBox("salida_wav")
        self._salida_wav_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._salida_wav_button_group = variable_chooser_button_group()
        self._salida_wav_group_box.setLayout(self._salida_wav_box)
        for i, label in enumerate(self._salida_wav_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._salida_wav_box.addWidget(radio_button)
        	self._salida_wav_button_group.addButton(radio_button, i)
        self._salida_wav_callback = lambda i: Qt.QMetaObject.invokeMethod(self._salida_wav_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._salida_wav_options.index(i)))
        self._salida_wav_callback(self.salida_wav)
        self._salida_wav_button_group.buttonClicked[int].connect(
        	lambda i: self.set_salida_wav(self._salida_wav_options[i]))
        self.top_layout.addWidget(self._salida_wav_group_box)
        self._rango_l_range = Range(0, 20000, 100, 20000, 200)
        self._rango_l_win = RangeWidget(self._rango_l_range, self.set_rango_l, 'rango_low', "counter_slider", float)
        self.top_layout.addWidget(self._rango_l_win)
        self._range_h_range = Range(0, 20000, 100, 1, 200)
        self._range_h_win = RangeWidget(self._range_h_range, self.set_range_h, "range_h", "counter_slider", float)
        self.top_layout.addWidget(self._range_h_win)
        self.qtgui_sink_x_0 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, rango_l, 1000, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, range_h, 1000, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/root/Desktop/04_-_Caigu_.wav', True)
        self.blocks_mute_xx_0 = blocks.mute_ff(bool(salida_wav))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((0.05, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.05, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=sig_graf,
        	output_index=0,
        )
        self.audio_source_1 = audio.source(samp_rate, 'hw:0,0', True)
        self.audio_source_0 = audio.source(samp_rate, 'hw:1,0', True)
        self.audio_sink_0 = audio.sink(samp_rate, 'hw:2,0', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.audio_source_1, 0), (self.blks2_selector_0, 1))
        self.connect((self.blks2_selector_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_mute_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_mute_xx_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.high_pass_filter_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_bloc")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sig_graf(self):
        return self.sig_graf

    def set_sig_graf(self, sig_graf):
        self.sig_graf = sig_graf
        self._sig_graf_callback(self.sig_graf)
        self.blks2_selector_0.set_input_index(int(self.sig_graf))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.rango_l, 1000, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.range_h, 1000, firdes.WIN_HAMMING, 6.76))

    def get_salida_wav(self):
        return self.salida_wav

    def set_salida_wav(self, salida_wav):
        self.salida_wav = salida_wav
        self._salida_wav_callback(self.salida_wav)
        self.blocks_mute_xx_0.set_mute(bool(self.salida_wav))

    def get_rango_l(self):
        return self.rango_l

    def set_rango_l(self, rango_l):
        self.rango_l = rango_l
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.rango_l, 1000, firdes.WIN_HAMMING, 6.76))

    def get_range_h(self):
        return self.range_h

    def set_range_h(self, range_h):
        self.range_h = range_h
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.range_h, 1000, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_bloc, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
