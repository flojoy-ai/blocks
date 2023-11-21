from typing import Optional, Literal
from flojoy import VisaConnection, flojoy, DataContainer, TextBlob


@flojoy(deps={"tm_devices": "1.0"}, inject_connection=True)
def SOURCE_2450(
    connection: VisaConnection,
    input: Optional[DataContainer] = None,
    function: Literal["current", "voltage"] = "unchanged",
    level: float = 1.0,
    limit: float = 1.0,
) -> TextBlob:
    """Set the source output settings.

    Requires a CONNECT_2450 block to create the connection.

    Parameters
    ----------
    connection : VisaConnection
        The VISA address (requires the CONNECTION_2450 block).
    function : select, default=unchanged
        The type of output to use
    level : float, default=1
        The fixed voltage or current to output.
    limit : float, default=1
        Output limit (if function=voltage, current is limited and visa versa)

    Returns
    -------
    TextBlob
        Source settings
    """

    # Retrieve oscilloscope instrument connection
    smu = connection.get_handle()

    if function == "current":
        smu.commands.smu.source.func = "smu.FUNC_DC_CURRENT"
        smu.commands.smu.source.vlimit.level = limit
    else:
        smu.commands.smu.source.func = "smu.FUNC_DC_VOLTAGE"
        smu.commands.smu.source.ilimit.level = limit

    smu.commands.smu.source.level = level

    return TextBlob(text_blob="Source settings")
