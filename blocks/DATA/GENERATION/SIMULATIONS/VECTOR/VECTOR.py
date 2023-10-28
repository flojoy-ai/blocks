from flojoy import flojoy, Vector
from numpy import array

@flojoy
def VECTOR(elements : str = "") -> Vector:
    """The VECTOR node creats a vector type data given the elements

    Parameters
    ----------
    elements : str, default = ""
        The elements that should be in the vector

    Returns
    -------
    Vector
        The vector consists of the elements.
    """

    elements_list = elements.split(",")
    
    all_int = [int(element) for element in elements_list if element.isnumeric()]

    if all(isinstance(element, int) for element in all_int):
        return Vector(v=array(all_int))
    
    all_bool = [element.lower() == "true" for element in elements_list]

    if  all(isinstance(element, bool) for element in all_bool):
        return Vector(v=array(all_bool))

    raise ValueError(f"all elements of the vector must be in boolean or integer type: {all_int}")