from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

# This version is the new veriosn as of 11/14 without light show
RUN3_WAIT_ON=0


def run4():
    resetGyro(0)

    _angle = 335
    turnToAngle(_angle, speed=200, oneWheelTurn=True)

    gyroStraightWithDrive(distanceInCm = 52, speed = 400, targetAngle = _angle)

   # turnToAngle(targetAngle=270, speed=400, oneWheelTurn=True)
    #if RUN3_WAIT_ON == 1:
       # wait(500)

    #gyroStraightWithDrive(distanceInCm= 25, speed=400, targetAngle=270)

    turnToAngle(targetAngle=270, speed=200, oneWheelTurn=True)

    #right_med_motor.run_angle(speed=400, rotation_angle=130, wait=False)
    
    gyroStraightWithDrive(distanceInCm= 47, speed=400, targetAngle=270, slowDown=True)
    right_med_motor.run_angle(speed=200, rotation_angle=-130)

    wait(500)


    right_med_motor.run_angle(speed=200, rotation_angle=170)

    gyroStraightWithDrive(distanceInCm=47, speed=400, targetAngle=275, backward=True)

    _angle = 12
    turnToAngle(_angle, speed=200)
    gyroStraightWithDrive(distanceInCm=80, speed=400, targetAngle=_angle)

    _angle =0
    turnToAngle(_angle, speed=200)
    gyroStraightWithDrive(distanceInCm=45, speed=400, targetAngle=_angle)



# runWithTiming(run4, "run4")
#resetGyro(0)

#right_med_motor.run_angle(speed=500, rotation_angle=-100)

#wait(500)


#right_med_motor.run_angle(speed=500, rotation_angle=100)


# if RUN3_WAIT_ON == 1:
#             wait(500)



        
