from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

def immersiveExperianceFromBelow():
    angle = 0
    #Drive forward and stop right behind the camera in movie set
    gyroStraightWithDrive(distanceInCm=30, speed=400, targetAngle=angle)

    angle = -35
    #Turn to avoid the camera
    turnToAngle(targetAngle=angle, speed=400)
    gyroStraightWithDrive(distanceInCm=48, speed=400, targetAngle=-35)

    angle = -90
    turnToAngle(targetAngle=angle, speed=400)
    gyroStraightWithDrive(distanceInCm=35, speed=400, targetAngle=angle)
    left_med_motor.run_angle(speed=700, rotation_angle=1200)
    gyroStraightWithDrive(distanceInCm=20, speed=400, targetAngle=angle)

def lightShowTest():
    right_med_motor.run_angle(speed=800, rotation_angle=-3600)

def immersiveExperianceFromSide():
    left_med_motor.run_angle(speed=2000, rotation_angle=10000)
    left_med_motor.run_angle(speed=2000, rotation_angle=-10000)

def immersiveExperianceFromSideSlider():
    #Align it on the green part of museam, pushed against the wall
    gyroStraightWithDrive(distanceInCm=20,speed=700,targetAngle=0,backward=True)

    angle=90
    turnToAngle(targetAngle=angle, speed=700)
    gyroStraightWithDrive(distanceInCm=25,speed=400,targetAngle=angle,backward=True)

    left_med_motor.run_angle(speed=2000, rotation_angle=-2000)
    left_med_motor.run_angle(speed=2000, rotation_angle=1100)

def ThreeDCinemaUsingStaticArm():
    angle = 0
    gyroStraightWithDrive(distanceInCm = 30 , speed=400, targetAngle=angle)

def movieCameraAndRollingCameraStopper():
    left_med_motor.run_angle(speed=2000, rotation_angle=-1000)

    angle = 0
    gyroStraightWithDrive(distanceInCm = 10, speed=200, targetAngle=angle,backward=True)    
    angle = -20
    turnToAngle(targetAngle=angle, speed=400)

    left_med_motor.run_angle(speed=2000, rotation_angle=1000)

def run4():
    # ALIGNMENT: 3rd dark black line from the from the back wall
    gyroStraightWithDrive(distanceInCm = 48, speed = 500, targetAngle = 0)
    turnToAngle(targetAngle = -30, speed = 500)
    gyroStraightWithDrive(distanceInCm = 25, speed = 500, targetAngle = -30)
    turnToAngle(targetAngle = -90, speed = 500)
    gyroStraightWithDrive(distanceInCm = 40, speed = 500, targetAngle = -90)
    turnToAngle(targetAngle = -45, speed = 500)
    gyroStraightWithDrive(distanceInCm = 10, speed = 500, targetAngle = -45)

    left_med_motor.run_angle(speed=2000, rotation_angle=-3000)
    left_med_motor.run_angle(speed=2000, rotation_angle=1800)

    gyroStraight(distanceInCm = 5, speed = 500, targetAngle = -45)
    turnToAngle(targetAngle = -90, speed = 500)

    right_med_motor.run_angle(speed = 1000, rotation_angle = 1000)

    gyroStraight(distanceInCm = 15, speed = 300, targetAngle = -90)
    gyroStraight(distanceInCm = 7, speed = 50, targetAngle = -90)

    right_med_motor.run_angle(speed=1000, rotation_angle=3500)



#   RUN4 With Spinner and Slider
def rollingCamera():
    angle=0
    right_med_motor.run_angle(speed=2000, rotation_angle=-400)
    gyroStraightWithDriveWithAccurateDistance(distance=48, speed=300, targetAngle=angle)
    right_med_motor.run_angle(speed=2000, rotation_angle=-400)
    gyroStraightWithDriveWithAccurateDistance(distance=15, speed=300, targetAngle=angle, backward = True)

    angle=-35
    turnToAngle(targetAngle=angle,speed=400)
    right_med_motor.run_angle(speed=2000, rotation_angle=400)

def museum():
    angle=-35
    gyroStraightWithDriveWithAccurateDistance(distance=35, speed=400, targetAngle=angle)

    angle=-60
    turnToAngle(targetAngle=angle,speed=400)
    gyroStraightWithDriveWithAccurateDistance(distance=50, speed=400, targetAngle=angle)

    angle=-90
    turnToAngle(targetAngle=angle, speed=400)
    gyroStraightWithDriveWithAccurateDistance(distance=6, speed=200, targetAngle=angle)

    gyroStraightWithDriveWithAccurateDistance(distance=5, speed=400, targetAngle=angle,backward=True)
    right_med_motor.run_angle(speed=1000, rotation_angle=400)
    left_med_motor.run_angle(speed=1000, rotation_angle=800)

def lightShow():
    # Now after the pedestal drop off, drive backwards towards the light show. Using drivebase.straight as its more accurate for distance
    
    angle=-90
    #drive_base.settings(200, 500, 200, 500)
    #drive_base.straight(distance = -280)
    gyroStraightWithDriveWithAccurateDistance(distance=25, speed=400, targetAngle=angle,backward=True)
    wait(100)
    # Now we are at the light show, spin the lightshow from the back spinny arm.
    right_med_motor.run_angle(speed=600, rotation_angle=-3600)

def immersiveExperience():
    # Now move ahead from the light show
    angle=-90
    gyroStraightWithDriveWithAccurateDistance(distance=5, speed=400, targetAngle=angle)
    right_med_motor.run_angle(speed=1000, rotation_angle=700,wait=False)
    # Turn towards immersive experience
    angle=180
    turnToAngle(targetAngle=angle, speed=300)
    gyroStraightWithDriveWithAccurateDistance(distance=15, speed=400, targetAngle=angle)
    angle=-90
    turnToAngle(targetAngle=angle, speed=300)
    gyroStraightWithDriveWithAccurateDistance(distance=12, speed=400, targetAngle=angle)
    #drive_base.settings(200, 500, 200, 500)
    #drive_base.straight(distance = -200)
    
    #left_med_motor.run_angle(speed=2000, rotation_angle=-3000)
    #left_med_motor.run_angle(speed=2000, rotation_angle=1800)

def goHome():
    gyroStraightWithDrive(distanceInCm=10, speed=100, targetAngle=270, backward=True)
    # was 34
    gyroStraightWithDrive(distanceInCm=36, speed=400, targetAngle=270, backward=True)

    angle = 10
    turnToAngle(angle, speed=500)
    gyroStraightWithDrive(distanceInCm=100, speed=1000, targetAngle=angle)

    '''
    angle=-90
    gyroStraightWithDriveWithAccurateDistance(distance=50, speed=700, targetAngle=angle, backward=True)

    angle=0
    turnToAngle(targetAngle=angle, speed=600)
    gyroStraightWithDriveWithAccurateDistance(distance=100, speed=700, targetAngle=angle)
    '''
# We are not doing augmented reality right now
def augmentedReality():
    angle = 0
    right_med_motor.run_angle(speed=700, rotation_angle=-200)
    gyroStraightWithDrive(distanceInCm = 34, speed = 300, targetAngle = angle)

    angle = -90
    turnToAngle(targetAngle = angle, speed = 300)
    gyroStraightWithDrive(distanceInCm = 5, speed = 150, targetAngle = angle)
    
    angle = 0
    turnToAngle(targetAngle = angle, speed = 700)

    angle=-80
    turnToAngle(targetAngle = angle, speed = 500)
    gyroStraightWithDrive(distanceInCm = 7, speed = 300, targetAngle = angle, backward = True)
    
    angle = 0
    turnToAngle(targetAngle = angle, speed = 300)
    right_med_motor.run_angle(speed=700, rotation_angle=800)
    gyroStraightWithDrive(distanceInCm = 60, speed = 400, targetAngle = angle)

def goHomeWithAugmentedReality():
    angle = 90
    turnToAngle(targetAngle = angle, speed = 1000)
    gyroStraightWithDrive(distanceInCm = 50, speed = 1000, targetAngle = angle)

def goHomeWithExpertPickup():
    angle = 270
    gyroStraightWithDrive(distanceInCm=10, speed=100, targetAngle=270, backward=True)
    gyroStraightWithDrive(distanceInCm=36, speed=400, targetAngle=270, backward=True)
    # Turn towards home
    #angle = 10
    #turnToAngle(angle, speed=500)
    # Run towards home with expert pickup
    #gyroStraightWithDrive(distanceInCm=75, speed=1000, targetAngle=angle)

    angle=-50
    gyroStraightWithDrive(distanceInCm=45, speed=400, targetAngle=angle)

    angle=-90
    turnToAngle(targetAngle=angle, speed=400)
    gyroStraightWithDrive(distanceInCm=35, speed=400, targetAngle=angle)



#RUN4 With flush on Light show
def flushOnLightShow():
    angle=-40
    turnToAngle(targetAngle=angle, speed=400)
    gyroStraightWithDrive(distanceInCm=25, speed=700, targetAngle=angle)
    #Lower bucket arm completly
    right_med_motor.run_angle(speed=2000, rotation_angle=-400)
    #Crash into the light show
    gyroStraightWithDrive(distanceInCm=10, speed=100, targetAngle=angle)

def museumAfterFlushOnLightShow():
    angle=-40
    gyroStraightWithDrive(distanceInCm=10, speed=400, targetAngle=angle, backward=True)

    angle=-60
    turnToAngle(targetAngle=angle, speed=400)
    gyroStraightWithDrive(distanceInCm=65, speed=400, targetAngle=angle)
    
    #angle=-90
    #turnToAngle(targetAngle=angle, speed=400)
    #right_med_motor.run_angle(speed=700, rotation_angle=470)




#RUN4 With curve to go to museum
def catchLineBesideLightShowAndCurveToMuseum():
    # Move forward a little after doing the rolloing camera so we do not pull the rolling camera with us.
    angle=-40
    gyroStraightWithDrive(distanceInCm=13, speed=500, targetAngle=angle)
    # Bring the bucket down so pedestal doesnt come out
    # This is intentionally 200 so it doesnt drag on the mat while moving
    right_med_motor.run_angle(speed=700, rotation_angle=-200)
    # Now move ahead at a slight angle so we dont hit the light show and catch the black line between light show and rolling camera.
    angle=2
    turnToAngle(targetAngle=angle, speed=400)
    driveTillLine(speed=200, doCorrection=False, sensor=right_color, blackOrWhite="Black")
    # We have now reached the black line. Curve to not hit light show to sound mixer and reach in front of the museum.
    angle=0
    turnToAngle(targetAngle=angle, speed=400)
    drive_base.settings(400, 400, 400, 400)
    drive_base.curve(radius=-160, angle=-90,then=Stop.COAST)
    drive_base.curve(radius=-170, angle=-92)

def dropoffPedestal():

    # Now we are in front of the museum after the curve.
    # Turn towards museum, drive forward to be within the museum target area and open the bucket to drop the pedestal.
    angle=-90
    turnToAngle(targetAngle=angle, speed=400)
    gyroStraightWithDrive(distanceInCm=13, speed=600, targetAngle=angle)
    right_med_motor.run_angle(speed=800, rotation_angle=700)




#RUN4 With thether scene change type path
def museumStartingPointingForward():
    # First lower the bucket a little.
    right_med_motor.run_angle(speed=2000, rotation_angle=-400)

    # Now drive forward at a slight angle.
    angle=7
    gyroStraightWithDriveWithAccurateDistance(distance=55, speed=800, backward = False, targetAngle = angle, 
                                              stop = Stop.COAST)

    # Now drive till the black line.
    gyroStraightWithDriveWithAccurateDistance(distance=10, speed=800, backward = False, targetAngle = angle, 
                                              tillBlackLine = True,
                                              stop = Stop.HOLD)

    # Now Lower the bucket fully.
    right_med_motor.run_angle(speed=2000, rotation_angle=-400)

    # Drive forward a little more so we can turn 90,
    gyroStraightWithDriveWithAccurateDistance(distance=7, speed=400, backward = False, targetAngle = angle, 
                                              stop = Stop.HOLD)

    # Now turn towards the LightShow
    angle = 90
    turnToAngle(targetAngle = angle, speed=400)

    # Now drive till the museum
    gyroStraightWithDriveWithAccurateDistance(distance=62, speed=800, backward = False, targetAngle = angle, 
                                              stop = Stop.HOLD)

    # Now turn to drop off the museum.
    angle = 0
    turnToAngle(targetAngle = angle, speed=400)

    # Now drive forward before dropping off the units.
    gyroStraightWithDriveWithAccurateDistance(distance=10, speed=800, backward = False, targetAngle = angle, 
                                              stop = Stop.HOLD)

    # Now lift the bucket.
    right_med_motor.run_angle(speed=2000, rotation_angle=800)

    # Now backp till the light sho0w.
    gyroStraightWithDriveWithAccurateDistance(distance=20, speed=500, backward = True, targetAngle = angle, 
                                              stop = Stop.HOLD)

    # Now slowly backoff.
    gyroStraightWithDriveWithAccurateDistance(distance=5, speed=200, backward = True, targetAngle = angle, 
                                              stop = Stop.HOLD)

    # Now turn the light show
    right_med_motor.run_angle(speed=1000, rotation_angle=-600)



def resetBucket(angle = 800):
    right_med_motor.run_angle(speed=1000, rotation_angle=angle)

def run4():
    initializeAndWaitForRobotReady()
    rollingCamera()
    museum()
    lightShow()
    immersiveExperience()
    goHome()

def run4Between3dCimenaAndSoundMixer():
    museumStartingPointingForward()

runWithTiming(run4,"Run4")





#runWithTiming(lightShowTest, "Light Show")
#resetBucket(angle = 400)

