import traceback
from typing import Optional, cast

import serial
from flojoy import DataContainer, SerialConnection, TextBlob, flojoy


@flojoy(deps={"pyserial": "3.5"}, inject_connection=True)
def PROLOGIX_VER(
    connection: SerialConnection,
    default: Optional[DataContainer] = None,
) -> TextBlob:
    """The PROLOGIX_VER command queries the Prologix USB-to-GPIB firmware version.

    Inputs
    ------
    default: DataContainer
        Any DataContainer - likely connected to the output of the OPEN_SERIAL node.

    Parameters
    ----------
    connection: Serial
        The open serial connection with the instrument.

    Returns
    -------
    TextBlob
        The Prologix controller available commands.
    """

    try:
        # Start serial communication with the instrument
        set = cast(serial.Serial, connection.get_handle())
        if set is None:
            raise ValueError("Serial communication is not open")
        set.write(b"++ver\r\n")
        s = set.read(1000).decode()
    except Exception:
        s = traceback.format_exc()

    return TextBlob(s)
