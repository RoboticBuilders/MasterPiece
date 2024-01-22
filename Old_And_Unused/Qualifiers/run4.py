from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *



def run4():
    _angle=-30
    resetGyro(_angle)

    # gyroStraightWithDrive(distanceInCm = 63, speed = 400, targetAngle = _angle)
    gyroStraightWithDrive(distanceInCm = 60, speed = 400, targetAngle = _angle)

    # _angle = 335
    # turnToAngle(_angle, speed=200, oneWheelTurn=True)

    # Changed 11/16: 52 to 54 to avoid hitting the Sound Mixer
    # gyroStraightWithDrive(distanceInCm = 50, speed = 400, targetAngle = _angle) 
    # robot.straight(distance=580)
    #Changed Dec 3: angle 275 to 270
    #turnToAngle(targetAngle=275, speed=200, oneWheelTurn=True)
    turnToAngle(targetAngle=270, speed=200, oneWheelTurn=True)
     #Changed Dec 3: distance 45 to 44
    gyroStraightWithDrive(distanceInCm = 45, speed=200, targetAngle=270, slowDown=True,multiplier = 1) 
    # gyroStraightWithDrive(distanceInCm = 5, speed=100, targetAngle=270, slowDown=True) 
    #wait(3000)
    # Now drop off the expert.
    right_med_motor.run_angle(speed=1000, rotation_angle=1200)
    right_med_motor.run_angle(speed=1000, rotation_angle=-1200, wait=False)

    #wait(5000)
    # backoff.
    gyroStraightWithDrive(distanceInCm=10, speed=100, targetAngle=270, backward=True)
    # was 34
    gyroStraightWithDrive(distanceInCm=36, speed=400, targetAngle=270, backward=True)
    #gyroStraightWithDrive(distanceInCm=44, speed=400, targetAngle=270, backward=True)

    # Code after this is new code.
    # gyroStraightWithDrive(distanceInCm=5, speed=400, targetAngle=275, backward=True)
    angle = 10
    turnToAngle(angle, speed=500)
    # catch the black line
    driveTillLine(speed=300, sensor=right_color, doCorrection=False, maxDistanceMM=240, tag="Light Show")
    drive_base.straight(distance=100)
    # gyroStraightWithDrive(distanceInCm=24, speed=400, targetAngle=angle)
    
    left_med_motor.run_angle(speed=1000, rotation_angle=500)
    # wait(1000)
    # Changed dec 3: removed wait= false
    left_med_motor.run_angle(speed=1000, rotation_angle=-500)
    gyroStraightWithDrive(distanceInCm=75, speed=1000, targetAngle=angle)

def testLighthouseDrop():
    while True:
        left_med_motor.run_angle(speed = 100, rotation_angle=150)
        left_med_motor.run_angle(speed = 300, rotation_angle=-150)
        wait(1000)       

'''
    angle = 0
    gyroStraightWithDrive(distanceInCm = 40, speed = 250, targetAngle = angle)
    _positionChicken()
    '''

#initializeAndWaitForRobotReady()
# runWithTiming(run4,'run4')

#right_med_motor.run_target(300, 100)

# testLighthouseDrop()

# left_med_motor.run_angle(speed=300, rotation_angle=-80)
# wait(1000)
# left_med_motor.run_angle(speed=300, rotation_angle=80)

# left_med_motor.run_angle(speed=1000, rotation_angle=500)
# wait(1000)
# left_med_motor.run_angle(speed=1000, rotation_angle=-500)