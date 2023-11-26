from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *


#testHsv(sensor=right_color)

driveTillHsvRange(maxDistance=2400, speed=15,sensor=left_color, hueRange = range(351, 357), saturationRange=range(64, 68), valueRange=range(64, 68) )
turnToAngle(220, speed=200)
gyroStraightWithDrive(distanceInCm=12, speed=200, targetAngle=220)
driveTillHsvRange(maxDistance=2400, speed=200,sensor=right_color, hueRange = range(47, 55), saturationRange=range(13, 19), valueRange=range(74, 82) )