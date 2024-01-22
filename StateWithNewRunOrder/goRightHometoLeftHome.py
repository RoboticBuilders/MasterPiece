from Utilities import *

def goRightHometoLeft():
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance = 100, speed = 500, backward = False, targetAngle = angle,stop=Stop.COAST,slowDown=False)
    # Pickup the expert
    
    angle = -15
   
    gyroStraightWithDriveWithAccurateDistance(distance = 80, speed = 1000, backward = False, targetAngle = angle)


def dohome2home():
    resetRobot()
    goRightHometoLeft ()

#runWithTiming(_dorun,"home2home")
