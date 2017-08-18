#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Bl
# Generated: Wed Aug 16 20:00:45 2017
##################################################

from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_bl(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Bl")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.rango_l = rango_l = 24000
        self.range_h = range_h = 50

        ##################################################
        # Blocks
        ##################################################
        _rango_l_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rango_l_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rango_l_sizer,
        	value=self.rango_l,
        	callback=self.set_rango_l,
        	label='rango_l',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rango_l_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rango_l_sizer,
        	value=self.rango_l,
        	callback=self.set_rango_l,
        	minimum=0,
        	maximum=24000,
        	num_steps=240,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rango_l_sizer)
        _range_h_sizer = wx.BoxSizer(wx.VERTICAL)
        self._range_h_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_range_h_sizer,
        	value=self.range_h,
        	callback=self.set_range_h,
        	label="range_h",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._range_h_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_range_h_sizer,
        	value=self.range_h,
        	callback=self.set_range_h,
        	minimum=0,
        	maximum=24000,
        	num_steps=240,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_range_h_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, rango_l, 100, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0 = filter.fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, range_h, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/usr/share/sounds/alsa/Front_Center.wav", True)
        self.audio_sink_0 = audio.sink(samp_rate, "sysdefault", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.low_pass_filter_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.wxgui_fftsink2_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.range_h, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.rango_l, 100, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_rango_l(self):
        return self.rango_l

    def set_rango_l(self, rango_l):
        self.rango_l = rango_l
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.rango_l, 100, firdes.WIN_HAMMING, 6.76))
        self._rango_l_slider.set_value(self.rango_l)
        self._rango_l_text_box.set_value(self.rango_l)

    def get_range_h(self):
        return self.range_h

    def set_range_h(self, range_h):
        self.range_h = range_h
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.range_h, 100, firdes.WIN_HAMMING, 6.76))
        self._range_h_slider.set_value(self.range_h)
        self._range_h_text_box.set_value(self.range_h)

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
    tb = top_bl()
    tb.Start(True)
    tb.Wait()
