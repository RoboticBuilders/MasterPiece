from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

def squareTest():
    turnspeed = 500
    driveTillDistance(distanceinCM=20, speed=300)
    turnToAngle(targetAngle=90, turn_rate=turnspeed)

    driveTillDistance(distanceinCM=20, speed=300)
    turnToAngle(targetAngle=180, turn_rate=turnspeed)

    driveTillDistance(distanceinCM=20, speed=300)
    turnToAngle(targetAngle=270, turn_rate=turnspeed)

    driveTillDistance(distanceinCM=20, speed=300)
    turnToAngle(targetAngle=0, turn_rate=turnspeed)

    return

def turnTest():

    angle = 0
    while True:
        angle = angle  + 45
        if angle > 360:
            angle = angle % 360
        turnToAngle(targetAngle=angle)
        wait(500)
    
    '''
    angle = 90
    turn = FORCETURN_RIGHT
    while True:
        turnToAngle(targetAngle=angle, forceTurn=turn)
        if turn==FORCETURN_LEFT:
            turn = FORCETURN_RIGHT
            angle = 90
        else:
            turn = FORCETURN_LEFT
            angle = 0
        wait(500)
    '''
def testDriveStraight():
    gyroStraightWithDrive(distanceInCm=50, speed=300, targetAngle=0)
    gyroStraightWithDrive(distanceInCm=50, speed=300, backward=True, targetAngle=0)
    gyroStraightWithDrive(distanceInCm=50, speed=300, targetAngle=0)
    gyroStraightWithDrive(distanceInCm=50, speed=300, backward=True, targetAngle=0)

def testDriveTillBlackline():
    gyroStraightWithDrive(distanceInCm=25, speed=500, targetAngle=0)
    driveTillBlackLine(speed=300, distanceInCM=25, target_angle=0)
    gyroStraightWithDrive(distanceInCm=10, speed=300, targetAngle=0)
    turnToAngle(targetAngle=90)
    gyroStraightWithDrive(distanceInCm=10, speed=400, targetAngle=90, backward=True)
    hub.imu.reset_heading(90)
    
    followBlackLine(speed=400, distance=170, control_color=50, edge=LINE_FOLLOWER_EDGE_RIGHT)
    turnToAngle(targetAngle=270)
    followBlackLine(speed=400, distance=170, control_color=50, edge=LINE_FOLLOWER_EDGE_LEFT)

    #gyroStraightWithDrive(distance=200, speed=400, targetAngle=90)
    #gyroStraightWithDrive(distance=160, speed=400, targetAngle=90, backward=True)

    #basicgyrostraightwithDrive(distance=2, speed=300, targetAngle=0)
    #basicgyrostraightwithDrive(distance=2, speed=300, targetAngle=0, backward=True)
    #basicgyrostraightwithDrive(distance=20, speed=800, targetAngle=0, backward=True)
    #basicgyrostraightwithDrive(distance=20, speed=800, targetAngle=0)
    
    #drive_base.straight(100, Stop.COAST)

def printColorValues():
    while True:
        print(getReflectedLight())

def testFollowBlackLine():
    #driveTillBlackLine(speed=300, distanceInCM=20, target_angle=0)
    #gyroStraightWithDrive(distance=10, speed=100, targetAngle=0)
    #turnToAngle(targetAngle=90, speed=300)
    followBlackLine(speed=300, distance=160, control_color=50, edge=LINE_FOLLOWER_EDGE_RIGHT, gain=0.3)
    #followBlackLine(speed=300, distance=160, control_color=50, edge=LINE_FOLLOWER_EDGE_LEFT, gain=1)

def runUntilStall():
    drive_base.drive(200, 0)
    while(drive_base.stalled() == False):
        continue
    print("Drive baases stopped")
    drive_base.stop()

def printHSVValues(sensor=left_color):
    while  True:
        print("(h,s,v) = {}, color: {}".format(sensor.hsv(), sensor.color()))
   
initializeAndWaitForRobotReady()
hub.imu.reset_heading(90)
#squareTest()
#turnTest()
#testDriveStraight()
#testDriveTillBlackline()
#printColorValues()
#testPositionUtil()
#testFollowBlackLine()
#runUntilStall()
printHSVValues()

