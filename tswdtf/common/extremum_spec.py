import numpy as np
import tensorflow as tf

from tswdtf.common.extremum import (
    GlobalMinimum,
    GlobalMaximum,
    LocalMinimum,
    LocalMaximum,
)
from tswdtf.tests import TestCase


class ExtremumSpec(TestCase):
    def setUp(self):
        self.sheets = self.read_ods(self.from_test_res("extremum.ods", __file__))
        self.sheet = self.sheets["Sheet1"]

    def test_global_min(self):
        global_minimum = GlobalMinimum()
        values = tf.placeholder(tf.float32)
        global_minimum_ts, _, _ = global_minimum(values)

        with tf.Session() as sess:
            output = sess.run(global_minimum_ts, {values: self.sheet["Value"]})

        np.testing.assert_almost_equal(
            output, self.sheet["GlobalMin"].values, decimal=3
        )

    def test_global_max(self):
        global_maximum = GlobalMaximum()
        values = tf.placeholder(tf.float32)
        global_maximum_ts, _, _ = global_maximum(values)

        with tf.Session() as sess:
            output = sess.run(global_maximum_ts, {values: self.sheet["Value"]})

        np.testing.assert_almost_equal(
            output, self.sheet["GlobalMax"].values, decimal=3
        )

    def test_local_min(self):
        local_minimum = LocalMinimum(5)
        values = tf.placeholder(tf.float32)
        local_minimum_ts, _, _ = local_minimum(values)

        with tf.Session() as sess:
            output = sess.run(local_minimum_ts, {values: self.sheet["Value"]})

        np.testing.assert_almost_equal(output, self.sheet["LocalMin"].values, decimal=3)

    def test_local_max(self):
        local_maximum = LocalMaximum(5)
        values = tf.placeholder(tf.float32)
        local_maximum_ts, _, _ = local_maximum(values)

        with tf.Session() as sess:
            output = sess.run(local_maximum_ts, {values: self.sheet["Value"]})

        np.testing.assert_almost_equal(output, self.sheet["LocalMax"].values, decimal=3)
