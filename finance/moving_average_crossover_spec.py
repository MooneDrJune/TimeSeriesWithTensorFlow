import numpy as np
import pandas as pd
import tensorflow as tf

from tswdtf.tests import TestCase
from tswdtf.finance.moving_average_crossover import SimpleMovingAverageCrossover


class MovingAverageCrossoverSpec(TestCase):
    def setUp(self):
        self.sheets = self.read_ods(
            self.from_test_res("moving_average_crossover.ods", __file__)
        )

    def test_simple_moving_average_crossover(self):
        ma_crossover = SimpleMovingAverageCrossover(10, 4)
        close_prices = tf.placeholder(tf.float32)
        sheet = self.sheets["Sheet1"]

        ma_crossover_ts, _, _ = ma_crossover(close_prices)
        with tf.Session() as sess:
            output = sess.run(ma_crossover_ts, {close_prices: sheet["Close"]})

        np.testing.assert_almost_equal(output, sheet["MA Crossover"], decimal=3)
