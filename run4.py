from Utilities import *

def run4():
    # pickup Expert Attachment constants
    PICKUP_EXPERT_ATTACHMENT_DOWN = 1
    PICKUP_EXPERT_ATTACHMENT_UP = 2

    # Expects the arm to start up.
    def _positionPickUpExpertAttachment(position):
        if position == PICKUP_EXPERT_ATTACHMENT_DOWN:
            right_med_motor.run_target(500, 150)
        else: 
            right_med_motor.run_target(500, 0)

    def _positionChicken():
        left_med_motor.run_angle(speed=250, rotation_angle=-600)

    def _rolling_camera():
        gyroStraightWithDrive(distanceInCm = 26, speed = 250, targetAngle = 0)
        gyroStraightWithDrive(distanceInCm = 8, speed = 100, targetAngle = 0)

    def _pickup_emily():
        gyroStraightWithDrive(distanceInCm = 3, speed = 100, targetAngle = 0, backward=True)
        turnToAngle(targetAngle = 55, speed = 200)
        #gyroStraightWithDrive(distanceInCm = 5, speed = 200, targetAngle = 55)
        #turnToAngle(targetAngle = 35, speed = 150)
        right_med_motor.run_angle(1000, 90)

    def _drop_in_movie():
        turnToAngle(targetAngle = -10, speed = 500)
        gyroStraightWithDrive(distanceInCm = 40, speed = 300, targetAngle = -10)
        gyroStraightWithDrive(distanceInCm = -20, speed = 300, targetAngle = -10)

    def _resetAttachment():
        # Reset the attachment for next run.
        _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_DOWN)

    angle = 0
    # Drive forward to do rolling camera and also to drop off the
    # expert and the orange audience on to the movie set.
    gyroStraightWithDrive(distanceInCm = 45, speed = 250, targetAngle = angle)
    angle = -3
    gyroStraightWithDrive(distanceInCm = 35, speed = 400, targetAngle = angle)

    # Backoff from the movie set
    gyroStraightWithDrive(distanceInCm = 65, speed = 500, targetAngle = angle, backward=True)

    # Drive forward to pickup the expert in front of the 3d printer.
    angle = 46
    turnToAngle(targetAngle = angle, speed = 500)
    _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_DOWN) 

    # drive forward before picking up arm
    gyroStraightWithDrive(distanceInCm = 25, speed = 200, targetAngle = angle)

    # Pickup the expert
    _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP)

    # Now flush with the missions.
    gyroStraightWithDrive(distanceInCm = 15, speed = 250, targetAngle = angle)
    
    # Start Driving forward
    drive_base.drive(50, 0)
    
    # Now turn the chicken
    _positionChicken()

    # Now backoff.
    gyroStraightWithDrive(distanceInCm = 15, speed = 150, targetAngle = angle, backward=True)
    gyroStraightWithDrive(distanceInCm = 40, speed = 500, targetAngle = angle, backward=True)

    # Reset attachment for the next run. 
    # Comment in the main program.
    _resetAttachment()
    
    '''
    _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP)
    wait(3000)
    _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP_TO_DOWN)
    '''

initializeAndWaitForRobotReady()
runWithTiming(run4, "run4")
#right_med_motor.run_target(300, 100)
