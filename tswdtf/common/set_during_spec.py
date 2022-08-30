import numpy as np
import tensorflow as tf

from tswdtf.common.set_during import SetDuring
from tswdtf.tests import TestCase


class SetDuringSpec(TestCase):
    def test_set_during(self):
        values = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9])
        set_during = SetDuring(0, 4)
        ts, _, _ = set_during(values)

        with tf.Session() as sess:
            output = sess.run(ts)

        np.testing.assert_almost_equal(output, [0, 0, 0, 0, 5, 6, 7, 8, 9], decimal=3)
