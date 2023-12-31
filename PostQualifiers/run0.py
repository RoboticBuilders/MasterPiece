from Utilities import *

def _3dCinemaAndTwoFacesDropoff():
    # Go forward to push the static arm, which then aligns against the 3D Cinema and drops off one audience in the two faces.
    #Alignment: To the left of the third black line from the wall. The attachment's yellow L-beam is pushed against the base arms yellow slope
    angle = 0
    gyroStraightWithDrive(distanceInCm = 25, speed = 500, targetAngle = angle) 
    gyroStraightWithDrive(distanceInCm = 25, speed = 300, targetAngle = angle,backward=True) 


def _run0():
    _3dCinemaAndTwoFacesDropoff()

def _pushRollingCameraLever():
    # We just push the static arm with the bucket to drop the lever

    angle = 0
    right_med_motor.run_angle(speed=2000, rotation_angle=-600)
    
    right_med_motor.run_angle(speed=2000, rotation_angle=600)

def _run0point5():
    _pushRollingCameraLever()

#runWithTiming(_run0,"3DCinema")
runWithTiming(_run0point5,"Lever")
#_run0point5()
