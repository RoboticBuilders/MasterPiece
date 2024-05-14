from Utilities import *

def _3dCinemaAndTwoFacesDropoff():
    # Go forward to push the static arm, which then aligns against the 3D Cinema and drops off one audience in the two faces.
    #Alignment: To the left of the third black line from the wall. The attachment's yellow L-beam is pushed against the base arms yellow slope
    angle = 0
    gyroStraightWithDrive(distanceInCm = 25, speed = 400, targetAngle = angle) 
    gyroStraightWithDrive(distanceInCm = 20, speed = 300, targetAngle = angle,backward=True) 

def run4():
    resetRobot()
    _3dCinemaAndTwoFacesDropoff()

#runWithTiming(run1,"3DCinema")

#runWithTiming(_run1,"3DCinema")
#runWithTiming(_run0point5,"Lever")
#_run0point5()


