import tensorflow as tf
from tswdtf.meta.compose import Compose
from tswdtf.common.common import Select
from tswdtf.common.set_during import SetDuring
from tswdtf.finance.signals.zero_crossover_signal import ZeroCrossoverSignal
from tswdtf.finance.moving_average_convergence_divergence import (
    MovingAverageConvergenceDivergence as MACD,
)


def MovingAverageConvergenceDivergenceSignal(slow, fast, macd):
    return Compose(
        SetDuring(tf.constant(0), slow + macd - 2),
        ZeroCrossoverSignal(),
        Select(4),
        MACD(slow=slow, fast=fast, macd=macd),
    )
