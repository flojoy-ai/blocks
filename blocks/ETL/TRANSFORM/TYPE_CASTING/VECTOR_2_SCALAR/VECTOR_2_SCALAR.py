from flojoy import flojoy, Vector, Scalar


@flojoy
def VECTOR_2_SCALAR(default: Vector) -> Scalar:
    """The VECTOR_2_SCALAR node takes a vector and transform it into scalar data type

    Parameters
    ----------
    default: Vector
        The input vector that will be transformed into scalar data type.

    Returns
    -------
    Scalar
        The scalar that is generated from the given vector.
    """
    all_boolean = all(isinstance(element, bool) for element in default.v)

    if all_boolean:
        decimal_num = sum(bit << i for i, bit in enumerate(default.v))
        return Scalar(c=decimal_num)

    all_boolean = all(isinstance(element, int) for element in default.v)

    if all_boolean:
        decimal_num = sum(element for element in default.v)
        return Scalar(c=decimal_num)

    raise ValueError("all elements of the vector must be in boolean or integer type")
