from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

def run3():
    resetGyro(0)
    turnToAngle(-30, speed=200, oneWheelTurn=True)
    resetGyro(0)

    gyroStraightWithDrive(48)

    turnToAngle(-40, speed=200, oneWheelTurn=True)
    resetGyro(0)
    wait(500)

    gyroStraightWithDrive(38)

    turnToAngle(17, speed=200)
    resetGyro(0)
    wait(500)

    gyroStraightWithDrive(15)

    turnToAngle(-42, speed=200, oneWheelTurn=True)
    resetGyro(0)
    wait(1000)

    gyroStraightWithDrive(-24)

    left_med_motor.run_angle(300, 360 * 4)

    left_med_motor.run_angle(300, -360 * 4)

    gyroStraightWithDrive(7)

    turnToAngle(-90, speed=200)

    gyroStraightWithDrive(20)

    resetGyro(0)

    turnToAngle(90, speed=200)

    gyroStraightWithDrive(23)

    gyroStraightWithDrive(-50)
    resetGyro(0)

    turnToAngle(110, speed=200)
    resetGyro(0)

    gyroStraightWithDrive(110)

run3()