from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import GyroDriveBase, DriveBase

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
left_med_motor = Motor(Port.B)
right_med_motor = Motor(Port.D)

hub = PrimeHub()

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=88,
    axle_track= 122)

DEFAULT_SPEED = 300
DEFAULT_ACCELERATION = 100
DEFAULT_TURN_RATE = 300
DEFAULT_TURN_ACCEL = 100

def resetRobot():
    robot.settings(straight_speed=DEFAULT_SPEED, straight_accel=DEFAULT_ACCELERATION, turn_rate=DEFAULT_TURN_RATE, turn_acceleration=DEFAULT_TURN_ACCEL)
    robot.reset()

def resetGyro(angle:int = 0):
    hub.imu.reset_heading(angle)

async def goStraight(distance, backward = False, straightSpeed=DEFAULT_SPEED, straightAcceleration=DEFAULT_ACCELERATION, turnRate=DEFAULT_TURN_RATE, turnAcceleration=DEFAULT_TURN_ACCEL, wait=True):
    """
    Drives the robot straight for a specified distance.

    distance -- Distance to travel in mm
    backward -- [Optional, default=false] set to True to move backwards, else robot will move forward
    straightSpeed -- [Optional, default= (Number, mm/s) Straight-line speed of the robot.
    straightAcceleration -- (Number, mm/s²) Straight-line acceleration and deceleration of the robot. Provide a tuple with two values to set acceleration and deceleration separately.
    turnRate -- (Number, deg/s) Turn rate of the robot.
    turnAcceleration (Number, deg/s²) Angular acceleration and deceleration of the robot. Provide a tuple with two values to set acceleration and deceleration separately.
    wait -- 
    """
    (origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
    robot.settings(straightSpeed, straightAcceleration, turnRate, turnAcceleration)

    if(backward):
        robot.straight(-1*distance, wait)
    else: 
        robot.straight(distance, wait)
    
    robot.settings(origSpeed, origAccel, origTurnSpeed, origTurnAccel)

async def turnToAngle(absoluteAngle:int, wait=True):
    """
    Turns the robot to the specific Gyro angle
    absoluteAngle -- Target angle the robot should get to (range -179 to 180)
    """
    angleToTurn = absoluteAngle - robot.imu.heading()
    robot.turn(angleToTurn)