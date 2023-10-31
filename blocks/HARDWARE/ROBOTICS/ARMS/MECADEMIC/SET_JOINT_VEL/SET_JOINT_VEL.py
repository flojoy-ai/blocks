from flojoy import TextBlob, flojoy
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_JOINT_VEL(ip_address: TextBlob, v: float) -> TextBlob:
    """
    Set the robot arm's angular velocity for its joints.

    Parameters
    ----------
    ip_address : TextBlob
        The IP address of the robot arm.

    v : float
        The angular velocity to be set for each joint.

    Returns
    -------
    ip_address : TextBlob
        The IP address of the robot arm.
    """

    robot = query_for_handle(ip_address)
    robot.SetJointVel(v)
    return ip_address
