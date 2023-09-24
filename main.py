from Utilities import *

def run1():
    print("Add code to me!")

def run2():
    print("Add code to me!")

def run3():
    print("Add code to me!")

def run4():
    def _goToCraftCreator():
        gyroStraightWithDrive(distance = 13, speed = 500, targetAngle = 0)
        turnToAngle(absoluteAngle = -45, turnRate = 500)
        gyroStraightWithDrive(distance = 28, speed = 500, targetAngle = -45)

    def _doVirtualRealityArtist():
        print("Add code to me!")

    def _goToMovieSet():
        gyroStraightWithDrive(distance = 16, speed = 800, targetAngle = -45, backward = True)
        turnToAngle(absoluteAngle = -90, turnRate = 500)
        gyroStraightWithDrive(distance = 45, speed = 500, targetAngle = -90)
        turnToAngle(absoluteAngle = -135, turnRate = 500)
        gyroStraightWithDrive(distance = 10, speed = 500, targetAngle = -135)

    def _movieSetDropoffs():
        print("Add code to me!")

    def _goHome():
        gyroStraightWithDrive(distance = 10, speed = 500, targetAngle = -135, backward = True)
        turnToAngle(absoluteAngle = 110, turnRate = 500)
        gyroStraightWithDrive(distance = 75, speed = 1000, targetAngle = 110) 

    _goToCraftCreator()
    _doVirtualRealityArtist()
    _goToMovieSet()
    _movieSetDropoffs()
    _goHome()

def run5():
    print("Add code to me!")