from pybricks.tools import wait
from Utilities import *


def run4():
    resetGyro(0)

    _angle=0
    gyroStraightWithDrive(distanceInCm = 7, speed = 200, targetAngle = _angle) 

    _angle = 335
    turnToAngle(_angle, speed=200, oneWheelTurn=True)

    # Changed 11/16: 52 to 54 to avoid hitting the Sound Mixer
    gyroStraightWithDrive(distanceInCm = 52, speed = 400, targetAngle = _angle) 
    turnToAngle(targetAngle=270, speed=200, oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm = 47, speed=400, targetAngle=270, slowDown=True)
    
    # Now drop off the expert.
    right_med_motor.run_angle(speed=1000, rotation_angle=1200)
    wait(500)
    right_med_motor.run_angle(speed=1000, rotation_angle=-1200)

    # backoff.
    gyroStraightWithDrive(distanceInCm=10, speed=400, targetAngle=270, backward=True)
    gyroStraightWithDrive(distanceInCm=37, speed=400, targetAngle=275, backward=True)

    # Code after this is new code.
    # gyroStraightWithDrive(distanceInCm=5, speed=400, targetAngle=275, backward=True)
    angle = 8
    turnToAngle(angle, speed=500)  
    gyroStraightWithDrive(distanceInCm=90, speed=1000, targetAngle=angle)

#run4()

