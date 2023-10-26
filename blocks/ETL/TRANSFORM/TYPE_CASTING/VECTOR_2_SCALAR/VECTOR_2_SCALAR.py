from numpy import bool_, int_
from flojoy import flojoy, Vector, Scalar


@flojoy
def VECTOR_2_SCALAR(default: Vector) -> Scalar:
    """The VECTOR_2_MATRIX node takes a vector and transform it into matrix data type where
    the shape is chosen by row and col parameters.

    Inputs
    ------
    default: Vector
        The input vector that will be transformed into matrix.

    Parameters
    ----------
    row: int
        number of rows for the new matrix
    col: int
        number of columns for the new matrix
    Returns
    -------
    Matrix
        The matrix that is generated from the given vector and the parameters.
    """
    all_boolean = all(isinstance(element, bool_) for element in default.v)

    if all_boolean:
        decimal_num = sum(bit << i for i, bit in enumerate(default.v))
        return Scalar(c=decimal_num)
    
    all_boolean = all(isinstance(element, int_) for element in default.v)

    if all_boolean:
        decimal_num = sum(element for element in default.v)
        return Scalar(c=decimal_num)
    
    raise ValueError("all elements of the vector must be in boolean or integer type")
