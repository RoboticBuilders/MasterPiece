from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *


def testDriveForTime():
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle=0, speed=500)
    drive_base.use_gyro(False)
    driveForTime(timeInMS = 500, stopAtEnd = True, speed = 300, turnRate = 0)
    wait(2000)

testDriveForTime()