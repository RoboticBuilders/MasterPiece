from pybricks.tools import wait
from Utilities import *

def run4_new_arm():
    resetGyro(0)

    _angle=0
    gyroStraightWithDrive(distanceInCm = 7, speed = 200, targetAngle = _angle) 

    _angle = 335
    turnToAngle(_angle, speed=200, oneWheelTurn=True)

    # Changed 11/16: 52 to 54 to avoid hitting the Sound Mixer
    gyroStraightWithDrive(distanceInCm = 54, speed = 400, targetAngle = _angle) 

    turnToAngle(targetAngle=270, speed=200, oneWheelTurn=True)
    
    gyroStraightWithDrive(distanceInCm= 47, speed=400, targetAngle=270, slowDown=True)
    
    right_med_motor.run_angle(500, -1000)
    wait(500)
    right_med_motor.run_angle(500, 1000)

    gyroStraightWithDrive(distanceInCm=47, speed=400, targetAngle=275, backward=True)

    _angle = 12
    turnToAngle(_angle, speed=200)
    gyroStraightWithDrive(distanceInCm=80, speed=400, targetAngle=_angle)

    _angle = 0
    turnToAngle(_angle, speed=800)
    gyroStraightWithDrive(distanceInCm=45, speed=800, targetAngle=_angle)