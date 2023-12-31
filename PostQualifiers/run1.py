from Utilities import *

TURN_SPEED = 300

def _doSoundMixerWithComplicatedArm():
    angle = 0
    gyroStraightWithDrive(distanceInCm = 60, speed = 200, targetAngle = angle)

    # Turn the motor to remove the lock for the left sound mixer.
    left_med_motor.run_angle(speed=800, rotation_angle=-500)

    # Turn the right motor to pick up the expert
    right_med_motor.run_angle(speed=2000, rotation_angle=-800)

    # Now backoff.
    gyroStraightWithDrive(distanceInCm = 50, speed = 800, targetAngle = angle, backward=True)

def _resetBucket():
    # Turn the right motor to pick up the expert
    right_med_motor.run_angle(speed=2000, rotation_angle=800)

def run1():
    _doSoundMixerWithComplicatedArm()

runWithTiming(run1, "Sound Mixer")
_resetBucket()
