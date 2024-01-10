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
    # We start resetting the left motor when we curve home, because we want to be able to change the 
    # attachment
    _resetLeftMotor(wait = False)
    drive_base.settings(500, 1000, 500, 1000)
    drive_base.curve(radius = -550, angle = -40)

def _resetBucket():
    # Turn the right motor to pick up the expert
    right_med_motor.run_angle(speed=2000, rotation_angle=800, wait = False)

def _resetLeftMotor(wait):
    left_med_motor.run_angle(speed=2000, rotation_angle=800, wait=wait)

def waitForLeftMotor():
    while left_med_motor.done() == False:
        continue

def run0():
    resetRobot()
    _doSoundMixerWithComplicatedArm()
    _resetBucket()

#runWithTiming(run0, "Sound Mixer")
#_resetBucket()
