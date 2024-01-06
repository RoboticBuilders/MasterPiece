from Utilities import *

def _pushRollingCameraLever():
    # We just push the static arm with the bucket to drop the lever

    angle = 0
    right_med_motor.run_angle(speed=2000, rotation_angle=-600)
    
    right_med_motor.run_angle(speed=2000, rotation_angle=600)

def run2():
    _pushRollingCameraLever()

#runWithTiming(run2,"Lever")