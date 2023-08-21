from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import GyroDriveBase, DriveBase


# Here are the final ports for all the motors and sensors.
# Please don't change these
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
left_med_motor = Motor(Port.B) 
right_med_motor = Motor(Port.D)

left_color = ColorSensor(Port.A)
right_color = ColorSensor(Port.F)

hub = PrimeHub()

robot = GyroDriveBase(
    left_motor,
    right_motor,
    wheel_diameter=88,
    axle_track= 122)

DEFAULT_SPEED = 300
DEFAULT_ACCELERATION = 500
DEFAULT_TURN_RATE = 300
DEFAULT_TURN_ACCEL = 100

def resetRobot():
    robot.settings(straight_speed=DEFAULT_SPEED, straight_accel=DEFAULT_ACCELERATION, turn_rate=DEFAULT_TURN_RATE, turn_acceleration=DEFAULT_TURN_ACCEL)
    robot.reset()

def resetGyro(angle:int = 0):
    hub.imu.reset_heading(angle)

def goStraight(distance, wait=True, backward = False, straightSpeed=DEFAULT_SPEED, straightAcceleration=DEFAULT_ACCELERATION, turnRate=DEFAULT_TURN_RATE, turnAcceleration=DEFAULT_TURN_ACCEL):
    """
    Drives the robot straight for a specified distance.

    distance -- Distance to travel in mm

    wait -- [Optional, default=True] wait for action to finish before returning from function

    backward -- [Optional, default=False] set to True to move backwards, else robot will move forward

    straightSpeed -- [Optional, default= (Number, mm/s) Straight-line speed of the robot.

    straightAcceleration -- (Number, mm/s²) Straight-line acceleration and deceleration of the robot. Provide a tuple with two values to set acceleration and deceleration separately.

    turnRate -- (Number, deg/s) Turn rate of the robot.

    turnAcceleration (Number, deg/s²) Angular acceleration and deceleration of the robot. Provide a tuple with two values to set acceleration and deceleration separately.
    """
    (origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
    robot.settings(straightSpeed, straightAcceleration, turnRate, turnAcceleration)

    if(backward):
        robot.straight(-1*distance, wait=wait)
    else: 
        robot.straight(distance, wait=wait)
    
    robot.settings(origSpeed, origAccel, origTurnSpeed, origTurnAccel)

def turnToAngle(absoluteAngle:int, wait=True):
    """
    Turns the robot to the specific Gyro angle

    absoluteAngle -- Target angle the robot should get to (range -179 to 180)

    wait -- [Optional, default=True] wait for action to finish before returning from function
    """
    angleToTurn = absoluteAngle - robot.angle()
    robot.turn(angleToTurn)