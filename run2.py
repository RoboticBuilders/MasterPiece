from Utilities import *
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run2():
    resetGyro(0)
    gyroStraightWithDrive(distanceInCm=38, speed=350)
    #right_med_motor.run_angle(speed=1000, rotation_angle = -1300, wait=False) # was 1000
    gyroStraightWithDrive(distanceInCm=20, speed=250) 
    right_med_motor.run_angle(speed=2000, rotation_angle = -1300)
    #come back home
    gyroStraightWithDrive(distanceInCm=48, speed=500, backward=True, targetAngle=0)
    right_med_motor.run_angle(speed=2000, rotation_angle = 1300)

#run2()