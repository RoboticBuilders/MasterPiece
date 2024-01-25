from Utilities import *

def goRightHometoLeft():
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance = 60, speed = 1000, backward = False, targetAngle = angle)
    # Pickup the expert
    
    angle = -2
    gyroStraightWithDriveWithAccurateDistance(distance = 110, speed = 1000, backward = False, targetAngle = angle,stop=Stop.COAST,slowDown=False)


def run1():
    resetRobot()
    goRightHometoLeft()

#runWithTiming(_dorun,"home2home")
