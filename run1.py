from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.tools import wait, StopWatch
from Utilities import *

# This is the main entry point for Run1. Driver is calling this method
def run1():
    resetGyro(0)
    
    #3D Cinema
    do3DCinema()

    # Scene Change
    doSceneChange()
   
    pickupNoahExpert()

def do3DCinema():
    left_med_motor.run_angle(600, 150, wait=False)
    gyroStraightWithDrive(9 * CM_PER_INCH, targetAngle=0, speed=300)
    #gyroStraightWithDrive(distanceInCm=17, targetAngle=0, speed=500)
    left_med_motor.run_angle(500, -150)
    left_med_motor.run_angle(500, 150)
    gyroStraightWithDrive(distanceInCm=-13, targetAngle=0, speed=500)

def doSceneChange():
    #go to M2
    turnToAngle(90) 
    #goStraight(218) #218mm
    left_med_motor.run_angle(500, -150, wait=False)
    gyroStraightWithDrive(distanceInCm=19, targetAngle=90)
    driveTillHsvRange(maxDistance=3*MM_PER_INCH, sensor=left_color, hueRange = range(214, 230) )
    turnToAngle(0) 
    gyroStraightWithDrive(7*CM_PER_INCH, targetAngle=0)
    left_med_motor.run_angle(speed=500, rotation_angle=150, wait=False)
    #gyroStraightWithDrive(9*CM_PER_INCH, targetAngle=0)
    #wait(3000)
    gyroStraightWithDrive(7*CM_PER_INCH, targetAngle=0)
    driveTillLine(speed=200, doCorrection=False, sensor=left_color, blackOrWhite="Black")
    # gyroStraightWithDrive(distanceInCm=3, targetAngle=0)
    #wait(10000)
    #Execute M2
    turnToAngle(-45) 
    gyroStraightWithDrive(distanceInCm=13, targetAngle=-45)
    right_med_motor.run_angle(speed=800, rotation_angle = -1300) # was 1000

def pickupNoahExpert():
    # STRATEGY to pick up Noah
    gyroStraightWithDrive(-15, targetAngle=-45, speed=500)
    right_med_motor.run_angle(speed=1000, rotation_angle = 300,wait=False) # was 1000
    # wait(3000)

    # wait(3000)
    turnToAngle(45, oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=8, targetAngle=45, speed=500)  ## was 6 now is 8 cm
    turnToAngle(120)
    left_med_motor.run_angle(speed= 500, rotation_angle = -150, wait=False)


    gyroStraightWithDrive(30, targetAngle=100,speed=300)
    #wait(3000)  ## we were doing 25 instead of 27 cm of go back.
    turnToAngle(175, forceTurn=FORCETURN_RIGHT)
    #wait(3000)
    gyroStraightWithDrive(35, targetAngle=175,speed=300)  ## we were doing 25 instead of 27 cm of go forward.
    turnToAngle(-120)
    gyroStraightWithDrive(50, targetAngle=-120, speed=1000)

# This is code that was outside.
def initializeRun1():
    print("Calling func now")

    resetRobot()
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    run1()

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    right_med_motor.run_angle(1000, 1200)

    print("DONE")

#run1()
# initializeRun1()
