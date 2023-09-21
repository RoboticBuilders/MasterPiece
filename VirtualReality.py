from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

_MM_PER_INCH = 25.4

def virtualRealityTest():
    left_med_motor.run_angle(500, 30)
    turnToAngle(absoluteAngle = 10, turnRate = 100)
    left_med_motor.run_angle(500, 30)
    
virtualRealityTest()