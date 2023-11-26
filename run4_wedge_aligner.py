from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *



def run4_wedge_aligner():
    _angle=-30
    resetGyro(_angle)

    gyroStraightWithDrive(distanceInCm = 63, speed = 400, targetAngle = _angle)

    # _angle = 335
    # turnToAngle(_angle, speed=200, oneWheelTurn=True)

    # Changed 11/16: 52 to 54 to avoid hitting the Sound Mixer
    # gyroStraightWithDrive(distanceInCm = 50, speed = 400, targetAngle = _angle) 
    # robot.straight(distance=580)

    turnToAngle(targetAngle=275, speed=200, oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm = 47, speed=200, targetAngle=270, slowDown=True)
    
    # Now drop off the expert.
    right_med_motor.run_angle(speed=1000, rotation_angle=1200)
    # wait(500)
    right_med_motor.run_angle(speed=1000, rotation_angle=-1200)

    # backoff.
    gyroStraightWithDrive(distanceInCm=10, speed=400, targetAngle=270, backward=True)
    gyroStraightWithDrive(distanceInCm=34, speed=400, targetAngle=275, backward=True)

    # Code after this is new code.
    # gyroStraightWithDrive(distanceInCm=5, speed=400, targetAngle=275, backward=True)
    angle = 8
    turnToAngle(angle, speed=500)  
    gyroStraightWithDrive(distanceInCm=98, speed=1000, targetAngle=angle)

#run4()
# waitForButtonPress()
# runWithTiming(run4_wedge_aligner, "Run 4 Wedge Aligner")

