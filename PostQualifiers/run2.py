from Utilities import *

TURN_SPEED = 300

def _doSoundMixerWithComplicatedArm():
    angle = 0
    gyroStraightWithDriveWithAccurateDistance(distance = 35, speed = 800, targetAngle = angle, stop = Stop.COAST)
    gyroStraightWithDriveWithAccurateDistance(distance = 20, speed = 400, targetAngle = angle)

    # Turn the motor to remove the lock for the left sound mixer.
    # Do this in parallel with the expert pick up.
    left_med_motor.run_angle(speed=2000, rotation_angle=-800, wait=False)

    # Turn the right motor to pick up the expert
    right_med_motor.run_angle(speed=2000, rotation_angle=-800)

    # Make sure that the stopper has been removed.
    while left_med_motor.done() == False:
        continue

    # Now backoff.
    gyroStraightWithDriveWithAccurateDistance(distance = 23, speed = 1000, targetAngle = angle, backward=True,
                                              stop = Stop.COAST)

    # Now drive back home.
    drive_base.settings(500, 1000, 500, 1000)
    drive_base.curve(radius = -500, angle = -30)


def _doSoundMixerWithComplicatedArmWithCurve():
    drive_base.settings(500, 1000, 500, 1000)
    drive_base.curve(radius = 140,angle = -55)
    
    gyroStraightWithDriveWithAccurateDistance(distance = 25, speed = 500, targetAngle = -45)
    gyroStraightWithDriveWithAccurateDistance(distance = 15, speed = 100, targetAngle = -45)

    # Turn the motor to remove the lock for the left sound mixer.
    left_med_motor.run_angle(speed=800, rotation_angle=-800)

    # Turn the right motor to pick up the expert
    right_med_motor.run_angle(speed=2000, rotation_angle=-800)
    angle = -45
    # Now backoff.
    gyroStraightWithDrive(distanceInCm = 50, speed = 800, targetAngle = angle, backward=True)
    #drive_base.settings(1000, 1000, 1000, 1000)
    #drive_base.curve(radius = -600,angle = -45)


def _resetBucket():
    # Turn the right motor to pick up the expert
    right_med_motor.run_angle(speed=2000, rotation_angle=800)
def _resetLeftMotor():
    left_med_motor.run_angle(speed=2000, rotation_angle=800)

def run2():
    resetRobot()
    _doSoundMixerWithComplicatedArm()
    _resetBucket()
    _resetLeftMotor()

#runWithTiming(run2, "Sound Mixer")
#_resetBucket()
