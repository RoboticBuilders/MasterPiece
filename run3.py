from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

# This version is the new veriosn as of 11/14 without light show
RUN3_WAIT_ON=0


def run3():
    resetGyro(0)

    turnToAngle(335, speed=200, oneWheelTurn=True)

    gyroStraightWithDrive(distanceInCm = 52, speed = 400, targetAngle = 335)

   # turnToAngle(targetAngle=270, speed=400, oneWheelTurn=True)
    #if RUN3_WAIT_ON == 1:
       # wait(500)

    #gyroStraightWithDrive(distanceInCm= 25, speed=400, targetAngle=270)

    turnToAngle(targetAngle=270, speed=200, oneWheelTurn=True)

    #right_med_motor.run_angle(speed=400, rotation_angle=130, wait=False)
    
    gyroStraightWithDrive(distanceInCm= 47, speed=400, targetAngle=270, slowDown=True)
    right_med_motor.run_angle(speed=200, rotation_angle=100)

    wait(500)


    right_med_motor.run_angle(speed=200, rotation_angle=-100)

    gyroStraightWithDrive(distanceInCm=45, speed=600, targetAngle=275, backward=True)

    turnToAngle(17, speed=200)
    wait(100)
        
    gyroStraightWithDrive(distanceInCm=125, speed=600, targetAngle=17)



#runWithTiming(run3, "run3")



# if RUN3_WAIT_ON == 1:
#             wait(500)



        
