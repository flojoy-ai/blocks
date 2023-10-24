from flojoy import DataContainer, TextBlob, flojoy


@flojoy()
def DATACONTAINER_TYPE(
    default: DataContainer,
) -> TextBlob:
    """The DATACONTAINER_TYPE node returns a TextBlob containing the input DataContainer type (e.g. Vector).

    Must use the TEXT_VIEW node to view the text.

    Parameters
    ----------
    default : DataContainer
        The input DataContainer to check the type.

    Returns
    -------
    DataContainer
        TextBlob: Input DataContainer type
    """

    return TextBlob(text_blob=default.type)
