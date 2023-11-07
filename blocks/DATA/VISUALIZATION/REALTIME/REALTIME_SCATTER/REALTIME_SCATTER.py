import numpy as np
from flojoy import DataFrame, Matrix, OrderedPair, Plotly, flojoy, Vector


@flojoy(node_type="SCATTER", forward_result=True)
def SCATTER(default: OrderedPair | DataFrame | Matrix | Vector) -> OrderedPair:
    """The SCATTER node creates a Plotly Scatter visualization for a given input DataContainer.

    Inputs
    ------
    default : OrderedPair|DataFrame|Matrix|Vector
        the DataContainer to be visualized

    Returns
    -------
    Plotly
        the DataContainer containing the Plotly Scatter visualization
    """

    match default:
        case OrderedPair():
            return default
        case Vector():
            return OrderedPair(x=np.arange(len(default.v)), y=default.v)
        case _:
            raise TypeError(
                f"SCATTER node does not support input of type {type(default)}"
            )
