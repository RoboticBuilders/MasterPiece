from pybricks.tools import wait, StopWatch
from Utilities import *

def openFlippyV2():
    left_med_motor.run_angle(speed = 2000, rotation_angle = 2400)

def closeFlippyV2withoutWait():
     left_med_motor.run_angle(speed = -2000, rotation_angle = 2400, wait = False)

def openFlippy():
    left_med_motor.run_angle(-2000, 1800)

def closeFlippywithoutWait():
     left_med_motor.run_angle(speed = 2000, rotation_angle = 1800, wait = False)


def musicconcert(userV2Flippy = False):
    # Changed 1/26/2024: In order to fix the incorrect line catches now going straight then turning to catch the correct line
    angle = 0
    # First go forward at an angle to catch the black spur line in front
    # of the music concernt.
    gyroStraightWithDriveWithAccurateDistance(distance=45, targetAngle=angle, speed=1000, stop=Stop.COAST)
    angle = -45
    turnToAngle(targetAngle = angle, speed = 300)
    if (gyroStraightWithDriveWithAccurateDistance(distance=30, targetAngle = angle, speed=1000, 
                                    tillBlackLine = True,
                                    color_sensor = right_color) == False):
        print("Run7: musicconcertnew: Missed black line catch infront of music concert")
    gyroStraightWithDriveWithAccurateDistance(distance=6, targetAngle=angle, speed=200)

    # Now turn towards the wall to flush
    angle = 0
    turnToAngle(targetAngle = angle, speed = 500)
    

    # Now drop off the experts
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle=0, speed=1000, stop=Stop.COAST)
    gyroStraightWithDriveWithAccurateDistance(distance=8, targetAngle=0, speed=300)
    driveForTime(timeInMS = 500, stopAtEnd = True, speed = 300, turnRate = 0)

    # Now dropoff is done, lets do music concert. Backoff first at an angle to ensure
    # the experts are in.
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance=25, targetAngle=angle, backward=True, speed=400)

    # turn towards the Music Concert
    angle = 45
    turnToAngle(targetAngle = angle, speed = 300)
    wait(100)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=13, targetAngle=angle, speed=300)
    driveForTime(timeInMS = 750, stopAtEnd=True, speed=200, turnRate=0)
    #driveForTime(timeInMS=500, speed=200)

    # Wait for a little and run Flippy to turn the speakers
    wait(100)
    if userV2Flippy == True:
        openFlippyV2()    
    else:
        openFlippy()

    drive_base.reset()
    wait(100)
    hub.imu.reset_heading(angle)
    
    
    
def augmentedRealitynew(userV2Flippy = False):
    # Back up from music concert and turn towards Augmented Reality
    
    angle = 45
    
    drive_base.straight(-70)
    if (gyroStraightWithDriveWithAccurateDistance(distance=8, targetAngle = angle, speed=300, 
                                    tillBlackLine = True, backward=True,
                                    color_sensor = left_color) == False):
        print("Missed black line catch when backing from music concert")
    #turnToAngle(targetAngle = angle, speed = 400)
    wait(100)
    if userV2Flippy == True:
        closeFlippyV2withoutWait()
    else:
        closeFlippywithoutWait()
    
    gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 200, targetAngle = angle, backward=True)

    # Now drive towars the augmented reality
    angle = -90
    turnToAngle(targetAngle = angle, speed = 500)
    gyroStraightWithDriveWithAccurateDistance(distance=35, targetAngle=angle, speed = 300)

    # wait(augmentedRealityWaitTime)
    angle = -45
    turnToAngle(targetAngle=angle, oneWheelTurn=True)

    # back up to pull Augmented Reality lever
    gyroStraightWithDriveWithAccurateDistance(distance=3, targetAngle=angle, speed = 300)

    # turn a little more and back up again to make sure the lever caught
    angle = 25
    turnToAngle(targetAngle=angle, oneWheelTurn=True, speed = 300)
    gyroStraightWithDriveWithAccurateDistance(distance=10, targetAngle=angle, backward=True, speed = 300)

    # go forward to fully push the lever
    angle = 45
    turnToAngle(targetAngle=angle,oneWheelTurn=True)
    gyroStraightWithDriveWithAccurateDistance(distance=12, targetAngle=angle, speed = 300)

    # back up from Augmented Reality
    angle=30
    turnToAngle(targetAngle=angle,oneWheelTurn=True, forceTurn=FORCETURN_LEFT)
    gyroStraightWithDriveWithAccurateDistance(distance=14, targetAngle=angle, backward=True, speed = 300)

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

def closeAugmentedRealitySliderFully():
    # Close slider to open the augmented reality.
    right_med_motor.run_angle(speed = 400, rotation_angle = 492)

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

def run8():
    resetRobot()
    useFlippyV2 = True
    musicconcert(userV2Flippy = useFlippyV2)
    augmentedRealitynew(userV2Flippy = useFlippyV2)
    # goToRightHome()
    #dropexpertsFromlefthome()
    #expertDropsnew()

def mainRun8():
    initializeAndWaitForRobotReady()

    print("BATTERY = " + str(hub.battery.voltage()))
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    run8()

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    print("DONE")

waitForButtonPress()
mainRun8()