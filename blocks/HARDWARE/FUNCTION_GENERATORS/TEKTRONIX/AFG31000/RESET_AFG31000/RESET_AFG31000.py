from flojoy import flojoy, DataContainer, TextBlob, VisaConnection
from typing import Optional


@flojoy(inject_connection=True)
def RESET_AFG31000(
    connection: VisaConnection,
    input: Optional[DataContainer] = None,
) -> TextBlob:
    """Reset the instrument.

    This block should also work with compatible Tektronix AFG31XXX instruments.

    Parameters
    ----------
    connection: VisaConnection
        The VISA address (requires the CONNECTION_AFG31000 block).

    Returns
    -------
    TextBlob
        Placeholder
    """

    afg = connection.get_handle()

    afg.write("*RST")

    return TextBlob(text_blob="Reset channel parameters")
