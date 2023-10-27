from flojoy import TextBlob, flojoy
from PYTHON.utils.mecademic_state.mecademic_state import (
    add_handle,
    init_handle_map,
    query_for_handle,
)


@flojoy(deps={"mecademicpy": "1.4.0"})
def CONNECT(ip_address: str, simulator: bool = False) -> TextBlob:
    """
    The CONNECT node establishes a connection to the Mecademic robot arm via its API and activates the robot arm.

    Parameters
    ----------
    ip_address : str
        The IP address of the robot arm.
    simulator : bool
        Whether to activate the simulator or not. Defaults to False.


    Returns
    -------
    String
       The IP address of the robot arm.
    """
    init_handle_map(allow_reinit=True)
    add_handle(ip_address)

    handle = query_for_handle(ip_address)
    if simulator:
        handle.ActivateSim()
    else:
        handle.ActivateRobot()
    handle.WaitActivated()

    return TextBlob(text_blob=ip_address)
