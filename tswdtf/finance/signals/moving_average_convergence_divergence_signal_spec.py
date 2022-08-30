import numpy as np
import pandas as pd
import tensorflow as tf

from tswdtf.finance.signals import (
    MovingAverageConvergenceDivergenceSignal as MACDSignal,
)
from tswdtf.tests import TestCase


class MACDSignalSpec(TestCase):
    def setUp(self):
        self.sheets = self.read_ods(self.from_test_res("macd_signals.ods", __file__))

    def test_single_dim(self):
        s = self.sheets["Sheet1"]
        prices_ts = s["Close"]

        expected_signals = s["Trade Signals"]

        signal = MACDSignal(26, 12, 9)
        prices = tf.placeholder(tf.float32)
        signals_ts, _, _ = signal(prices)

        with tf.Session() as sess:
            output_ts = sess.run(signals_ts, {prices: prices_ts})

        np.testing.assert_almost_equal(output_ts, expected_signals.values, decimal=3)
