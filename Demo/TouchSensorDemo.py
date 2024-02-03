from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

def run():
    resetRobot()
    drive_base.straight(distance = 1000, wait = False)
    stall_detect.avg_load(max_load_change = 1, minValidLoad = 30, minObservationsRequired = 15, debug = False)

run()