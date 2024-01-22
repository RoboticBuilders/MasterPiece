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
    gyroStraightWithDriveWithAccurateDistance(distance=41, speed=800, targetAngle=angle)
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
    drive_base.curve(radius = 610, angle = -50)

    gyroStraightWithDrive(distanceInCm = 7, speed = 400, targetAngle = -90)
       
    #wait(5000)
    # Now turn to drop off at museum
    angle = -30
    turnToAngle(targetAngle=angle,speed=600)
    gyroStraightWithDriveWithAccurateDistance(distance=27, speed=1000, targetAngle=angle)
    # Drop off the expert and audience
    
    left_med_motor.run_angle(speed=500, rotation_angle=500)

    angle=-90
    turnToAngle(targetAngle=angle, speed=800)
    #gyroStraightWithDriveWithAccurateDistance(distance=5, speed=650, targetAngle=angle)
    right_med_motor.run_angle(speed=2000, rotation_angle=400)
  
def lightShow():
    # Now after the pedestal drop off, drive backwards towards the light show. Using drivebase.straight as its more accurate for distance
    # Currently the lightshow is set to run at 1000 speed. In the speed testing for lightshow the times taken were:
    # speed 600 - time->4.8sec
    # speed 800 - time-> 3.8 sec
    # speed 1000 - time ->3.5 sec
    
    angle=-90
    gyroStraightWithDriveWithAccurateDistance(distance=10, speed=700, targetAngle=angle,backward=True,stop=Stop.COAST)
    gyroStraightWithDriveWithAccurateDistance(distance=8, speed=500, targetAngle=angle,backward=True)
    wait(100)
    # Now we are at the light show, spin the lightshow from the back spinny arm.
    orgSpeed,orgAccel,orgTorque = left_med_motor.control.limits()
    left_med_motor.control.limits(speed = orgSpeed,acceleration = orgAccel,torque = 1000)
    left_med_motor.run_angle(speed=1000, rotation_angle=-2500, wait = True)
    left_med_motor.control.limits(speed = orgSpeed,acceleration = orgAccel,torque = orgTorque)

def immersiveExperience():
    # Now move ahead from the light show
    angle=-90
    gyroStraightWithDriveWithAccurateDistance(distance=7, speed=500, targetAngle=angle)
    # Turn towards immersive experience
    angle=170
    turnToAngle(targetAngle=angle, speed=300)
    gyroStraightWithDriveWithAccurateDistance(distance=21.5, speed=400, targetAngle=angle)
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


def goHomeWithCurveAccurate():
    # Backoff from the Immersive experience.
    gyroStraightWithDriveWithAccurateDistance(distance=28, speed=800, targetAngle=270, backward=True)

    # Curve around the light show to avoid hitting the camera and also go home.
    drive_base.curve(radius = -200, angle = 90)
  
    # Drive backward at a slight angle to ensure that we are catching the
    # expert when going home.

    #Changed angle from 187 to 190 to make sure it always catches the expert    1/15
    angle = 190
    gyroStraightWithDriveWithAccurateDistance(distance=40, speed=1000, targetAngle=angle, 
                                              slowDown = False, backward = True,
                                              useSlowerAccelerationForBackward = False,stop=Stop.COAST)
    #Changed angle from 160 to 157 since changed the agle in the gyroStraight above    1/15
    angle = 157
    gyroStraightWithDriveWithAccurateDistance(distance=45, speed=1000, targetAngle=angle, 
                                              slowDown = False, backward = True,
                                              useSlowerAccelerationForBackward = False, stop = Stop.COAST)

    
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

def run4ayaantable():
    resetRobot()
    rollingCamera()
    museumwithpedestaloutside()
    lightShow()
    immersiveExperience()
    goHomeWithCurveAccurate()
    

#testBucket()
# lightShowTestWith8ToothGear()
#lightShowTestWithLoad()
#runWithTiming(lightShowTest, "Light Show")
#resetBucket(angle = 400)
#testAudienceDropOffAtLightShow()
#runWithTiming(testlightShowtime, "lightshowtime")



