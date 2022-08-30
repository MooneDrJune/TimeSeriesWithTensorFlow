from tswdtf.streamable import Streamable
from tswdtf.meta.join import Join


def Factory(operator_clazz, operators_args):
    instances = tuple(operator_clazz(*args) for args in operators_args)
    return Join(*instances)
