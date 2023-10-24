import numpy as np
from flojoy import flojoy, Matrix


@flojoy
def MATMUL(a: Matrix, b: Matrix) -> Matrix:
    """The MATMUL node takes two input matrices, multiplies them, and returns the result.

    Parameters
    ----------
    a : Matrix
        The matrix on the left of the multiplication.
    b : Matrix
        The matrix on the right of the multiplication.

    Returns
    -------
    Matrix
        The matrix result from the matrix multiplication.
    """

    return Matrix(m=np.matmul(a.m, b.m))
