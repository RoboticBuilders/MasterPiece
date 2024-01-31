from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

# This version work with new attachment as of 10.29

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

        gyroStraightWithDrive(distanceInCm = 46, speed = 400, targetAngle = 330)

        turnToAngle(targetAngle=305, speed=200, oneWheelTurn=True)
        if RUN3_WAIT_ON == 1:
            wait(500)

        gyroStraightWithDrive(distanceInCm= 63, speed=300, targetAngle=305)


    # This is new code for doing immersive experience with Flushing
    def _executeImmersiveExperience(): 
        gyroStraightWithDrive(distanceInCm=33, speed=300, targetAngle=305, backward=True)
        turnToAngle(265, speed=200)
        gyroStraightWithDrive(distanceInCm=30, speed=300, targetAngle=265)

    def _executeLightShow():
        gyroStraightWithDrive(distanceInCm=12, speed=200, targetAngle=265, backward=True)
        turnToAngle(0, speed=200)
        gyroStraightWithDrive(distanceInCm=15, speed=200, targetAngle=0)
        turnToAngle(265, speed=200)
        gyroStraightWithDrive(distanceInCm=13, speed=200, targetAngle=265)
        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=3710)
        gyroStraightWithDrive(distanceInCm=27, speed=200, targetAngle=265, backward=True)
        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-4430)
        left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=1620)
        

     # This function does the lightshow mission by lifting up the arms.
    # def _executeLightShow():
    #     left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=3710)
    #     if RUN3_WAIT_ON == 1:
    #         wait(500)
        
    #     gyroStraightWithDrive(distanceInCm=27, speed=200, targetAngle=270, backward=True)
    #     if RUN3_WAIT_ON == 1:
    #         wait(1000)

    #     left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-4430)
    #     if RUN3_WAIT_ON == 1:
    #         wait(500)

    #     left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=1620)
    #     if RUN3_WAIT_ON == 1:
    #         wait(500)

    # # This is new code for doing immersive experience with Flushing
    # def _executeImmersiveExperience(): 
    #     gyroStraightWithDrive(distanceInCm=24, speed=100, targetAngle=270)
    #         # Check the Target angle above
    #     left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-1440)
    #     driveTillHsvRange(maxDistance=2400, speed=-30, sensor=left_color, hueRange = range(351, 357), saturationRange=range(64, 68), valueRange=range(64, 68) )
    #     turnToAngle(160, speed=200)
    #     gyroStraightWithDrive(distanceInCm=22, speed=200, targetAngle=160)
    #     turnToAngle(275, speed=200)
    #     gyroStraightWithDrive(distanceInCm=27, speed=300, targetAngle=275)



    # def _goHomeWithEmily():   
    #     gyroStraightWithDrive(distanceInCm=50, speed=600, targetAngle=275, backward=True)
    #     turnToAngle(16, speed=200)
    #     wait(100)
    #     gyroStraightWithDrive(distanceInCm=125, speed=600, targetAngle=16)


    # This is new code for doing Immersive Experience for accuratly using Color Sensor.
    # def _executeImmersiveExperience():   
    #     gyroStraightWithDrive(distanceInCm=4, speed=200, targetAngle=270)
        
    #     driveTillHsvRange(maxDistance=2400, speed=25, sensor=left_color, hueRange = range(351, 357), saturationRange=range(64, 68), valueRange=range(64, 68) )
    #     left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-1440)
    #     turnToAngle(160, speed=200)
    #     gyroStraightWithDrive(distanceInCm=12, speed=200, targetAngle=160)
    #     driveTillHsvRange(maxDistance=2400, speed=200,sensor=right_color, hueRange = range(47, 55), saturationRange=range(13, 19), valueRange=range(74, 82) )
    #     turnToAngle(275, speed=200)
    #     gyroStraightWithDrive(distanceInCm=27, speed=300, targetAngle=275)
    # def _goHomeWithEmily():   
    #     gyroStraightWithDrive(distanceInCm=50, speed=600, targetAngle=275, backward=True)
    #     turnToAngle(16, speed=200)
    #     wait(100)
    #     gyroStraightWithDrive(distanceInCm=125, speed=600, targetAngle=16)


    # # This function does the immersive experience mission.
    # def _executeImmersiveExperience():
    #     gyroStraightWithDrive(distanceInCm=8, speed=100, targetAngle=270)

    #     left_med_motor.run_angle(speed=lightshow_arm_speed, rotation_angle=-1440)
    #     #left_med_motor.run_angle(300, -1080)
    #     turnToAngle(160, speed=200)

    #     gyroStraightWithDrive(distanceInCm=24, speed=300, targetAngle=160)


    #     turnToAngle(275, speed=200)

    #     gyroStraightWithDrive(distanceInCm=27, speed=300, targetAngle=275)
    # # This function is when we go to homw 2 and we pick up Emily on the way back.
    # def _goHomeWithEmily():
    #     gyroStraightWithDrive(distanceInCm=50, speed=600, targetAngle=275, backward=True)

    #     turnToAngle(16, speed=200)
    #     wait(100)
        
    #     gyroStraightWithDrive(distanceInCm=125, speed=600, targetAngle=16)
    # This is function shows what the code for run3 is.
   
    def _codeForRun3():
        resetGyro(0)
        _positionInnovationProjectAndExpertsToMuseum()
        _executeImmersiveExperience()
        _executeLightShow()
       # _goHomeWithEmily()

    _codeForRun3()
# This is function runs the entire run.
run3()

        
