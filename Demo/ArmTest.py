from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from umath import *
from Utilities import *


orgSpeed,orgAccel,orgTorque = left_med_motor.control.limits()
left_med_motor.control.limits(speed = orgSpeed,acceleration = orgAccel,torque = 1000)

while True:
    left_med_motor.run_angle(rotation_angle=1000, speed=300)
    left_med_motor.run_angle(rotation_angle=-1000, speed=300)