import tensorflow as tf
from tswdtf.common.set_during import SetDuring
from tswdtf.finance.moving_average_crossover import SimpleMovingAverageCrossover
from tswdtf.finance.signals.zero_crossover_signal import ZeroCrossoverSignal
from tswdtf.meta.compose import Compose


def SimpleMovingAverageCrossoverSignal(slow, fast):
    return Compose(
        SetDuring(tf.constant(0), slow),
        ZeroCrossoverSignal(),
        SimpleMovingAverageCrossover(slow, fast),
    )
