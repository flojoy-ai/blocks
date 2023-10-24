from flojoy import DataContainer, TextBlob, flojoy


@flojoy()
def PRINT_DATACONTAINER(
    default: DataContainer,
) -> TextBlob:
    """The PRINT_DATACONTAINER node returns a TextBlob containing input DataContainer information.

    Must use the TEXT_VIEW node to view the text.

    Parameters
    ----------
    default : DataContainer
        The input DataContainer to print.

    Returns
    -------
    DataContainer
        TextBlob: Input datacontainer information
    """

    return TextBlob(text_blob=str(default))
