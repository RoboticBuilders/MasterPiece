from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

left_med_motor.run_angle(speed=200, rotation_angle=-150)
left_med_motor.run_angle(speed=200, rotation_angle=150)