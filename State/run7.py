from pybricks.tools import wait, StopWatch
from Utilities import *

def openFlippy():
    left_med_motor.run_angle(-2000, 1800)

def closeFlippywithoutWait():
     left_med_motor.run_angle(speed = 2000, rotation_angle = 1800, wait = False)


def musicconcert():
    angle = -20
    # First go forward at an angle to catch the black spur line in front
    # of the music concernt.
    if (gyroStraightWithDriveWithAccurateDistance(distance=70, targetAngle = angle, speed=1000, 
                                    tillBlackLine = True,
                                    color_sensor = right_color) == False):
        print("Run7: musicconcertnew: Missed black line catch infront of music concert")
    
    # Now turn towards the wall to flush
    angle = 0
    turnToAngle(targetAngle = angle, speed = 500)

    # Now drop off the experts
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle=0, speed=1000, stop=Stop.COAST)
    gyroStraightWithDriveWithAccurateDistance(distance=8, targetAngle=0, speed=300)

    # Now dropoff is done, lets do music concert. Backoff first at an angle to ensure
    # the experts are in.
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance=25, targetAngle=angle, backward=True, speed=400)

    # turn towards the Music Concert
    angle = 45
    turnToAngle(targetAngle = angle, speed = 300)
    wait(100)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=27, targetAngle=angle, speed=300)
    #driveForTime(timeInMS=500, speed=200)

    # Wait for a little and run Flippy to turn the speakers
    wait(100)
    openFlippy()
    wait(100)
    
def augmentedReality():
    # Back up from music concert and turn towards Augmented Reality
    angle = 45
    if (gyroStraightWithDriveWithAccurateDistance(distance=15, targetAngle = angle, speed=300, 
                                    tillBlackLine = True, backward=True,
                                    color_sensor = left_color) == False):
        print("Missed black line catch when backing from music concert")

    # Bring up flippy.
    clsoeFlippywithoutWait()
    gyroStraightWithDriveWithAccurateDistance(distance = 3, speed = 200, targetAngle = angle, backward=True)

    # Now drive towars the augmented reality
    angle = -90
    turnToAngle(targetAngle = angle, speed = 500)

    # go to Augmented Reality
    gyroStraightWithDriveWithAccurateDistance(distance = 36, speed =300, targetAngle = angle) 
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
    gyroStraightWithDriveWithAccurateDistance(distance = 7, speed = 500, targetAngle = angle)
    wait(150)
    # Note that this is a white line catch.
    if (gyroStraightWithDriveWithAccurateDistance(distance = 7, speed = 300, targetAngle = angle, 
                                                  backward = True, tillWhiteLine = True, color_sensor = left_color) == False):
        print("run7: augmentedReality: Did not find whiteline infront of augmented reality when backing up at the end.")
   
    turnToAngle(targetAngle = -90, speed = 750)

def augmentedRealitynew():
    # Back up from music concert and turn towards Augmented Reality
    angle = 45
    if (gyroStraightWithDriveWithAccurateDistance(distance=15, targetAngle = angle, speed=300, 
                                    tillBlackLine = True, backward=True,
                                    color_sensor = left_color) == False):
        print("Missed black line catch when backing from music concert")
    closeFlippywithoutWait()
    gyroStraightWithDriveWithAccurateDistance(distance = 3, speed = 200, targetAngle = angle, backward=True)


    # Now drive towars the augmented reality
    angle = -90
    turnToAngle(targetAngle = angle, speed = 500)

    # go to Augmented Reality
    gyroStraightWithDriveWithAccurateDistance(distance = 24, speed =500, targetAngle = angle,stop=Stop.COAST) 
    if (gyroStraightWithDriveWithAccurateDistance(distance = 14, speed = 300, targetAngle = angle, 
                                                  backward = False, tillWhiteLine = True, color_sensor = left_color) == False):
        print("run7: augmentedReality: Did not find whiteline infront of augmented reality when moving forward towardsit before pulling lever.")
    #After cathing the white line move a little forward so the flippy doesnt snag against the mission model
    drive_base.straight(60)
    # Now open the slider to bring in the augmented reality.
    openAugmentedRealitySlider()
    #Backup to pull the lever
    drive_base.straight(-50)
    closeAugmentedRealitySlider()
    #PullInTheAugmentedRealityLever()

    
    # Now backoff to push the lever in and turn to ensure the lever is turned
    # We backoff at an angle, because the augmented reality opens 
    # and we want to make sure we dont hit it.
    angle = -85
    gyroStraightWithDriveWithAccurateDistance(distance = 20, speed = 1000, targetAngle = angle, backward = True)
    closeAugmentedRealitySliderCompletely()
    # Now turn to ensure that we have pushed in the augmented reality. We turn and drive forward
    # then backoff till the white line and turn back to our heading.
    angle = -30
    turnToAngle(targetAngle = angle, speed = 1000)
    gyroStraightWithDriveWithAccurateDistance(distance = 7, speed = 500, targetAngle = angle)
    wait(150)
    # Note that this is a white line catch.
    if (gyroStraightWithDriveWithAccurateDistance(distance = 7, speed = 300, targetAngle = angle, 
                                                  backward = True, tillWhiteLine = True, color_sensor = left_color) == False):
        print("run7: augmentedReality: Did not find whiteline infront of augmented reality when backing up at the end.")
   
    turnToAngle(targetAngle = -90, speed = 500)   
    
def expertDropsnew():
    # Travel a total of 100cm till the Sound mixer. 
    # We travel straight first, to get past the light show, then
    # we turn slighly towards the sound mixer to ensure we dont hit the immersive exp.
    # then we turn slightly towards the wall to ensure we dont hit the sound mixer.
    angle = -90
    gyroStraightWithDriveWithAccurateDistance(distance = 50, speed = 700, targetAngle = angle)
    
    angle = -100
    turnToAngle(targetAngle=angle, speed=500)
    gyroStraightWithDriveWithAccurateDistance(distance = 18, speed = 700, targetAngle = angle)
    
    angle = -70
    turnToAngle(targetAngle=angle, speed=500)
    distToWhiteLineMM = driveTillHsvRange(maxDistance=160, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100), tag="expert dropoffs")
    
    gyroStraightWithDriveWithAccurateDistance(distance = 23, speed = 500, targetAngle = angle)
    
    # Now turn towards the wall and align.
    angle = 0
    turnToAngle(targetAngle=angle, speed=300)
    gyroStraightWithDriveWithAccurateDistance(distance=19, targetAngle=angle, speed=300)

    # now open the arms.
    right_med_motor.run_angle(speed = -400, rotation_angle = 600, wait=False)
    gyroStraightWithDriveWithAccurateDistance(distance=15, backward=True, targetAngle=0, speed=300)
    turnToAngle(targetAngle=-38, speed=300)
    


def expertDropsWithCurve():
    # Travel a total of 100cm till the Sound mixer. 
    # We travel straight first, to get past the light show, then
    # we turn slighly towards the sound mixer to ensure we dont hit the immersive exp.
    # then we turn slightly towards the wall to ensure we dont hit the sound mixer.
    angle = -90
    gyroStraightWithDriveWithAccurateDistance(distance = 55, speed = 700, targetAngle = angle)
    
    #drive_base.curve(radius=480,angle = 45)
    '''
    # now open the arms.
    right_med_motor.run_angle(speed = 400, rotation_angle = 600, wait=False)
    gyroStraightWithDriveWithAccurateDistance(distance=15, backward=True, targetAngle=0, speed=300)
    turnToAngle(targetAngle=-45, speed=300)    
    '''
    
def expertDrops():
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
def goToRightHome():
    print("in gotorighthome")

def testFlippy():
    while(True):
        wait(1000)
        left_med_motor.run_angle(-1000, 1500)
        wait(1000)
        left_med_motor.run_angle(1000, 1500)

def resetFlippy(): 
    left_med_motor.run_angle(1000, 1500)
def openAugmentedRealitySlider():
    # Now open the slider to bring in the augmented reality.
     right_med_motor.run_angle(speed = -400, rotation_angle = 492)

def closeAugmentedRealitySlider():
    # Close slider to open the augmented reality.
    right_med_motor.run_angle(speed = 400, rotation_angle = 442)
def closeAugmentedRealitySliderCompletely():
    # Close slider to open the augmented reality.
    right_med_motor.run_angle(speed = 400, rotation_angle = 50)

def PullInTheAugmentedRealityLever():
    # Now open the slider to bring in the augmented reality.
    #Changed from 550 to 540 since it was stalling sometimes
    right_med_motor.run_angle(speed = -400, rotation_angle = 492)
    wait(100)
    # Close slider to open the augmented reality.
    right_med_motor.run_angle(speed = 400, rotation_angle = 492)

def PullInTheAugmentedLeverWithStallDetect():
    # Now move out to pull the lever
    right_med_motor.run(400)
    distance_to_travel = 400
    dist_travelled = 0
    init_distance = abs(right_med_motor.angle())
    #print(init_distance)
    while(right_med_motor.stalled() == False and dist_travelled < distance_to_travel):
        curr = abs(right_med_motor.angle())
        print(curr)
        dist_travelled = curr - init_distance

    right_med_motor.hold()    

    wait(100)
    # Now pull the lever in...
    right_med_motor.run_angle(speed = -400, rotation_angle = 400)

def testSliderOpenAndClose():

     right_med_motor.run_angle(speed = -400, rotation_angle = 492)
     wait(2000)
     right_med_motor.run_angle(speed = 400, rotation_angle = 492)
    
    #while (True):
    #    wait(1000)
    #    PullInTheAugmentedRealityLever()

def run7ayaantable():
    resetRobot()
    #testCrazyMovement()
    #hub.imu.reset_heading(45)
    musicconcert()
    augmentedRealitynew()
    goToRightHome()
    #dropexpertsFromlefthome()
    #expertDropsnew()

def mainRun7():
    initializeAndWaitForRobotReady()

    print("BATTERY = " + str(hub.battery.voltage()))
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    run7()

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    print("DONE")

