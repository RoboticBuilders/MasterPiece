from pybricks.tools import wait, StopWatch
from Utilities import *

def openFlippyV2():
    left_med_motor.run_angle(speed = 2000, rotation_angle=1800)

def closeFlippyV2withoutWait():
     left_med_motor.run_angle(speed = -2000, rotation_angle = 1800, wait = False)

def openFlippy():
    left_med_motor.run_angle(rotation_angle=-3000, speed=2000)

def closeFlippywithoutWait():
     left_med_motor.run_angle(speed = 2000, rotation_angle = 3000, wait = False)


def musicconcert(userV2Flippy = False):
    # First drive forward, and then turn to catch the black spur.
    angle = 0
    gyroStraightWithDriveWithAccurateDistance(distance=45, targetAngle=angle, speed=1000)

    # Turn to catch the black spur and drive till black line.
    angle = -45
    turnToAngle(targetAngle = angle, speed = 300)
    if (gyroStraightWithDriveWithAccurateDistance(distance=30, targetAngle = angle, speed=1000, 
                                    tillBlackLine = True,
                                    color_sensor = right_color) == False):
        print("Run8: musicconcertnew: Missed black line catch infront of music concert")
   
    # Now drive forward 2cm, we use drive_base.
    drive_base.straight(20)

    # Now turn towards the wall to flush
    angle = 0
    turnToAngle(targetAngle = angle, speed = 300)

    # Now drop off the experts
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle=0, speed=500)
    driveForTime(timeInMS = 500, stopAtEnd = True, speed = 300, turnRate = 0)

    # Now dropoff is done, lets do music concert. Backoff first at an angle to ensure
    # the experts are in.
    angle = 5
    gyroStraightWithDriveWithAccurateDistance(distance=25, targetAngle=angle, backward=True, speed=300)

    # turn towards the Music Concert
    angle = 45
    turnToAngle(targetAngle = angle, speed = 300)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=13, targetAngle=angle, speed=300)
    driveForTime(timeInMS = 750, stopAtEnd=True, speed=200, turnRate=0)

    # Wait for a little and run Flippy to turn the speakers
    if userV2Flippy == True:
        openFlippyV2()    
    else:
        openFlippy()

    drive_base.reset()
    wait(50)
    hub.imu.reset_heading(angle)
    
def augmentedRealitynew(userV2Flippy = False):
    # Back up from music concert and turn towards Augmented Reality
    # We set the angle to the one that we are at currently, since we dont
    # want the robot to backup at an angle, we want to just
    # backup at the same angle it is at.
    #angle = 45
    angle = hub.imu.heading()
    
    drive_base.straight(-70)
    if (gyroStraightWithDriveWithAccurateDistance(distance=8, targetAngle = angle, speed=300, 
                                    tillBlackLine = True, backward=True,
                                    color_sensor = left_color) == False):
        print("Missed black line catch when backing from music concert")
    if userV2Flippy == True:
        closeFlippyV2withoutWait()
    else:
        closeFlippywithoutWait()
    
    #gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 200, targetAngle = angle, backward=True)
    drive_base.straight(-30)

    # Now drive towars the augmented reality
    angle = -90
    turnToAngle(targetAngle = angle, speed = 500)
    #waitForButtonPress()

    # go to Augmented Reality
    gyroStraightWithDriveWithAccurateDistance(distance = 42, speed = 500, targetAngle = angle) 
    
    # Now open the slider to bring in the augmented reality.
    openAugmentedRealitySlider()

    #waitForButtonPress()

    # Backup to pull the lever
    drive_base.straight(-40)
    
    #closeAugmentedRealitySlider()
    closeAugmentedRealitySliderFully()
    #PullInTheAugmentedRealityLever()
    
    # Now backoff to push the lever in and turn to ensure the lever is turned
    # We backoff at an angle, because the augmented reality opens 
    # and we want to make sure we dont hit it.
    angle = -90
    gyroStraightWithDriveWithAccurateDistance(distance = 20, speed = 1000, targetAngle = angle, backward = True)
    #closeAugmentedRealitySliderCompletely()
    
    # Now turn to ensure that we have pushed in the augmented reality. We turn and drive forward
    # then backoff till the white line and turn back to our heading.
    angle = -30
    turnToAngle(targetAngle = angle, speed = 1000)
    gyroStraightWithDriveWithAccurateDistance(distance = 8, speed = 500, targetAngle = angle)
    

def augmentedRealityWithCurve(userV2Flippy = False):
    # Back up from music concert and turn towards Augmented Reality
    # We set the angle to the one that we are at currently, since we dont
    # want the robot to backup at an angle, we want to just
    # backup at the same angle it is at.
    #angle = 45
    angle = hub.imu.heading()
    
    drive_base.straight(-70)
    if (gyroStraightWithDriveWithAccurateDistance(distance=8, targetAngle = angle, speed=300, 
                                    tillBlackLine = True, backward=True,
                                    color_sensor = left_color) == False):
        print("Missed black line catch when backing from music concert")
    if userV2Flippy == True:
        closeFlippyV2withoutWait()
    else:
        closeFlippywithoutWait()
    
    gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 200, targetAngle = angle, backward=True)

    # Now drive towars the augmented reality
    angle = -90
    turnToAngle(targetAngle = angle, speed = 500)
    #waitForButtonPress()

    # go to Augmented Reality
    gyroStraightWithDriveWithAccurateDistance(distance = 42, speed = 500, targetAngle = angle) 
    
    # Now open the slider to bring in the augmented reality.
    openAugmentedRealitySlider()

    #waitForButtonPress()

    # Backup to pull the lever
    drive_base.straight(-40)
    
    closeAugmentedRealitySlider()
    #closeAugmentedRealitySliderFully()
    drive_base.curve(angle = 90, radius = -300)
    
    '''
    # Now backoff to push the lever in and turn to ensure the lever is turned
    # We backoff at an angle, because the augmented reality opens 
    # and we want to make sure we dont hit it.
    angle = -90
    gyroStraightWithDriveWithAccurateDistance(distance = 20, speed = 1000, targetAngle = angle, backward = True)
    #closeAugmentedRealitySliderCompletely()
    
    # Now turn to ensure that we have pushed in the augmented reality. We turn and drive forward
    # then backoff till the white line and turn back to our heading.
    angle = -30
    turnToAngle(targetAngle = angle, speed = 1000)
    gyroStraightWithDriveWithAccurateDistance(distance = 8, speed = 500, targetAngle = angle)
    '''

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
     right_med_motor.run_angle(speed = -2000, rotation_angle = 492)

def closeAugmentedRealitySlider():
    # Close slider to open the augmented reality.
    right_med_motor.run_angle(speed = 2000, rotation_angle = 420)

def closeAugmentedRealitySliderCompletely():
    # Close slider to open the augmented reality.
    right_med_motor.run_angle(speed = 400, rotation_angle = 50)

def closeAugmentedRealitySliderFully():
    # Close slider to open the augmented reality.
    right_med_motor.run_angle(speed = 400, rotation_angle = 492)

def testSliderOpenAndClose():
     right_med_motor.run_angle(speed = -400, rotation_angle = 492)
     wait(2000)
     right_med_motor.run_angle(speed = 400, rotation_angle = 492)
    

def run8():
    resetRobot()
    useFlippyV2 = False
    musicconcert(userV2Flippy = useFlippyV2)
    augmentedRealitynew(userV2Flippy = useFlippyV2)
    #augmentedRealityWithCurve(userV2Flippy = useFlippyV2)
    
def mainRun8():
    initializeAndWaitForRobotReady()

    print("BATTERY = " + str(hub.battery.voltage()))
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    run8()

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    print("DONE")

# waitForButtonPress()
# run8()