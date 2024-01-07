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
    
    drive_base.curve(radius = 650, angle = -50)
       
    #wait(5000)
    # Now turn to drop off at museum
    angle = -40
    turnToAngle(targetAngle=angle,speed=600)
    gyroStraightWithDriveWithAccurateDistance(distance=30, speed=1000, targetAngle=angle)
    # Drop off the expert and audience
    
    left_med_motor.run_angle(speed=500, rotation_angle=500)

    angle=-90
    turnToAngle(targetAngle=angle, speed=800)
    gyroStraightWithDriveWithAccurateDistance(distance=4, speed=650, targetAngle=angle)
    right_med_motor.run_angle(speed=2000, rotation_angle=400)
  
def lightShow():
    # Now after the pedestal drop off, drive backwards towards the light show. Using drivebase.straight as its more accurate for distance
    # Currently the lightshow is set to run at 1000 speed. In the speed testing for lightshow the times taken were:
    # speed 600 - time->4.8sec
    # speed 800 - time-> 3.8 sec
    # speed 1000 - time ->3.5 sec
    
    angle=-90
    gyroStraightWithDriveWithAccurateDistance(distance=12, speed=700, targetAngle=angle,backward=True,stop=Stop.COAST)
    gyroStraightWithDriveWithAccurateDistance(distance=11, speed=200, targetAngle=angle,backward=True)
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
    gyroStraightWithDriveWithAccurateDistance(distance=22.5, speed=400, targetAngle=angle)
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
    
    angle = 165
    gyroStraightWithDriveWithAccurateDistance(distance=35, speed=1000, targetAngle=angle, 
                                              slowDown = False, backward = True,
                                              useSlowerAccelerationForBackward = False)
    
    




def OLD():

    '''
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
        gyroStraightWithDriveWithAccurateDistance(distance=35, speed=400, targetAngle=0,backward=True)
        wait(100)
        # Now we are at the light show, spin the lightshow from the back spinny arm.
        right_med_motor.run_angle(speed=100, rotation_angle=-800)

    def lightShowTestWith8ToothGearWithStall():
        gyroStraightWithDriveWithAccurateDistance(distance=15, speed=400, targetAngle=0,backward=True)
        gyroStraightWithDriveWithAccurateDistance(distance=10, speed=150, targetAngle=0,backward=True)
        wait(100)
        # Now we are at the light show, spin the lightshow from the back spinny arm.
        MAX_TIME = 7000
        sw = StopWatch()
        start_time = sw.time()

        right_med_motor.run_angle(speed=600, rotation_angle=-800, wait = False)
        while right_med_motor.done() == False:
            if right_med_motor.stalled() and (-800 - right_med_motor.angle()) < -75:
                print("Restarting Light Show turn")
                
                right_med_motor.stop()

                drive_base.straight(100)
                drive_base.straight(-100)

                dist_left = -800 - right_med_motor.angle()
                right_med_motor.run_angle(speed = 800, rotation_angle = dist_left, wait = False)
            
            curr_time = sw.time()

            if curr_time - start_time > MAX_TIME:
                print("Spent too long on Light Show. Exiting now...")
                break

            wait(10)

    def lightShowTestWith8ToothGear():
        gyroStraightWithDriveWithAccurateDistance(distance=15, speed=400, targetAngle=0,backward=True)
        gyroStraightWithDriveWithAccurateDistance(distance=10, speed=150, targetAngle=0,backward=True)
        wait(100)

        #right_med_motor.run_angle(speed=600, rotation_angle=-3600, wait = True)
        left_med_motor.run_angle(speed=500, rotation_angle=-4000, wait = True)
        
    def lightShowTestWithLoad():
        # NO LOAD: 13.7
        # JUST HITTING LIGHT SHOW: 
        # MOVING LIGHT SHOW: 
        orgSpeed,orgAccel,orgTorque = left_med_motor.control.limits()
        left_med_motor.control.limits(speed = orgSpeed,acceleration = orgAccel,torque = 1000)
        left_med_motor.run_angle(speed = 600, rotation_angle = -2700, wait = False)

        total_load = 0
        occurances = 0
        while left_med_motor.done() == False:
            total_load += left_med_motor.load()
            occurances += 1
            wait(10)

        print("Average Load: " + str(total_load / occurances))

    def museum():
        angle=-40
        # Drive all the way to the before the lightshow
        gyroStraightWithDriveWithAccurateDistance(distance=32, speed=650, targetAngle=angle)

        #Lower the arm to avoid the lightshow
        right_med_motor.run_angle(speed=2000, rotation_angle=-200,wait=False)

        # Turn towards the museum and drive to it
        angle=-60
        turnToAngle(targetAngle=angle, speed=600)
        gyroStraightWithDriveWithAccurateDistance(distance=40, speed=650, targetAngle=angle)

        
        angle=-40
        turnToAngle(targetAngle=angle,speed=600)
        gyroStraightWithDriveWithAccurateDistance(distance=11, speed=650, targetAngle=angle)
        # Drop off the expert and audience
        right_med_motor.run_angle(speed=2000, rotation_angle=400)
        left_med_motor.run_angle(speed=500, rotation_angle=500)

        angle=-90
        turnToAngle(targetAngle=angle, speed=600)
        gyroStraightWithDriveWithAccurateDistance(distance=2, speed=650, targetAngle=angle)

        gyroStraightWithDriveWithAccurateDistance(distance=2, speed=650, targetAngle=angle,backward=True)
        right_med_motor.run_angle(speed=2000, rotation_angle=200)

    def goTomuseumwith2turns():

        angle = -15 
        right_med_motor.run_angle(speed=2000, rotation_angle=-200)
        gyroStraightWithDriveWithAccurateDistance(distance=5, speed=500, targetAngle=angle, backward = True)

        angle=-35
        turnToAngle(targetAngle=angle,speed=400)
        gyroStraightWithDriveWithAccurateDistance(distance=40, speed=400, targetAngle=angle)

        angle=-60
        turnToAngle(targetAngle=angle,speed=400)
        gyroStraightWithDriveWithAccurateDistance(distance=50, speed=400, targetAngle=angle)
        right_med_motor.run_angle(speed=2000, rotation_angle=400,wait=False)
        left_med_motor.run_angle(speed=2000, rotation_angle=500)

        angle=-90
        turnToAngle(targetAngle=angle,speed=400)
        #gyroStraightWithDriveWithAccurateDistance(distance=10, speed=400, targetAngle=angle, backward=True)
        right_med_motor.run_angle(speed=500, rotation_angle=200)

    def museumfaster():
        angle  = -15
        gyroStraightWithDriveWithAccurateDistance(distance=4, speed=1000, targetAngle=angle, backward = True)
        angle=-20
        turnToAngle(targetAngle=angle,speed=400)
        
        #Lower the arm to avoid the lightshow
        #right_med_motor.run_angle(speed=2000, rotation_angle=-200,wait=True)
        #Use a curve to reach in front of the immersive experience
        drive_base.curve(radius=660,angle = -60)
        #right_med_motor.run_angle(speed=2000, rotation_angle=-200,wait=True)
        
        # Now turn to drop off at museum
        angle=-35
        turnToAngle(targetAngle=angle,speed=600)
        gyroStraightWithDriveWithAccurateDistance(distance=22.5, speed=1000, targetAngle=angle)
        # Drop off the expert and audience
        right_med_motor.run_angle(speed=2000, rotation_angle=400,wait=False)
        left_med_motor.run_angle(speed=500, rotation_angle=500)

        angle=-90
        turnToAngle(targetAngle=angle, speed=800)
        #gyroStraightWithDriveWithAccurateDistance(distance=2, speed=650, targetAngle=angle)

        #gyroStraightWithDriveWithAccurateDistance(distance=2, speed=650, targetAngle=angle,backward=True)
        right_med_motor.run_angle(speed=2000, rotation_angle=200)

    def goHome():
        # gyroStraightWithDrive(distanceInCm=10, speed=100, targetAngle=270, backward=True)
        # was 34
        gyroStraightWithDriveWithAccurateDistance(distance=45, speed=800, targetAngle=270, backward=True)

        # Drive backward at a slight angle to ensure that we are catching the
        # expert when going home.
        angle = 187
        turnToAngle(angle, speed=500)
        gyroStraightWithDriveWithAccurateDistance(distance=100, speed=1000, targetAngle=angle, 
                                                slowDown = False, backward = True,
                                                useSlowerAccelerationForBackward = False)
        
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

    def testleftmotor():
        left_med_motor.run_angle(speed=500, rotation_angle=500)

    def testlightShowtime():
        orgSpeed,orgAccel,orgTorque = left_med_motor.control.limits()
        left_med_motor.control.limits(speed = orgSpeed,acceleration = orgAccel,torque = 1000)
        left_med_motor.run_angle(speed=1000, rotation_angle=-2700, wait = True)
        left_med_motor.control.limits(speed = orgSpeed,acceleration = orgAccel,torque = orgTorque)

    def run4Between3dCimenaAndSoundMixer():
        museumStartingPointingForward()

    def testAudienceDropOffAtLightShow():
        gyroStraightWithDriveWithAccurateDistance(distance=12, speed=700, targetAngle=0,backward=True,stop=Stop.COAST)
        gyroStraightWithDriveWithAccurateDistance(distance=9, speed=200, targetAngle=0,backward=True)
        wait(2000)
        gyroStraightWithDriveWithAccurateDistance(distance=12, speed=700, targetAngle=0)
    '''




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

def run4():
    resetRobot()
    runWithTiming(rollingCamera,"rolling camera")
    runWithTiming(museumwithpedestaloutside,"museumwithpedestaloutside")
    runWithTiming(lightShow, "lightshow")
    runWithTiming(immersiveExperience, "ImmersiveExperience")
    runWithTiming(goHomeWithCurve, "goHomeWithCurve")
    
#waitForButtonPress()
#runWithTiming(run4,"Run4")
#testBucket()
# lightShowTestWith8ToothGear()
#lightShowTestWithLoad()
#runWithTiming(lightShowTest, "Light Show")
#resetBucket(angle = 400)
#testAudienceDropOffAtLightShow()
#runWithTiming(testlightShowtime, "lightshowtime")
#drive_base.curve(radius = -150, angle = 180)



