from typing import Optional
from flojoy import flojoy, TextBlob
from PYTHON.utils.mecademic_state.mecademic_calculations import get_circle_positions
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle
from PYTHON.utils.mecademic_state.mecademic_helpers import safe_robot_operation


@safe_robot_operation
@flojoy(deps={"mecademicpy": "1.4.0"})
def MOVE_CIRCLE(
    ip_address: TextBlob,
    radius: Optional[float] = 0.0,
    revolutions: Optional[float] = 1.0,
) -> TextBlob:
    """
    The Move circle node moves in a circle relative to a reference plane.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.

    Parameters:
    -------
    radius: Optional[float]
        The radius of the circle. If not specified, the default value of 0.0 is used.
    revolutions: Optional[float]
        The number of revolutions to make. If not specified, the default value of 1.0 is used.

    Returns
    -------
    ip_address
        The IP address of the robot arm.

    """
    robot = query_for_handle(ip_address)

    X, Y, Z, alpha, beta, gamma = robot.GetPose()

    positions = get_circle_positions(radius, revolutions, (X, Y, Z))
    for position in positions:
        robot.MoveLin(
            x=position[0],
            y=position[1],
            z=position[2],
            alpha=alpha,
            beta=beta,
            gamma=gamma,
        )
    robot.MoveLin(x=X, y=Y, z=Z, alpha=alpha, beta=beta, gamma=gamma)

    return ip_address
