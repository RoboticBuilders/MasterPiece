from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

RUN3_WAIT_ON=0
lightshow_arm_speed = 2000

def run3():

    # This function drops of the innovation project, expert, and orange person to the museum.
    def _positionInnovationProjectAndExpertsToMuseum():

        #left_med_motor.run_angle(300, 360 * -8)

        turnToAngle(330, speed=200, oneWheelTurn=True)

        gyroStraightWithDrive(distanceInCm = 48, speed = 300, targetAngle = 330)

        turnToAngle(targetAngle=305, speed=200, oneWheelTurn=True)
        if RUN3_WAIT_ON == 1:
            wait(500)

        gyroStraightWithDrive(distanceInCm=60, speed=300, targetAngle=305)

        turnToAngle(targetAngle=270, speed=200, oneWheelTurn=True)
        if RUN3_WAIT_ON == 1:
            wait(500)

    # This function does the lightshow mission by lifting up the arms.
    def _executeLightShow():
        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=360 * 11)
        if RUN3_WAIT_ON == 1:
            wait(500)
        
        gyroStraightWithDrive(distanceInCm=27, speed=300, targetAngle=270, backward=True)
        if RUN3_WAIT_ON == 1:
            wait(1000)

        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=360 * -11)
        if RUN3_WAIT_ON == 1:
            wait(500)

        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=360 * 4)
        if RUN3_WAIT_ON == 1:
            wait(500)


    # This function does the immersive experience mission.
    def _executeImmersiveExperience():
        gyroStraightWithDrive(distanceInCm=7, speed=300, targetAngle=270)

        left_med_motor.run_angle(300, 360 * -2)
        turnToAngle(160, speed=200)

        gyroStraightWithDrive(distanceInCm=25, speed=300, targetAngle=160)


        turnToAngle(275, speed=200)

        gyroStraightWithDrive(distanceInCm=27, speed=300, targetAngle=275)
    # This function is when we go to homw 2 and we pick up Emily on the way back.
    def _goHomeWithEmily():
        gyroStraightWithDrive(distanceInCm=50, speed=300, targetAngle=275, backward=True)

        turnToAngle(15, speed=200)

        gyroStraightWithDrive(distanceInCm=110, speed=341, targetAngle=15)
    # This is function shows what the code for run3 is.
    def _codeForRun3():
        resetGyro(0)
        _positionInnovationProjectAndExpertsToMuseum()
        _executeLightShow()
        _executeImmersiveExperience()
        _goHomeWithEmily()

    _codeForRun3()
# This is function runs the entire run.
#run3()

        