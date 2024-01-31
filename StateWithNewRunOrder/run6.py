from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

def rollingCamera():
    # First bring down the bucket.
    angle=0
    right_med_motor.run_angle(speed=2000, rotation_angle=-400, wait = False)

    # Now drive towards the rolling camera and bring down the bucket
    # We bring down the motor slightly more, to ensure that
    # the camera is caught.
    gyroStraightWithDriveWithAccurateDistance(distance=40, speed=800, targetAngle=angle)
    right_med_motor.run_angle(speed=2000, rotation_angle=-420)
    
    # Now backup and pull the camera and turn it into its place.
    # We do a back and forth before turn, so we get give in the thread, so we dont have resistance
    # when we turn.
    gyroStraightWithDriveWithAccurateDistance(distance=20, speed=800, targetAngle=angle, backward = True)
    gyroStraightWithDriveWithAccurateDistance(distance=7, speed=800, targetAngle=angle)
    angle = -25
    turnToAngle(targetAngle=angle,speed=400)
    
    # Now bring up the bucket, before driving away.
    # TODO consider doing part of this in parallel.
    right_med_motor.run_angle(speed=2000, rotation_angle=420)
    
def museumwithpedestaloutside():
    #Use a curve to reach in front of the immersive experience
    # 1/30/204: Increased curve from 610 to 650
    drive_base.curve(radius = 610, angle = -50)
    # Added this to drop the bucket so pedestal doesnt move out near the expert.
    right_med_motor.run_angle(speed=2000, rotation_angle=-200)
    gyroStraightWithDrive(distanceInCm = 7, speed = 400, targetAngle = -90)
       
    #wait(5000)
    # Now turn to drop off at museum
    angle = -30
    turnToAngle(targetAngle=angle,speed=600)
    # gyroStraightWithDriveWithAccurateDistance(distance=27, speed=1000, targetAngle=angle)
     # 1/30/204: Reduced distance from 25 to 22
    gyroStraightWithDriveWithAccurateDistance(distance=25, speed=1000, targetAngle=angle)
    # Drop off the expert and audience
    
    left_med_motor.run_angle(speed=500, rotation_angle=500)

    angle=-90
    turnToAngle(targetAngle=angle, speed=800)
    
    # wait(5000)
    drive_base.straight(50)
    # Increased this from 400 to 600 as we are now bringing the bucket down to not let pedestal move
    right_med_motor.run_angle(speed=2000, rotation_angle=600)
  
def lightShow():
    # Now after the pedestal drop off, drive backwards towards the light show. Using drivebase.straight as its more accurate for distance
    # Currently the lightshow is set to run at 1000 speed. In the speed testing for lightshow the times taken were:
    # speed 600 - time->4.8sec
    # speed 800 - time-> 3.8 sec
    # speed 1000 - time ->3.5 sec
    
    angle=-90
    gyroStraightWithDriveWithAccurateDistance(distance=12, speed=700, targetAngle=angle,backward=True,stop=Stop.COAST)
    '''STALL DETECTION CODE: IMPLEMENT IF IT WORKS / MUCH CLEANER'''
    drive_base.settings(300, 500, 300, 500)
    drive_base.straight(distance = -200, wait = False)
    stall_detect.load(max_load = 120, debug = False)
    '''DRIVE FOR TIME CODE: IMPLEMENT IF STALL DETECT DOESN'T WORK'''
    # driveForTime(500, stopAtEnd=True, speed=-500, turnRate=0)
    wait(100)
    # Now we are at the light show, spin the lightshow from the back spinny arm.
    orgSpeed,orgAccel,orgTorque = left_med_motor.control.limits()
    left_med_motor.control.limits(speed = orgSpeed,acceleration = orgAccel,torque = 1000)
    left_med_motor.run_angle(speed=1000, rotation_angle=-2500, wait = True)
    left_med_motor.control.limits(speed = orgSpeed, acceleration = orgAccel, torque = orgTorque)
  
def immersiveExperience():
    # Now move ahead from the light show
    angle=-90
    gyroStraightWithDriveWithAccurateDistance(distance=7, speed=500, targetAngle=angle)
    # Turn towards immersive experience
    angle=170
    turnToAngle(targetAngle=angle, speed=300)
    gyroStraightWithDriveWithAccurateDistance(distance=20, speed=400, targetAngle=angle)
    angle=-90
    turnToAngle(targetAngle=angle, speed=300)
    gyroStraightWithDriveWithAccurateDistance(distance=13, speed=400, targetAngle=angle)
    
def goHomeWithCurve():
    # Backoff from the Immersive experience.
    gyroStraightWithDriveWithAccurateDistance(distance=28, speed=800, targetAngle=270, backward=True)

    # Curve around the light show to avoid hitting the camera and also go home.
    drive_base.curve(radius = -200, angle = 90)
  
    # Drive backward at a slight angle to ensure that we are catching the
    # expert when going home.

    angle = 187
    gyroStraightWithDriveWithAccurateDistance(distance=40, speed=1000, targetAngle=angle, 
                                              slowDown = False, backward = True,
                                              useSlowerAccelerationForBackward = False,stop=Stop.COAST)
    angle = 160
    gyroStraightWithDriveWithAccurateDistance(distance=23, speed=1000, targetAngle=angle, 
                                              slowDown = False, backward = True,
                                              useSlowerAccelerationForBackward = False, stop = Stop.COAST)
    
    
    angle = 180
    gyroStraightWithDriveWithAccurateDistance(distance=20, speed=1000, targetAngle=angle, 
                                              slowDown = False, backward = True,
                                              useSlowerAccelerationForBackward = False)


def goHomeBetweenChickenAndAugmentedReality():
    # Backoff from the Immersive experience. Turn towards home2 and then go home.
    gyroStraightWithDriveWithAccurateDistance(distance=5, speed=800, targetAngle=270, backward=True)
    angle = 0
    turnToAngle(targetAngle = angle, speed = 300)
    gyroStraightWithDriveWithAccurateDistance(distance=75, speed=1000, targetAngle=angle)

    angle = 60
    turnToAngle(targetAngle = angle, speed = 300)
    gyroStraightWithDriveWithAccurateDistance(distance=50, speed=1000, targetAngle=angle)

def goHomeWithCurveAccurate():
    # Backoff from the Immersive experience.
    gyroStraightWithDriveWithAccurateDistance(distance=28, speed=800, targetAngle=270, backward=True)

    # Curve around the light show to avoid hitting the camera and also go home.
    drive_base.curve(radius = -200, angle = 90)
  
    # Drive backward at a slight angle
    angle = 195
    gyroStraightWithDriveWithAccurateDistance(distance=85, speed=1000, targetAngle=angle, 
                                              slowDown = False, backward = True,
                                              useSlowerAccelerationForBackward = False,stop=Stop.COAST)
    #angle = 157
    #gyroStraightWithDriveWithAccurateDistance(distance=45, speed=1000, targetAngle=angle, 
    #                                          slowDown = False, backward = True,
    #                                          useSlowerAccelerationForBackward = False, stop = Stop.COAST)

    
def resetBucket(angle = 800):
    right_med_motor.run_angle(speed=1000, rotation_angle=angle)

def testBucket():
    while True:
        # Brind down the bucket.
        right_med_motor.run_angle(speed=2000, rotation_angle=-400)
        wait(200)
        right_med_motor.run_angle(speed=2000, rotation_angle=-400)
        wait(2000)
        right_med_motor.run_angle(speed=2000, rotation_angle=800)
        wait(2000)

def run6():
    resetRobot()
    rollingCamera()
    museumwithpedestaloutside()
    lightShow()
    immersiveExperience()
    goHomeWithCurveAccurate()
    
#waitForButtonPress()
#runWithTiming(run6, "Light Show")

