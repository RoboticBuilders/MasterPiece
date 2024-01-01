from Utilities import *

TURN_SPEED = 300
DRIVE_SPEED = 400

def threeDCinema():
    angle = 0
    gyroStraightWithDrive(distanceInCm = 20, speed = DRIVE_SPEED, targetAngle = angle)

    angle = -55
    turnToAngle(targetAngle = angle, speed = TURN_SPEED)
    gyroStraightWithDrive(distanceInCm = 20, speed = DRIVE_SPEED, targetAngle = angle)

    angle = 0
    turnToAngle(targetAngle = angle, speed = 1000)

def theaterSceneChange():
    angle = -45
    turnToAngle(targetAngle = angle, speed = TURN_SPEED)
    gyroStraightWithDrive(distanceInCm = 25, speed = DRIVE_SPEED, targetAngle = angle, backward = True)

    angle = 27
    turnToAngle(targetAngle = angle, speed = TURN_SPEED)
    gyroStraightWithDrive(distanceInCm = 60, speed = DRIVE_SPEED, targetAngle = angle)
    
    angle = -45
    turnToAngle(targetAngle = angle, speed = TURN_SPEED)
    gyroStraightWithDrive(distanceInCm = 20, speed = 200, targetAngle = angle)

    angle = -90
    turnToAngle(targetAngle = angle, speed = 200)
    gyroStraightWithDrive(distanceInCm = 12, speed = 300, targetAngle = angle, backward = True)

def goHome():
    angle = -145
    turnToAngle(targetAngle = angle, speed = 750)
    gyroStraightWithDrive(distanceInCm = 60, speed = 1000, targetAngle = angle)

def run3():
    threeDCinema()
    theaterSceneChange()
    goHome()

#run3()
# gyroStraightWithDrive(distanceInCm = 28, speed = DRIVE_SPEED, targetAngle = 0)