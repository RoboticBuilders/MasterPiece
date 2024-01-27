from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from umath import *
from Utilities import *


left_med_motor.run_angle(2000, 1000)
left_med_motor.run_angle(-2000, 1000)