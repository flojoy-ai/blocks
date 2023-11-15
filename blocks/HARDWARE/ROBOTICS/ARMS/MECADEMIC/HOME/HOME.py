from flojoy import flojoy, TextBlob
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle
from PYTHON.utils.mecademic_state.mecademic_helpers import safe_robot_operation


@safe_robot_operation
@flojoy(deps={"mecademicpy": "1.4.0"})
def HOME(ip_address: TextBlob) -> TextBlob:
    """
    Home the robot arm. This block is required to be run before any other robot arm movement. It is recommended to run this block immediately after "ACTIVATE".

    Inputs
    ------
    ip_address
        The IP address of the robot arm.

    Returns
    -------
    ip_address
        The IP address of the robot arm.
    """
    robot = query_for_handle(ip_address)
    robot.Home()
    robot.WaitHomed()
    return ip_address
