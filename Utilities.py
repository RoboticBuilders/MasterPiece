from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait
from pybricks.parameters import Stop


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
DEFAULT_TURN_ACCEL = 300

def resetRobot():
    robot.settings(straight_speed=DEFAULT_SPEED, straight_acceleration=DEFAULT_ACCELERATION, turn_rate=DEFAULT_TURN_RATE, turn_acceleration=DEFAULT_TURN_ACCEL)
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

def turnToAngle(absoluteAngle:int, turnRate:int = DEFAULT_TURN_RATE, turnAcceleration = DEFAULT_TURN_ACCEL, wait=True):
    """
    Turns the robot to the specific Gyro angle

    absoluteAngle -- Target angle the robot should get to (range -179 to 180)

    wait -- [Optional, default=True] wait for action to finish before returning from function
    """
    (origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
    robot.settings(origSpeed, origAccel, turnRate, turnAcceleration)

    angleToTurn = absoluteAngle - robot.angle()
    robot.turn(angleToTurn)

    robot.settings(origSpeed, origAccel, origTurnSpeed, origTurnAccel)


def driveTillLine(speed, distanceInCM, target_angle, doCorrection=True, colorSensorToUse="Left", blackOrWhite="Black"):
    
    if colorSensorToUse == "Left":
        if blackOrWhite == "Black":
            print(left_color.hsv())
            saturation = left_color.hsv().s
            robot.drive(speed = speed, turn_rate = 0)
            while saturation > 10:
                # print("Color sensor Saturation: {}".format(saturation))
                saturation = left_color.hsv().s

            print("Stopping at saturation = {}".format(saturation))
            # robot.hold()
            # left_motor.hold()
            # right_motor.hold()
            # robot.drive(speed=-1*speed, turn_rate=0)
            # robot.stop()
            robot.straight(distance=1, then=Stop.BRAKE, wait=True)
            if(doCorrection):
                (origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
                robot.settings(100, 100, 100, 100)
                robot.straight(distance=-40, then=Stop.HOLD, wait=True)
                robot.settings(origSpeed, origAccel, origTurnSpeed, origTurnAccel)
            # robot.stop()
            # robot.stop(Stop.Hold)
            # wait(2000)
            saturation = left_color.hsv().s
            # print("Color sensor Saturation: {}".format(saturation))
                