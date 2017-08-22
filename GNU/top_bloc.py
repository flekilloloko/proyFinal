#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Bloc
# Generated: Tue Aug 22 00:16:40 2017
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
        self.samp_rate = samp_rate = 48000
        self.salida_wav = salida_wav = 0
        self.rango_l = rango_l = 24000
        self.range_h = range_h = 1
        self.mute_audio = mute_audio = 0

        ##################################################
        # Blocks
        ##################################################
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
        self._rango_l_range = Range(0, 24000, 100, 24000, 200)
        self._rango_l_win = RangeWidget(self._rango_l_range, self.set_rango_l, 'rango_low', "counter_slider", float)
        self.top_layout.addWidget(self._rango_l_win)
        self._range_h_range = Range(0, 24000, 100, 1, 200)
        self._range_h_win = RangeWidget(self._range_h_range, self.set_range_h, "range_h", "counter_slider", float)
        self.top_layout.addWidget(self._range_h_win)
        self._mute_audio_options = (0, 1, )
        self._mute_audio_labels = ('sale', 'mute', )
        self._mute_audio_group_box = Qt.QGroupBox("mute_audio")
        self._mute_audio_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._mute_audio_button_group = variable_chooser_button_group()
        self._mute_audio_group_box.setLayout(self._mute_audio_box)
        for i, label in enumerate(self._mute_audio_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._mute_audio_box.addWidget(radio_button)
        	self._mute_audio_button_group.addButton(radio_button, i)
        self._mute_audio_callback = lambda i: Qt.QMetaObject.invokeMethod(self._mute_audio_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._mute_audio_options.index(i)))
        self._mute_audio_callback(self.mute_audio)
        self._mute_audio_button_group.buttonClicked[int].connect(
        	lambda i: self.set_mute_audio(self._mute_audio_options[i]))
        self.top_layout.addWidget(self._mute_audio_group_box)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
        	10000, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(True)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
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
        	80000, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	12000, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
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
        	1, samp_rate, rango_l, 500, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, range_h, 500, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/root/Desktop/04_-_Caigu_.wav', True)
        self.blocks_mute_xx_0_0 = blocks.mute_ff(bool(mute_audio))
        self.blocks_mute_xx_0 = blocks.mute_ff(bool(salida_wav))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((0.05, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.05, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_source_1 = audio.source(samp_rate, 'hw:2,0', True)
        self.audio_source_0 = audio.source(samp_rate, 'hw:1,0', True)
        self.audio_sink_0 = audio.sink(samp_rate, 'hw', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.blocks_mute_xx_0_0, 0))
        self.connect((self.audio_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.audio_source_1, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_mute_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_mute_xx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_mute_xx_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_mute_xx_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.qtgui_freq_sink_x_1, 1))
        self.connect((self.low_pass_filter_0, 0), (self.high_pass_filter_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_bloc")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(12000, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.rango_l, 500, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.range_h, 500, firdes.WIN_HAMMING, 6.76))

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
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.rango_l, 500, firdes.WIN_HAMMING, 6.76))

    def get_range_h(self):
        return self.range_h

    def set_range_h(self, range_h):
        self.range_h = range_h
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.range_h, 500, firdes.WIN_HAMMING, 6.76))

    def get_mute_audio(self):
        return self.mute_audio

    def set_mute_audio(self, mute_audio):
        self.mute_audio = mute_audio
        self._mute_audio_callback(self.mute_audio)
        self.blocks_mute_xx_0_0.set_mute(bool(self.mute_audio))


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
