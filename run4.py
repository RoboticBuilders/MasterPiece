from Utilities import *

def run4():
    def _doRollingCameraAndDropOffAtMovieSet():
        angle = 0
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

    def _resetAttachmentForNextRun():
        # Reset attachment for the next run. 
        # Comment in the main program.
        _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP)

    def _dorun4():
        _doRollingCameraAndDropOffAtMovieSet()
        _goHomeAfterRollingCamera()
        #_resetAttachmentForNextRun()

    resetRobot()
    _dorun4() 

def run45():
    # pickup Expert Attachment constants
    PICKUP_EXPERT_ATTACHMENT_DOWN = 1
    PICKUP_EXPERT_ATTACHMENT_UP = 2

    # Expects the arm to start down.
    def _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_DOWN, wait=True):
        if position == PICKUP_EXPERT_ATTACHMENT_DOWN:
            right_med_motor.run_target(500, 175, Stop.HOLD, wait)
        else:
            right_med_motor.run_target(300, -35, Stop.HOLD, wait)

    def _positionChicken():
        left_med_motor.run_angle(-500, 950)
    
    def _pickupExpert():
        angle = 0

        # Bring down attachment.
        _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_DOWN, wait=False)

        # drive forward before picking up arm
        gyroStraightWithDrive(distanceInCm = 23, speed = 500, targetAngle = angle)

        # Pickup the expert
        _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP)

    def _doChickenAndCraftCretor():
        angle = 0

        # Now flush with the missions.
        # And keep pushing the robot forward to align with the mission
        # while we turn the chicken
        gyroStraightWithDrive(distanceInCm = 10, speed = 200, targetAngle = angle)
        drive_base.drive(speed = 200, turn_rate = 0)

        # Now turn the chicken
        _positionChicken()

        # Now that we are done, stop pushing.
        stopDriveBase()

        # Now backoff.
        gyroStraightWithDrive(distanceInCm = 15, speed = 200, targetAngle = angle, 
                              backward=True, multiplier = 0.1)


    def _goHome():
        angle = 0
        gyroStraightWithDrive(distanceInCm = 30, speed = 1000, targetAngle = angle, backward=True)

    def _dorun45():
        _pickupExpert()
        _doChickenAndCraftCretor()
        _goHome()

    resetRobot()
    _dorun45() 
    