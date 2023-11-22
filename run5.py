from Utilities import *

def run5():
    def _doRollingCameraAndDropOffAtMovieSet():
        angle = 2
        # Drive forward to do rolling camera
        gyroStraightWithDrive(distanceInCm = 45, speed = 300, targetAngle = angle)

        angle = 0
        # Drive towards the dropoff at movie set
        gyroStraightWithDrive(distanceInCm = 25, speed = 500, targetAngle = angle)

        # Pick up the expert
        #_positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP)
        
    def _goHomeAfterRollingCamera():
        angle = 355

        # Backoff from the movie set to drop off the expert and orange 
        # audience. 
        gyroStraightWithDrive(distanceInCm = 65, speed = 1000, targetAngle = angle, backward=True)

    def _dorun5():
        _doRollingCameraAndDropOffAtMovieSet()
        _goHomeAfterRollingCamera()
        #_resetAttachmentForNextRun()

    resetRobot()
    _dorun5() 