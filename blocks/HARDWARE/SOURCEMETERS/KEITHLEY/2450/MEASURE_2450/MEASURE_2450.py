from typing import Optional, Literal
from flojoy import VisaConnection, flojoy, DataContainer, TextBlob


@flojoy(deps={"tm_devices": "1.0"}, inject_connection=True)
def MEASURE_2450(
    connection: VisaConnection,
    input: Optional[DataContainer] = None,
    measure: Literal["voltage", "current", "resistance", "power"] = "voltage",
) -> TextBlob:
    """Changes the measurement units for the 2450.

    Requires a CONNECT_2450 block to create the connection.

    Parameters
    ----------
    connection : VisaConnection
        The VISA address (requires the CONNECTION_2450 block).
    measure : select, default=voltage
        Select the measure unit

    Returns
    -------
    TextBlob
        Measurement
    """

    # Retrieve oscilloscope instrument connection
    smu = connection.get_handle()

    match measure:
        case "current":
            smu.commands.smu.measure.func = "smu.FUNC_DC_CURRENT"
        case "voltage":
            smu.commands.smu.measure.func = "smu.FUNC_DC_VOLTAGE"
        case "resistance":
            smu.commands.smu.measure.func = "smu.FUNC_DC_RESISTANCE"
        case "power":
            smu.commands.smu.measure.func = "smu.FUNC_DC_POWER"

    return TextBlob(text_blob=f"Measure {measure}")
