import tensorflow as tf

from tswdtf.finance.average_true_range import AverageTrueRange
from tswdtf.streamable import Streamable


class Supertrend(Streamable):
    def __init__(self, atr_period, factor):
        super().__init__()
        self.factor = factor
        self.atr = AverageTrueRange(atr_period)

    def step(
        self,
        close_price,
        low_price,
        high_price,
        prev_atr_state=None,
        last_close=None,
        last_trend_down=None,
        last_trend_up=None,
        last_trend=None,
    ):

        if last_close is None:
            last_close = tf.constant(0.0)
        if last_trend_down is None:
            last_trend_down = tf.constant(0.0)
        if last_trend_up is None:
            last_trend_up = tf.constant(0.0)
        if last_trend is None:
            last_trend = tf.constant(0)

        def default(atr):
            hl2 = (high_price + low_price) / 2.0
            up = hl2 - self.factor * atr
            down = hl2 + self.factor * atr

            trend_up = tf.cond(
                last_close > last_trend_up,
                lambda: tf.maximum(up, last_trend_up),
                lambda: up,
            )

            trend_down = tf.cond(
                last_close < last_trend_down,
                lambda: tf.minimum(down, last_trend_down),
                lambda: down,
            )

            trend = tf.case(
                {
                    close_price > last_trend_down: lambda: 1,
                    close_price < last_trend_up: lambda: -1,
                },
                exclusive=True,
                default=lambda: tf.cond(
                    tf.equal(last_trend, 0), lambda: 1, lambda: last_trend
                ),
            )

            supertrend = tf.cond(
                tf.equal(trend, 1), lambda: trend_up, lambda: trend_down
            )

            return trend_down, trend_up, trend, supertrend

        def warmup():
            return 0.0, 0.0, 0, 0.0

        atr, next_atr_state, atr_init = self.atr(
            inputs=(close_price, low_price, high_price),
            state=prev_atr_state,
            streamable=False,
        )

        trend_down, trend_up, trend, supertrend = tf.cond(
            tf.equal(atr, 0), lambda: warmup(), lambda: default(atr)
        )

        return (
            supertrend,
            (next_atr_state, close_price, trend_down, trend_up, trend),
            (atr_init, last_close, last_trend_down, last_trend_up, last_trend),
        )
