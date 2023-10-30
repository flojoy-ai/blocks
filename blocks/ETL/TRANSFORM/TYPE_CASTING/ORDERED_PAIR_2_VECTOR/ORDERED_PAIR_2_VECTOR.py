from flojoy import flojoy, Vector, OrderedPair


@flojoy
def ORDERED_PAIR_2_VECTOR(default: OrderedPair) -> Vector:
    """Convert an OrderedPair DataContainer to a Vector DataContainer.

    Parameters
    ----------
    default : OrderedPair
        The input OrderedPair.

    Returns
    -------
    Vector
        The y component of the input OrderedPair.
    """

    return Vector(v=default.y)
