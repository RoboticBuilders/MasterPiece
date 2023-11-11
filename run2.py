from Utilities import *
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run2_testSide():
    short_bucket_rotation_angle = 300
    short_bucket_rotation_angle = 600

    #go to the movie set
    gyroStraightWithDrive(distanceInCm=51, speed=350)
    right_med_motor.run_angle(600, rotation_angle=-200)
    
    #get camera in right position
    gyroStraightWithDrive(distanceInCm=18, speed=200, backward=True)
    turnToAngle(targetAngle=315, speed=40)
    right_med_motor.run_angle(600, rotation_angle=100)
    right_med_motor.run_angle(600, rotation_angle=250, wait=False)

    #go back to align for sound mixer
    gyroStraightWithDrive(distanceInCm=26, speed=200, backward=True, targetAngle=0)

    #set angle to sound mixer
    turnToAngle(targetAngle=300, speed=40)

    #go to sound mixer
    gyroStraightWithDrive(distanceInCm=45, speed=250)
    right_med_motor.run_angle(600, rotation_angle=-600)

    #come back home
    gyroStraightWithDrive(distanceInCm=45, speed=500, backward=True, targetAngle=0)
    #right_med_motor.run_angle(speed=600, rotation_angle=600)

def run2():
    resetGyro(0)
    run2_testSide()
