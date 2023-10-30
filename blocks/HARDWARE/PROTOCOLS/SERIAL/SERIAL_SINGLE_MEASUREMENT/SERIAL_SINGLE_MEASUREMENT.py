from typing import Optional

import numpy as np
import serial
from flojoy import OrderedPair, SerialDevice, flojoy


@flojoy(deps={"pyserial": "3.5"})
def SERIAL_SINGLE_MEASUREMENT(
    device: SerialDevice,
    default: Optional[OrderedPair] = None,
    baudrate: int = 9600,
) -> OrderedPair:
    """Take a single data reading from a connected serial device (such as an Arduino connected by USB).

    Parameters
    ----------
    baudrate : int
        Baud rate for the serial communication.
    comport : string
        Defines the communication port on which the serial device is connected.

    Returns
    -------
    OrderedPair
        the y axis contains the reading
    """

    set = serial.Serial(device.port, timeout=1, baudrate=baudrate)
    s = ""
    while s == "":
        s = set.readline().decode()

    reading = s[:-2].split(",")
    reading = np.array(reading)  # Create an array
    reading = reading.astype("float64")  # Convert the array to float
    x = np.arange(0, reading.size)  # Create a second array

    return OrderedPair(x=x, y=reading)
