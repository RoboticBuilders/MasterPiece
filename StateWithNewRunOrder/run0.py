from Utilities import *

def run0():
    
    def _positionChicken():
        left_med_motor.run_angle(1000, 1500)
    
    def _pickupExpert():
        right_med_motor.run_target(speed=300, target_angle=150, then=Stop.HOLD, wait = True)
        #right_med_motor.reset_angle(0)

        angle = 0

        # Bring down attachment.
        #run6PositionPickUpExpertAttachment(position=RUN6_PICKUP_EXPERT_ATTACHMENT_DOWN, wait=False)

        # drive forward before picking up arm
        #gyroStraightWithDrive(distanceInCm = 22, speed = 500, targetAngle = angle)
        gyroStraightWithDriveWithAccurateDistance(distance = 29, speed = 300, backward = False, targetAngle = angle, multiplier = 1)

        # Pickup the expert
        # run6PositionPickUpExpertAttachment(position=RUN6_PICKUP_EXPERT_ATTACHMENT_UP, speed = 150)

        # This code is commented out to try the load to pick up izzy.
        run6PositionPickUpExpertAttachment(position=RUN6_PICKUP_EXPERT_ATTACHMENT_UP, speed = 150, wait = False)
        passed_load_threshold = False
        while right_med_motor.done() == False:
            if right_med_motor.load() > 30:
                hub.speaker.beep()
                passed_load_threshold = True
        if passed_load_threshold == False:
            print("Missed Izzy")
            turnToAngle(targetAngle=-90, turn_acceleration=2000)
            turnToAngle(targetAngle=0)
        else:
            print("Picked up Izzy")

    def _doChickenAndCraftCretor():
        angle = 0

        # Now flush with the missions.
        # And keep pushing the robot forward to align with the mission
        # while we turn the chicken
        gyroStraightWithDrive(distanceInCm = 10, speed = 400, targetAngle = angle)
        drive_base.drive(speed = 100, turn_rate = 0)

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

    def _dorun0():
        _pickupExpert()
        _doChickenAndCraftCretor()
        _goHome()
    
    

    resetRobot()
    _dorun0() 

