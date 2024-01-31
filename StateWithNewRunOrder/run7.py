from Utilities import *

def run7():
    def _doRollingCameraAndDropOffAtMovieSet():
        angle = 0
        # Drive forward to do rolling camera
        gyroStraightWithDrive(distanceInCm = 27, speed = 300, targetAngle = angle)
        gyroStraightWithDrive(distanceInCm = 5, speed = 100, targetAngle = angle)
        
        angle = -6
        # Drive towards the dropoff at movie set
        gyroStraightWithDrive(distanceInCm = 30, speed = 800, targetAngle = angle)

        
    def _goHomeAfterRollingCamera():
        angle = -4

        # Backoff from the movie set to drop off the expert and orange 
        # audience. 
        gyroStraightWithDrive(distanceInCm = 65, speed = 1000, targetAngle = angle, backward=True)

    def _goHomeAfterRollingCameraWithCurve():
        angle = -8
        gyroStraightWithDrive(distanceInCm = 20, speed = 1000, backward = True, targetAngle = angle, slowDown = False)
        drive_base.settings(1000, 1000, 1000, 1000)
        #drive_base.curve(radius = -1750, angle = -20)
        drive_base.curve(radius = -300, angle = -70)

    def _dorun7():
        _doRollingCameraAndDropOffAtMovieSet()
        _goHomeAfterRollingCameraWithCurve()
        #_resetAttachmentForNextRun()

    resetRobot()
    _dorun7()

