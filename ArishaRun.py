from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

MM_PER_INCH = 25.4



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

def ArishaRun_M2():
    goStraight(600) 
    turnToAngle(30) 
    goStraight(100) 
    turnToAngle(-45) 
    #drive_base.settings(straight_speed=100, turn_rate=180)

    # turn back and forward
    goStraight(150)
    goStraight(-50)
    right_med_motor.run_angle(500, -2350) 
    goStraight(50)
    # right_med_motor.run_angle(500, -2300) 
    goStraight(-100)
    #go back
    turnToAngle(absoluteAngle=45, turnRate=100, turnAcceleration=100) 
    goStraight(-100)
    right_med_motor.run_angle(500, 2350) 

def ArishaRun_M1():
    left_med_motor.run_angle(800, 100)
    goStraight(350)
    right_med_motor.run_angle(800,1000)
    left_med_motor.run_angle(800,-100)
    goStraight(-350)
    right_med_motor.run_angle(800,-1000)




print("Calling func now")
ArishaRun_M1()
# AnyaRun()
# robot.straight(distance=500, then=Stop.Hold, wait=True)
# left_med_motor.run_angle(-1000, 2600)
print("DONE")