# from Utilities import *
from TestLoadUtils import *

TURN_SPEED = 300

def _doSoundMixerWithComplicatedArm():
    angle = 0
    # gyroStraightWithDriveWithAccurateDistance(distance = 32, speed = 800, targetAngle = angle, stop = Stop.COAST)
    # gyroStraightWithDriveWithAccurateDistance(distance = 20, speed = 150, targetAngle = angle)
    drive_base.straight(distance = 450, wait = False)
    stall_detect_1.avg_load(max_load_change = 1, min_stopping_condition = 30, avg_length = 15, debug = True)

    # Turn the right motor to pick up the expert
    right_med_motor.run_angle(speed=2000, rotation_angle=-800)
    # right_med_motor.run(speed=-200)

    gyroStraightWithDriveWithAccurateDistance(distance = 10, speed = 100, targetAngle = angle)
    # Turn the motor to remove the lock for the left sound mixer.
    # Do this in parallel with the expert pick up.
    left_med_motor.run_angle(speed=2000, rotation_angle=-800)

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
    drive_base.curve(radius = -420, angle = -50)


def _doSoundMixerWithStallDetection():
    angle = 0
    drive_base.straight(distance = 400, wait = False)
    stall_detect_1.load(max_load = 150, debug = False)
    gyroStraightWithDriveWithAccurateDistance(distance = 20, speed = 100, targetAngle = angle)

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
    drive_base.curve(radius = -530, angle = -40)


def _resetBucket():
    # Turn the right motor to pick up the expert
    right_med_motor.run_angle(speed=2000, rotation_angle=800)

def _resetLeftMotor(wait):
    left_med_motor.run_angle(speed=2000, rotation_angle=800, wait=wait)

def waitForLeftMotor():
    while left_med_motor.done() == False:
        continue

def run5():
    resetRobot()
    _doSoundMixerWithComplicatedArm()
    #_doSoundMixerWithStallDetection()
    _resetBucket()

# waitForButtonPress()
# runWithTiming(run5, "Sound Mixer")
# _doSoundMixerWithStallDetection()
#_resetBucket()
    
