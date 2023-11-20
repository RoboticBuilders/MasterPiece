# NOTE NOTE: This is RUN1
# There are things in here called Run2* please ignore.

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

def run2_withLineDetection():
    #go to the movie set
    gyroStraightWithDrive(distanceInCm=51, speed=350)
    right_med_motor.run_angle(600, rotation_angle=-200)
    
    #get camera in right position
    gyroStraightWithDrive(distanceInCm=18, speed=200, backward=True)
    turnToAngle(targetAngle=315, speed=40)
    right_med_motor.run_angle(600, rotation_angle=100)
    right_med_motor.run_angle(600, rotation_angle=250, wait=False)

    #go back to align for sound mixer
    turnToAngle(targetAngle=225, speed=300)
    driveTillLine(maxDistance=210, speed=200, doCorrection=False, sensor=right_color)
    gyroStraightWithDrive(distanceInCm=axle_track/20 - 2, speed=200, backward=True)

    #turnToAngle(targetAngle=325, speed=300, oneWheelTurn=True, forceTurn=FORCETURN_RIGHT)
    turnToAngle(targetAngle=320, speed=300)
    gyroStraightWithDrive(distanceInCm=20, speed=200)
    right_med_motor.run_angle(600, rotation_angle=-300)
    gyroStraightWithDrive(distanceInCm=47, speed=600, backward=True)


def _run1_internal():
    #go to the movie set
    gyroStraightWithDrive(distanceInCm=54, speed=350)
    right_med_motor.run_angle(speed=2000, rotation_angle = -1300)
    
    #get camera in right position
    gyroStraightWithDrive(distanceInCm=18, speed=200, backward=True)

    turnToAngle(targetAngle=320, speed=40)
    right_med_motor.run_angle(2000, rotation_angle=400) # was 400
    right_med_motor.run_angle(2000, rotation_angle=900, wait=False)

    turnToAngle(targetAngle=0, speed=100)

    gyroStraightWithDrive(distanceInCm=6*CM_PER_INCH, speed=1000, backward=True)
    # turnToAngle(targetAngle=180, speed=100, forceTurn=FORCETURN_LEFT)
    # gyroStraightWithDrive(distanceInCm=10*CM_PER_INCH, speed=1000)
    
    # right_med_motor.run_angle(speed=800, rotation_angle = 500)

def run2_B():
    gyroStraightWithDrive(distanceInCm=34, speed=350)
    right_med_motor.run_angle(speed=600, rotation_angle = -1300, wait=False) # was 1000
    gyroStraightWithDrive(distanceInCm=20, speed=250)

    #come back home
    gyroStraightWithDrive(distanceInCm=54, speed=500, backward=True, targetAngle=0)

    right_med_motor.run_angle(speed=800, rotation_angle = 1300)

def run1():
    resetGyro(0)
    #run2_testSide()
    _run1_internal()
