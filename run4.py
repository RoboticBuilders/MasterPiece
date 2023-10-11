from Utilities import *

def run4():
    # pickup Expert Attachment constants
    PICKUP_EXPERT_ATTACHMENT_UP_TO_DOWN = 1
    PICKUP_EXPERT_ATTACHMENT_UP = 2

    # Expects the arm to start down.
    def _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP_TO_DOWN):
        if position == PICKUP_EXPERT_ATTACHMENT_UP_TO_DOWN:
            right_med_motor.run_target(500, 200)
        else: 
            right_med_motor.run_target(500, -200)

    def _positionChicken():
        left_med_motor.run_angle(500, 600)


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
        _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP_TO_DOWN)

    angle = 0
    # Drive forward to do rolling camera and also
    # pick up the expert.
    gyroStraightWithDrive(distanceInCm = 50, speed = 250, targetAngle = angle)

    # Pick up the expert
    #_positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP)

    # Drive towards the dropoff at movie set
    gyroStraightWithDrive(distanceInCm = 34, speed = 250, targetAngle = angle)
    
    # Below this code is to pick up expert, 3d printer, chicken
    # 
    # Backoff from the movie set to drop off the expert and orange 
    # audience. 
    gyroStraightWithDrive(distanceInCm = 70, speed = 500, targetAngle = angle, backward=True)

    # Drive forward to pickup the expert.
    angle = 46
    turnToAngle(targetAngle = angle, speed = 500)

    # Bring down attachment.
    _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP_TO_DOWN)

    # drive forward before picking up arm
    gyroStraightWithDrive(distanceInCm = 26, speed = 200, targetAngle = angle)

    # Pickup the expert
    _positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP)

    # Now flush with the missions.
    gyroStraightWithDrive(distanceInCm = 13, speed = 250, targetAngle = angle)

    # Now turn the chicken
    _positionChicken()

    # Now backoff.
    gyroStraightWithDrive(distanceInCm = 10, speed = 150, targetAngle = angle, backward=True)
    gyroStraightWithDrive(distanceInCm = 40, speed = 250, targetAngle = angle, backward=True)

    # Reset attachment for the next run. 
    # Comment in the main program.
    _resetAttachment()

    #_positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP)
    #wait(3000)
    #_positionPickUpExpertAttachment(position=PICKUP_EXPERT_ATTACHMENT_UP_TO_DOWN)
    

'''
    angle = 0
    gyroStraightWithDrive(distanceInCm = 40, speed = 250, targetAngle = angle)
    _positionChicken()
    '''

initializeAndWaitForRobotReady()
run4()
#right_med_motor.run_target(300, 100)
