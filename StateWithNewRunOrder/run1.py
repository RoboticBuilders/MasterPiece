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

def goRightHometoLeftBackward():
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance = 60, speed = 1000, backward = True, targetAngle = angle,stop=Stop.COAST)

    # Pickup the expert
    # 1/30/2024 - Changed from -4 to -2
    angle = -2
    #Changed from 110 to 105 to make sure it doesn't hit into aligner
    gyroStraightWithDriveWithAccurateDistance(distance = 50, speed = 1000, backward = True, targetAngle = angle,stop=Stop.COAST,slowDown=False)

    angle = -30
    #Changed from 110 to 105 to make sure it doesn't hit into aligner
    gyroStraightWithDriveWithAccurateDistance(distance = 60, speed = 1000, backward = True, targetAngle = angle,stop=Stop.COAST,slowDown=False)

def run1():
    resetRobot()
    goRightHometoLeft()

