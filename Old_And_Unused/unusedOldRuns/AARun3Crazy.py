from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

# This version work with new attachment as of 10.23 with 37 seconds. Tested 10 times. Works 10 out of 10 times

RUN3_WAIT_ON=0
lightshow_arm_speed = 2000

def run3():
    turnToAngle(335, speed=400, oneWheelTurn=True)

    gyroStraightWithDrive(distanceInCm = 54, speed = 400, targetAngle = 335)

    turnToAngle(targetAngle=280, speed=400, oneWheelTurn=True)
    if RUN3_WAIT_ON == 1:
        wait(500)

    gyroStraightWithDrive(distanceInCm= 25, speed=400, targetAngle=280)

    turnToAngle(targetAngle=270, speed=400, oneWheelTurn=True)

    right_med_motor.run_angle(speed=400, rotation_angle=130, wait=False)
    gyroStraightWithDrive(distanceInCm= 22, speed=400, targetAngle=270)

    wait(1000)


    right_med_motor.run_angle(speed=400, rotation_angle=-130)

    gyroStraightWithDrive(distanceInCm=18, speed=200, targetAngle=270, backward=True)

    turnToAngle(targetAngle=330, speed=200)

    gyroStraightWithDrive(distanceInCm= 21, speed=200, targetAngle=330)

    wait(500)

    turnToAngle(targetAngle=265, speed=200)
    wait(500)

    left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=3710, wait=False)

    gyroStraightWithDrive(distanceInCm= 8, speed=200, targetAngle=270)
    wait(500)

    while(not left_med_motor.done()):
            wait(1)

    gyroStraightWithDrive(distanceInCm=24, speed=200, targetAngle=270, backward=True)

    drive_base.stop()

    left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-4430)

    left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=1620)

    drive_base.stop()

    gyroStraightWithDrive(distanceInCm=8, speed=200, targetAngle=270)

    left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-1440)

    turnToAngle(targetAngle=355, speed=200)

    gyroStraightWithDrive(distanceInCm=16, speed=200, targetAngle=355)

    turnToAngle(targetAngle=82, speed=200)

    gyroStraightWithDrive(distanceInCm=55, speed=400, targetAngle=82)

    turnToAngle(targetAngle=15, speed=200)

    gyroStraightWithDrive(distanceInCm=70, speed=400, targetAngle=15)





# turnToAngle(targetAngle=270, speed=400)

# left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=3710)
                
# gyroStraightWithDrive(distanceInCm=24, speed=200, targetAngle=270, backward=True)
       
# left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-4430)

# left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=1620)


runWithTiming(run3, "run3")



# if RUN3_WAIT_ON == 1:
#             wait(500)

