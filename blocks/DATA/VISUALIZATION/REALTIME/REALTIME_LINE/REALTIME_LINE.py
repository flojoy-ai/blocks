import numpy as np
from flojoy import OrderedPair, flojoy, Vector


@flojoy(node_type="LINE", forward_result=True)
def REALTIME_LINE(
    default: OrderedPair | Vector, log_y_scale: bool = False
) -> OrderedPair:
    """Creates a line plot visualization for a given input DataContainer.

    Inputs
    ------
    default : OrderedPair|DataFrame|Matrix|Vector
        the DataContainer to be visualized

    Returns
    -------
    OrderedPair
        Forwards data to frontend for visualization
    """

    match default:
        case OrderedPair():
            return default
        case Vector():
            return OrderedPair(x=np.arange(len(default.v)), y=default.v)
        case _:
            raise TypeError(
                f"REALTIME_LINE node does not support input of type {type(default)}"
            )
