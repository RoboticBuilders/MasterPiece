from Utilities import *

'''
ALIGNMENT: 2nd black line from left home on close wall
'''

def run1():
    gyroStraightWithDrive(distanceInCm = 10, speed = 300, targetAngle = 0)
    turnToAngle(targetAngle = 45, speed = 300)

    gyroStraightWithDrive(distanceInCm = 25, speed = 300, targetAngle = 45)
    gyroStraightWithDrive(distanceInCm = 10, speed = 100, targetAngle = 45)

    turnToAngle(targetAngle = 60, speed = 150)
    turnToAngle(targetAngle = 45, speed = 150)

    gyroStraightWithDrive(distanceInCm = 25, speed = 300, targetAngle = 45, backward = True)
    turnToAngle(targetAngle = -105, speed = 1000, forceTurn = FORCETURN_LEFT)
    gyroStraightWithDrive(distanceInCm = 20, speed = 1000, targetAngle = -105)

run1()