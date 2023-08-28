from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

MM_PER_INCH = 25.4

def myFunc():
    robot.straight(300, Stop.HOLD, False)
    while not robot.distance_control.done():
        print("Waiting....")
    print("1....Done")
    robot.turn(-30)
    print(2)
    robot.straight(450)
    print(3)
    robot.turn()
    print(4)

# def AnyaRun():
#     resetRobot()
#     goStraight(450)
#     # robot.straight(450)
#     turnToAngle(-50)
#     # robot.turn(-50)
#     goStraight(280)
#     # robot.straight(290)
#     wait(10000)
#     robot.turn(87)
#     robot.settings(straight_speed=180, turn_rate=180)
#     robot.straight(200)
#     robot.settings(straight_speed=300, turn_rate=300)
#     left_med_motor.run_angle(-1000, 2600)
#     robot.straight(-240)
#     robot.turn(100)
#     robot.straight(850)

def AnyaRun():
    goStraight(MM_PER_INCH*20)
    turnToAngle(-45)
    driveTillLine(speed=300, distanceInCM=200, target_angle=-45, doCorrection=False)
    # goStraight(MM_PER_INCH*2)
    turnToAngle(45)
    goStraight(MM_PER_INCH*7.5)
    left_med_motor.run_angle(-1000, 2500)
    goStraight(MM_PER_INCH*-5)
    turnToAngle(-20)
    goStraight(MM_PER_INCH*-30)

def ArishaRun():
    right_med_motor.run_angle(-200, 4325)

def testGoStraight():
    goStraight(distance=1000, backward=False, straightSpeed=1000, straightAcceleration=100, wait=False)
    left_med_motor.run_angle(-1000, 2600, wait=False)
    
    while not robot.distance_control.done() or not left_med_motor.control.done():
        if(not robot.distance_control.done()): 
            print("Waiting for robot distance....")
        if(not left_med_motor.control.done()):
            print("Waiting for medium motor...")
    print("All Done!!!")
    turnToAngle(45)




print("Calling func now")
AnyaRun()
# robot.straight(distance=500, then=Stop.Hold, wait=True)
# left_med_motor.run_angle(-1000, 2600)
print("DONE")