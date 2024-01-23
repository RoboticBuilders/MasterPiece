from Utilities import *

def run5():
    def _doRollingCameraAndDropOffAtMovieSet():
        angle = 2
        # Drive forward to do rolling camera
        gyroStraightWithDrive(distanceInCm = 27, speed = 300, targetAngle = angle)
        gyroStraightWithDrive(distanceInCm = 5, speed = 100, targetAngle = angle)
        
        angle = -4
        # Drive towards the dropoff at movie set
        gyroStraightWithDrive(distanceInCm = 30, speed = 800, targetAngle = angle)

        
    def _goHomeAfterRollingCamera():
        angle = -4

        # Backoff from the movie set to drop off the expert and orange 
        # audience. 
        gyroStraightWithDrive(distanceInCm = 65, speed = 1000, targetAngle = angle, backward=True)
        
    def _dorun5():
        _doRollingCameraAndDropOffAtMovieSet()
        _goHomeAfterRollingCamera()
        #_resetAttachmentForNextRun()

    resetRobot()
    _dorun5()

waitForButtonPress()
run5()