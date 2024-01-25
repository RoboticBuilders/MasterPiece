from Utilities import *
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def _run2_internal():
    drive_base.straight(distance=510)
    right_med_motor.run_angle(speed=2000, rotation_angle = -1300)
    
    #get camera in right position
    gyroStraightWithDrive(distanceInCm=18, speed=300, backward=True)

    turnToAngle(targetAngle=330, speed=250) # Anya: was 320 until 11/25/23, but was coming in way of run4, so reducing angle
    right_med_motor.run_angle(2000, rotation_angle=800)

    right_med_motor.run_angle(2000, rotation_angle=500, wait=False)

    _angle = 0
    # turnToAngle(targetAngle=_angle, speed=100)

    gyroStraightWithDrive(distanceInCm=8*CM_PER_INCH, speed=1000, targetAngle=_angle, backward=True)
    # turnToAngle(targetAngle=180, speed=100, forceTurn=FORCETURN_LEFT)
    # gyroStraightWithDrive(distanceInCm=10*CM_PER_INCH, speed=1000)
    
    # right_med_motor.run_angle(speed=800, rotation_angle = 500)

def run2():
    resetGyro(0)
    _run2_internal()
