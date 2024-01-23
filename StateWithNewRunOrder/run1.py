from Utilities import *

def goRightHometoLeft():
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance = 75, speed = 500, backward = False, targetAngle = angle,stop=Stop.COAST,slowDown=False)
    # Pickup the expert
    
    angle = -20
   
    gyroStraightWithDriveWithAccurateDistance(distance = 90, speed = 1000, backward = False, targetAngle = angle)


def run1():
    resetRobot()
    goRightHometoLeft()

#runWithTiming(_dorun,"home2home")
