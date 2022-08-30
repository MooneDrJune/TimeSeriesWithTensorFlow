import tensorflow as tf

from tswdtf.common.common import Sub, Fork, Identity
from tswdtf.common.lag import Lag
from tswdtf.common.set_during import SetDuring
from tswdtf.meta.compose import Compose
from tswdtf.meta.join import Join


def Momentum(period):
    return Compose(
        SetDuring(tf.constant(0.0), period),
        Sub(),
        Join(Identity(), Lag(period)),
        Fork(2),
    )
