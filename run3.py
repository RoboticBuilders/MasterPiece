from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

# This version work with new attachment as of 10.23 with 37 seconds. Tested 10 times. Works 10 out of 10 times

RUN3_WAIT_ON=0
lightshow_arm_speed = 2000

def armdown():
    armdown = 3350

def armup():
    armup = -3350



def run3():

    # This function drops of the innovation project, expert, and orange person to the museum.
    def _positionInnovationProjectAndExpertsToMuseum():

        #left_med_motor.run_angle(300, 360 * -8)

        turnToAngle(330, speed=200, oneWheelTurn=True)

        gyroStraightWithDrive(distanceInCm = 48, speed = 400, targetAngle = 330)

        turnToAngle(targetAngle=305, speed=300, oneWheelTurn=True)
        if RUN3_WAIT_ON == 1:
            wait(500)

        gyroStraightWithDrive(distanceInCm= 56.5, speed=300, targetAngle=305)

        turnToAngle(targetAngle=270, speed=200, oneWheelTurn=True)
        
        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=3710, wait=False)
        
        wait(500)

        drive_base.stop()
        wait(500)
        if RUN3_WAIT_ON == 1:
            wait(500)

    # This function does the lightshow mission by lifting u7 the arms.
    def _executeLightShow():
        gyroStraightWithDrive(distanceInCm=15, speed=200, targetAngle=270)
        if RUN3_WAIT_ON == 1:
            wait(500)
        
        gyroStraightWithDrive(distanceInCm=40, speed=200, targetAngle=270, backward=True)
        if RUN3_WAIT_ON == 1:
            wait(1000)

        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-4790)
        if RUN3_WAIT_ON == 1:
            wait(500)

        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=1620)
        drive_base.stop()
        #gyroStraightWithDrive(distanceInCm=5, speed=1000, targetAngle=265, backward=True)
        wait(500)

        if RUN3_WAIT_ON == 1:
            wait(500)


    # This function does the immersive experience mission.
    def _executeImmersiveExperience():
        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-1440, wait=False)
        
        gyroStraightWithDrive(distanceInCm=7, speed=200, targetAngle=270)

        #left_med_motor.run_angle(300, -1080)
        turnToAngle(160, speed=200)

        gyroStraightWithDrive(distanceInCm=23, speed=250, targetAngle=160)


        turnToAngle(275, speed=200)

        gyroStraightWithDrive(distanceInCm=27, speed=300, targetAngle=275)
    # This function is when we go to homw 2 and we pick up Emily on the way back.
    def _goHomeWithEmily():
        gyroStraightWithDrive(distanceInCm=45, speed=600, targetAngle=275, backward=True)

        turnToAngle(17, speed=200)
        wait(100)
        
        gyroStraightWithDrive(distanceInCm=125, speed=600, targetAngle=17)
    # This is function shows what the code for run3 is.
    def _codeForRun3():
        resetGyro(0)
        _positionInnovationProjectAndExpertsToMuseum()
        _executeLightShow()
        _executeImmersiveExperience()
        _goHomeWithEmily()

    _codeForRun3()
# This is function runs the entire run.
#runWithTiming(run3, 'run3')

        
