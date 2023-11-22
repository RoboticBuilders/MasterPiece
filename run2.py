from Utilities import *
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run2():
    resetGyro(0)
    gyroStraightWithDrive(distanceInCm=38, speed=350)
    #right_med_motor.run_angle(speed=1000, rotation_angle = -1300, wait=False) # was 1000
    gyroStraightWithDrive(distanceInCm=10, speed=250) 
    right_med_motor.run_angle(speed=2000, rotation_angle = -1300, wait= False)
    gyroStraightWithDrive(distanceInCm=7, speed=250) 
    #come back home
    # total was 48
    # gyroStraightWithDrive(distanceInCm=27, speed=500, backward=True, targetAngle=0)
    # robot.turn(45)
    # robot.straight(-100)
    gyroStraightWithDrive(distanceInCm=48, speed=500, backward=True, targetAngle=0)
    right_med_motor.run_angle(speed=2000, rotation_angle = 1300)

# This is code that was outside.
def initializeRun2():
    print("Calling func now")

    resetRobot()
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    #oldrun1()
    run2()
    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    print("DONE")

initializeRun2()