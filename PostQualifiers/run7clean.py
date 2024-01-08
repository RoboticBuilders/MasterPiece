from pybricks.tools import wait, StopWatch
from Utilities import *

# THis is not working code that we are trying to make work with a flappy arm.

def musicConcert():
    # go forward and turn towards the black line
    gyroStraightWithDriveWithAccurateDistance(distance=43, targetAngle=0, speed=700)

    #hub.display.number(1)

    turnToAngle(targetAngle = -45, speed = 700)

    #hub.display.number(2)

    # # catch the black line
    # driveTillLine(speed=500, doCorrection=False, tag="Music Concert")

    #hub.display.number(3)

    gyroStraightWithDriveWithAccurateDistance(distance = 22, speed = 500, targetAngle = -45)

    drive_base.curve(radius = 300, angle = 45)

    wait(250)

    #hub.display.number(5)
    
    gyroStraightWithDriveWithAccurateDistance(distance=26, targetAngle=0, speed=500, slowDown = False)

    # lift the arm to deliver the expert and back off
    gyroStraightWithDriveWithAccurateDistance(distance=7, targetAngle=10, backward=True, speed=400)
    gyroStraightWithDriveWithAccurateDistance(distance=19, targetAngle=-20, backward=True, speed=400)

    # turn towards the Music Concert
    turnToAngle(targetAngle = 45, speed = 300)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=13, targetAngle=45, speed=300)
    driveForTime(timeInMS=1000, speed=300)

    # Wait for a little and run Flippy to turn the speakers
    wait(100)

    left_med_motor.run_angle(-1000, 1500)

    wait(100)

def musicconcertnew():
    angle = -20
    # First go forward at an angle to catch the black spur line in front
    # of the music concernt.
    if (gyroStraightWithDriveWithAccurateDistance(distance=70, targetAngle = angle, speed=1000, 
                                    tillBlackLine = True,
                                    color_sensor = right_color) == False):
        print("Run7: musicconcertnew: Missed black line catch infront of music concert")
    
    # Now turn towards craft creator 
    angle = 0
    turnToAngle(targetAngle = angle, speed = 500)

    # Now drop off the experts
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle=0, speed=1000, stop=Stop.COAST)
    gyroStraightWithDriveWithAccurateDistance(distance=8, targetAngle=0, speed=300)

    # Now dropoff is done, lets do music concert
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance=25, targetAngle=angle, backward=True, speed=400)

    # turn towards the Music Concert
    turnToAngle(targetAngle = 45, speed = 300)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=13, targetAngle=45, speed=300)
    driveForTime(timeInMS=1000, speed=200)

    # Wait for a little and run Flippy to turn the speakers
    wait(100)
    left_med_motor.run_angle(-1000, 1500)
    wait(100)

    '''
    #Now turn towards craft creator 
    turnToAngle(targetAngle = -90, speed = 700)
    # Now curve to reach expert dropoff area
    drive_base.curve(radius=250,angle = 90)
    # Go straight and dropoff the expert
    gyroStraightWithDriveWithAccurateDistance(distance=15, targetAngle=0, speed=700)

    # Now dropoff is done, lets do music concert

    gyroStraightWithDriveWithAccurateDistance(distance=7, targetAngle=10, backward=True, speed=400)
    gyroStraightWithDriveWithAccurateDistance(distance=19, targetAngle=-20, backward=True, speed=400)

    # turn towards the Music Concert
    turnToAngle(targetAngle = 45, speed = 300)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=13, targetAngle=45, speed=300)
    driveForTime(timeInMS=1000, speed=300)

    # Wait for a little and run Flippy to turn the speakers
    wait(100)

    left_med_motor.run_angle(-1000, 1500)

    wait(100)
    '''

def augmentedRealitynew():
    # Back up from music concert and turn towards Augmented Reality
    angle = 45
    if (gyroStraightWithDriveWithAccurateDistance(distance=15, targetAngle = angle, speed=300, 
                                    tillBlackLine = True, backward=True,
                                    color_sensor = left_color) == False):
        print("Missed black line catch when backing from music concert")
    left_med_motor.run_angle(speed = 1000, rotation_angle = 1500, wait = False)
    gyroStraightWithDriveWithAccurateDistance(distance = 2, speed = 200, targetAngle = angle, backward=True)
    angle = -90
    turnToAngle(targetAngle = angle, speed = 500)

    # go to Augmented Reality
    gyroStraightWithDriveWithAccurateDistance(distance = 37, speed =300, targetAngle = angle)
        
    # Now open the slider to bring in the augmented reality.
    PullInTheAugmentedRealityLever()

    # Now backoff to push the lever in and turn to ensure the lever is turned
    # We backoff at an angle, because the augmented reality opens 
    # and we want to make sure we dont hit it.
    angle = -88
    gyroStraightWithDriveWithAccurateDistance(distance = 20, speed = 1000, targetAngle = angle, backward = True)

    # Now turn to ensure that we have pushed in the augmented reality. We turn and drive forward
    # then backoff till the white line and turn back to our heading.
    angle = -30
    turnToAngle(targetAngle = angle, speed = 1000)
    gyroStraightWithDriveWithAccurateDistance(distance = 5, speed = 500, targetAngle = angle)
    #gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 500, targetAngle = angle, backward = True)
    # Note that this is a white line catch.
    if (gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 300, targetAngle = angle, 
                                                  backward = True, tillWhiteLine = True) == False):
        print("run7: augmentedReality: Did not find whiteline infront of augmented reality when backingup at the end.")
    turnToAngle(targetAngle = -90, speed = 750)
    
def augmentedReality():
    # Back up from music concert and turn towards Augmented Reality
    angle = 45
    if (gyroStraightWithDriveWithAccurateDistance(distance=15, targetAngle = angle, speed=300, 
                                    tillBlackLine = True, backward=True,
                                    color_sensor = left_color) == False):
        print("Missed black line catch when backing from music concert")
    left_med_motor.run_angle(speed = 1000, rotation_angle = 1500, wait = False)
    gyroStraightWithDriveWithAccurateDistance(distance = 2, speed = 800, targetAngle = angle,backward=True)
    angle = -90
    turnToAngle(targetAngle = angle, speed = 500)

    
    # go to Augmented Reality
    # gyroStraightWithDrive(distanceInCm=33, targetAngle=_angle, speed = 500)
    gyroStraightWithDriveWithAccurateDistance(distance = 36, speed = 800, targetAngle = angle)
    
    _angle = -45
    turnToAngle(targetAngle=_angle,oneWheelTurn=True)

    # Now move forward to be setup to pull the augmented reality lever
    gyroStraightWithDriveWithAccurateDistance(distance=6, speed = 500, targetAngle=_angle)

    wait(100)
    # turnToAngle(targetAngle = _angle, speed = 300)
    drive_base.turn(angle = 35, wait = False)

    while not drive_base.done():
        if drive_base.stalled():
            drive_base.stop()
    gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 700, targetAngle = 0, backward = True)

    angle = -90
    turnToAngle(targetAngle=angle,speed=300)
    gyroStraightWithDriveWithAccurateDistance(distance = 30, speed = 1000, targetAngle = angle,backward = True)
    
    turnToAngle(targetAngle = 0, speed = 1000)
    turnToAngle(targetAngle = -90, speed = 750)
    
def expertDropsnew():
    angle = -90
    drive_base.reset()
    startDist = drive_base.distance()
    gyroStraightWithDriveWithAccurateDistance(distance = 68, speed = 500, targetAngle = angle)
    endDist = drive_base.distance()
    distGyroMM = endDist - startDist

    # try to catch the white line near Immersive Experience
    # maxdistance is in mm.
    distToWhiteLineMM = driveTillHsvRange(maxDistance=140, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100), tag="expert dropoffs")
    print("Distances covered so far: {}mm, {}mm".format(distGyroMM, distToWhiteLineMM))

    # distance from end of Augmented Reality to hitting Sound Mixer
    TOTAL_DIST_TO_TRAVEL_MM = 1003

    # if robot still hasn't gone total distance to travel -> go until total distance to travel
    if(distGyroMM + distToWhiteLineMM < TOTAL_DIST_TO_TRAVEL_MM):
        gyroStraightWithDriveWithAccurateDistance(distance=(TOTAL_DIST_TO_TRAVEL_MM - distGyroMM - distToWhiteLineMM)/10, targetAngle=-75, speed=500)
    else:
        print("No need to correct distance to {}".format(TOTAL_DIST_TO_TRAVEL_MM))


    # Now turn and open the bucket.
    # Now open the expert drop off arms.
    right_med_motor.run_angle(speed = 600, rotation_angle = 600, wait=False)
    angle = -47
    turnToAngle(targetAngle = angle, speed = 300)
    gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 500, targetAngle = -47)
   

def expertDrops():
    gyroStraightWithDriveWithAccurateDistance(distance = 30, speed = 700, targetAngle = -90)
    
    # turn and start driving towards Sound Mixer
    distGyro = gyroStraightWithDrive(distanceInCm=15*CM_PER_INCH, targetAngle=-75, speed=500)

    # try to catch the white line near Immersive Experience
    distToWhiteLine = driveTillHsvRange(maxDistance=3*MM_PER_INCH, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100), tag="expert dropoffs")
    #print("Distances covered so far: {}, {}".format(distGyro, distToWhiteLine))

    # distance from end of Augmented Reality to hitting Sound Mixer
    TOTAL_DIST_TO_TRAVEL = 8 * MM_PER_INCH
    
    # if robot still hasn't gone total distance to travel -> go until total distance to travel
    if(distGyro + distToWhiteLine < TOTAL_DIST_TO_TRAVEL):
        gyroStraightWithDrive(distanceInCm=(TOTAL_DIST_TO_TRAVEL - distGyro - distToWhiteLine)/10, targetAngle=_angle, speed=500)
    else:
        print("No need to correct distance to {}".format(TOTAL_DIST_TO_TRAVEL))

    # Now updated to negative for the new attachment
    right_med_motor.run_angle(speed = -600, rotation_angle = 700, then = Stop.COAST, wait = False)

    gyroStraightWithDriveWithAccurateDistance(distance = 18, speed = 500, targetAngle = -75)

    _angle = -45
    turnToAngle(targetAngle = _angle, speed = 300)

    gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 600, targetAngle = _angle)

def resetFlippy():
    left_med_motor.run_angle(1000, 1500)

def PullInTheAugmentedRealityLever():
    # Now open the slider to bring in the augmented reality.
    right_med_motor.run_angle(speed = 600, rotation_angle = 550)
    wait(100)
    # Close slider to open the augmented reality.
    right_med_motor.run_angle(speed = -600, rotation_angle = 550)

def testSliderOpenAndClose():
    while (True):
        wait(1000)
        PullInTheAugmentedRealityLever()

def run7():
    resetRobot()
    #hub.imu.reset_heading(45)
    #musicConcert()
    #resetFlippy()
    #augmentedReality()
    #expertDrops()
    
    musicconcertnew()
    augmentedRealitynew()
    expertDropsnew()

def mainRun7():
    initializeAndWaitForRobotReady()

    print("BATTERY = " + str(hub.battery.voltage()))
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    run7()

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    print("DONE")

waitForButtonPress()
mainRun7()