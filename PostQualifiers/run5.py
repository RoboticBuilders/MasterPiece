from Utilities import *

def run5():
    def _doRollingCameraAndDropOffAtMovieSet():
        angle = 2
        # Drive forward to do rolling camera
        gyroStraightWithDrive(distanceInCm = 27, speed = 300, targetAngle = angle)
        gyroStraightWithDrive(distanceInCm = 5, speed = 100, targetAngle = angle)
        run6PositionPickUpExpertAttachment(position = RUN6_PICKUP_EXPERT_ATTACHMENT_UP, wait = False, speed = 150)
        gyroStraightWithDrive(distanceInCm = 13, speed = 400, targetAngle = angle)

        angle = 0
        # Drive towards the dropoff at movie set
        gyroStraightWithDrive(distanceInCm = 25, speed = 700, targetAngle = angle)

        # Pick up the expert
        #_positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP)
        
    def _goHomeAfterRollingCamera():
        angle = 355

        # Backoff from the movie set to drop off the expert and orange 
        # audience. 
        gyroStraightWithDrive(distanceInCm = 55, speed = 1000, targetAngle = angle, backward=True)
        run6PositionPickUpExpertAttachment(position = RUN6_PICKUP_EXPERT_ATTACHMENT_DOWN, wait = False, speed = 1000)
        gyroStraightWithDrive(distanceInCm = 10, speed = 1000, targetAngle = angle, backward=True)

    def _dorun5():
        _doRollingCameraAndDropOffAtMovieSet()
        _goHomeAfterRollingCamera()
        #_resetAttachmentForNextRun()

    resetRobot()
    _dorun5() 