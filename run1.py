# NOTE NOTE: This is RUN1
# There are things in here called Run2* please ignore.

from Utilities import *
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

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



def run1():
    resetGyro(0)
    #run2_testSide()
    _run1_internal()
