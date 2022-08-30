from tswdtf.streamable import Streamable
from tswdtf.helpers.map_fn import map_fn


class LambdaStreamable(Streamable):
    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def step(self, *inputs):
        output = self.fn(*inputs)
        return output, (), ()


def make_streamable(fn):
    return LambdaStreamable(fn)
