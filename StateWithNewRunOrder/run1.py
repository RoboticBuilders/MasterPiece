from Utilities import *

def goRightHometoLeft():
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance = 60, speed = 1000, backward = False, targetAngle = angle)

    # Pickup the expert
    angle = -4
    #Changed from 110 to 100 to make sure it doesn't hit into aligner
    gyroStraightWithDriveWithAccurateDistance(distance = 100, speed = 1000, backward = False, targetAngle = angle,stop=Stop.COAST,slowDown=False)


def goRightHometoLeftPickUpNoah():
    angle = 25
    gyroStraightWithDriveWithAccurateDistance(distance = 60, speed = 1000, backward = False, targetAngle = angle)
    angle=0
    gyroStraightWithDriveWithAccurateDistance(distance = 25, speed = 400, backward = False, targetAngle = angle, tillBlackLine=True)

    #waitForButtonPress()

    angle=10
    gyroStraightWithDriveWithAccurateDistance(distance = 31, speed = 1000, backward = False, targetAngle = angle)

    #waitForButtonPress()

    # Pickup the expert 
    angle = -20
    gyroStraightWithDriveWithAccurateDistance(distance = 40, speed = 1000, backward = False, targetAngle = angle,stop=Stop.COAST,slowDown=False)


def run1():
    resetRobot()
    goRightHometoLeft()

#waitForButtonPress()
#runWithTiming(run1,"run1")