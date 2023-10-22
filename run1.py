from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

# This is the main entry point for Run1. Driver is calling this method
def run1():

    #3D Cinema
    do3DCinema()

    
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
    #driveTillLine(speed=-200, doCorrection=False)
   
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

def do3DCinema():
    left_med_motor.run_angle(600, 150, wait=False)
    gyroStraightWithDrive(9 * CM_PER_INCH, targetAngle=0, speed=300)
    #gyroStraightWithDrive(distanceInCm=17, targetAngle=0, speed=500)
    left_med_motor.run_angle(500, -150)
    left_med_motor.run_angle(500, 150)
    gyroStraightWithDrive(distanceInCm=-13, targetAngle=0, speed=500)

# This is code that was outside.
def initializeRun1():
    print("Calling func now")

    resetRobot()
    stopwatch = StopWatch()
    start_time = stopwatch.time()
    #time.ticks_ms()  
    #ArishaRun_M2()
    #ArishaRun_M1andM2()
    # ArishaRun_M1andM2_newgyroStr()
    #staticAttachmentTest()
    # staticAttachmentTest2()
    # staticAttachmentTestDriveTillLine()
    # resetGyro(angle=90)
    # driveTillColor(Color.BLUE)
    #driveTillLine(speed=150, doCorrection=False, sensor=left_color, blackOrWhite="Black")
    #MissionM1_M2_pickupNoah()
    run1()
    # MissionM1_M2_pickupNoah_Aligner()
    # right_med_motor.run_angle(speed=1000, rotation_angle=-300) 
    # gyroStraightWithDrive2(distanceInCm=15, targetAngle=0)
    # wait(1000)
    # gyroStraightWithDrive2(distanceInCm=15, targetAngle=0)
    # goStraight(distance=-50)
    # print("Second call now ----------------------------")
    # wait(1500)
    # gyroStraightWithDrive(distanceInCm=-5, targetAngle=0)
    # gyroStraightWithDrive(100, speed=300, targetAngle=0)
    #testHsv()
    #driveTillHueRange(214, 230, left_color)
    # turnToAngle(-90)
    # goStraight(240)
    # wait(5000)
    #driveTillLine(speed=150, doCorrection=False, sensor=right_color, blackOrWhite="White")
    #driveTillBlackLine(speed=200,distanceInCM=100, target_angle=0)
    #testHsv()
    # testColor()
    #bigger gear
    # end_time = stopwatch.time()
    # right_med_motor.run_angle(1000, 1300) 
    # right_med_motor.run_angle(1000, -1300) 
    #small gears
    # right_med_motor.run_angle(1000, 300) 
    # end_time = stopwatch.time()
    # right_med_motor.run_angle(1000, -300) 
    # right_med_motor.run_angle(1000, 300) 
    #logMessage("Time for run {} time(ms): {}".format(str(run), str(time.ticks_diff(end_time, start_time))), level=0)
    # MissionM1_M2_pickupNoah()
    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")
    #right_med_motor.run_angle(800, -300) 
    right_med_motor.run_angle(1000, 1200) 

    # AnyaRun()
    # robot.straight(distance=500, then=Stop.Hold, wait=True)

    print("DONE")


# initializeRun1()
