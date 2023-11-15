from skimage.exposure import adjust_gamma
import numpy as np
from flojoy import Image, flojoy


@flojoy(deps={"scikit-image": "0.21.0"})
def GAMMA_ADJUSTMENT(
    default: Image,
    gain: float = 1,
    gamma: float = 1,
) -> Image:
    """
    Adjusts the gamma of an input image and outputs the adjusted image

    Parameters
    ----------
    default: Image
        The input image
    gain: float
        The gain of the logarithmic correction. Default is 1.
    gamma: float
        The gamma to correct to. Default is 1.

    Returns
    -------
    Image
        The adjusted image.
    """

    r = default.r
    g = default.g
    b = default.b
    a = default.a

    if a is not None:
        rgba_image = np.stack((r, g, b, a), axis=2)
    else:
        rgba_image = np.stack((r, g, b), axis=2)

    # Check if the image is in the appropriate format
    if rgba_image.dtype != np.uint8:
        raise ValueError("Image must be in uint8 format")

    # Apply logarithmic correction
    corrected_image = adjust_gamma(rgba_image, gain=gain, gamma=gamma)

    r = corrected_image[:, :, 0]
    g = corrected_image[:, :, 1]
    b = corrected_image[:, :, 2]
    if a is not None:
        a = corrected_image[:, :, 3]

    return Image(r=r, g=g, b=b, a=a)
