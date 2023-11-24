# NOTE NOTE: This is RUN1
# There are things in here called Run2* please ignore.

from Utilities import *
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def _run1_internal():
    #go to the movie set
    # gyroStraightWithDrive(distanceInCm=52, speed=300) # was 54
    drive_base.straight(distance=500)
    right_med_motor.run_angle(speed=2000, rotation_angle = -1000)
    
    #get camera in right position
    gyroStraightWithDrive(distanceInCm=18, speed=300, backward=True)

    turnToAngle(targetAngle=320, speed=200)
    right_med_motor.run_angle(2000, rotation_angle=800) # was 400
    #wait(1000)

    #turnToAngle(targetAngle=0, speed=200)
    right_med_motor.run_angle(2000, rotation_angle=300, wait=False)

    _angle = 0
    # turnToAngle(targetAngle=_angle, speed=100)

    gyroStraightWithDrive(distanceInCm=8*CM_PER_INCH, speed=1000, targetAngle=_angle, backward=True)
    # turnToAngle(targetAngle=180, speed=100, forceTurn=FORCETURN_LEFT)
    # gyroStraightWithDrive(distanceInCm=10*CM_PER_INCH, speed=1000)
    
    # right_med_motor.run_angle(speed=800, rotation_angle = 500)



def run1():
    resetGyro(0)
    #run2_testSide()
    _run1_internal()


# This is code that was outside.
def initializeRun1():
    print("Calling func now")

    resetRobot()
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    #oldrun1()
    run1()
    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    print("DONE")

# initializeRun1()
# gyroStraightWithDrive(distanceInCm=45, speed=300)
# run_time(speed=100, time=3000)
# drive_base.straight(distance=520)
# driveTillHsvRange(hueRange=range(49,51), saturationRange=range(45,47), valueRange=range(79,81))
# testHsv(sensor=right_color)