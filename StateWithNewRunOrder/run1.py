from Utilities import *

def goRightHometoLeft():
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance = 60, speed = 1000, backward = False, targetAngle = angle,stop=Stop.COAST)

    # Pickup the expert
    # 1/30/2024 - Changed from -4 to -2
    angle = -2
    #Changed from 110 to 105 to make sure it doesn't hit into aligner
    gyroStraightWithDriveWithAccurateDistance(distance = 50, speed = 1000, backward = False, targetAngle = angle,stop=Stop.COAST,slowDown=False)

    angle = -30
    #Changed from 110 to 105 to make sure it doesn't hit into aligner
    gyroStraightWithDriveWithAccurateDistance(distance = 60, speed = 1000, backward = False, targetAngle = angle,stop=Stop.COAST,slowDown=False)


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

