from pybricks.tools import wait, StopWatch # import pybricks tools for timing (see bottom of the code)
from Utilities import * # import utilities

def musicConcert():
    angle = 0

    # go forward
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*17, targetAngle=angle, speed=400)

    angle = -45

    # turn towards the craft creator
    turnToAngle(targetAngle = angle, speed = 300)

    # catch the black line
    driveTillLine(speed=400, doCorrection=False, tag="Music Concert")

    # drive a little farther than the line to avoid hitting the music concert lights & sounds
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*1, targetAngle=angle, speed=400)

    angle = 0

    # turn towards the wall
    turnToAngle(targetAngle=angle, oneWheelTurn=False, speed = 300)
    
    # dropoff noah(expert) and the audience member
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*10.5, targetAngle=angle, speed=400)

    # back off to do the music concert lights & sounds. drive at an angle to make sure they are in (turns right a little)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*10.5, targetAngle=angle + 10, backward=True, speed=400)

    angle = 45

    # turn towards the music concert
    turnToAngle(targetAngle = angle, speed = 300)

    # push the hologram performer
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*5, targetAngle=angle, speed=300)
    driveForTime(timeInMS=1000, speed=300)

    # do the music concert
    wait(100)
    left_med_motor.run_angle(-1000, 1500)

def augmentedReality():
    # back up from the music concert
    driveTillBlackLine(speed=200, distanceInCM=15, targetangle=angle, backward=True)

    # reset the music concert arm in parallel
    left_med_motor.run_angle(speed = 1000, rotationangle = 1500, wait = False)
    
    # turn to get on the left side of augmented reality
    angle = -90
    turnToAngle(targetAngle = angle, speed = 300)

    # drive to get on the left side of augmented reality
    gyroStraightWithDriveWithAccurateDistance(distance = 33, speed = 500, targetAngle = angle)
    
    # go around the augmented reality to get the hook behind the lever
    angle = -45
    turnToAngle(targetAngle = angle, speed = 300, oneWheelTurn = True)

    # back up and pull the lever
    gyroStraightWithDrive(distanceInCm=7, targetAngle = angle)

    angle = 0
    turnToAngle(targetAngle = angle, speed = 300)
    gyroStraightWithDriveWithAccurateDistance(distance = 7, speed = 700, targetAngle = angle, backward = True)

    # turn a little more and make sure to whack the lever
    angle = 20
    turnToAngle(targetAngle=angle, oneWheelTurn=True, speed = 700)

    # push the lever in and make sure that we get full points
    gyroStraightWithDrive(distanceInCm = 13, speed = 300, targetAngle = angle)

    # back up off the augmented reality
    drive_base.straight(-120)

def expertDrops():
    # turn and start driving towards Sound Mixer
    angle = -90
    turnToAngle(targetAngle = angle - 5, speed = 300)

    distGyro = gyroStraightWithDrive(distanceInCm = 15*CM_PER_INCH, targetAngle = angle, speed = 500)

    # catch the white line near the immersive experience
    distToWhiteLine = driveTillHsvRange(maxDistance=3*MM_PER_INCH, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100), tag="expert dropoffs")
    print("Distances covered so far: {}, {}".format(distGyro, distToWhiteLine))

    # calculate the distance left to travel
    TOTAL_DIST_TO_TRAVEL = 8 * MM_PER_INCH
    
    # travel the distance that's left
    if(distGyro + distToWhiteLine < TOTAL_DIST_TO_TRAVEL):
        gyroStraightWithDrive(distanceInCm=(TOTAL_DIST_TO_TRAVEL - distGyro - distToWhiteLine)/10, targetAngle=angle, speed=500)
    else:
        print("No need to correct distance to {}".format(TOTAL_DIST_TO_TRAVEL))

    # start opening the slider arm in parallel
    right_med_motor.run_angle(speed = -1000, rotationangle = 1500, then = Stop.COAST, wait = False)

    # drive forward over the sound mixer
    gyroStraightWithDriveWithAccurateDistance(distance = 18, speed = 400, targetAngle = angle)

    # turn to align with the dropoffs
    angle = -45
    turnToAngle(targetAngle = angle, speed = 300)

    # drive to align with the dropoffs
    gyroStraightWithDriveWithAccurateDistance(distance = 4, speed = 200, targetAngle = angle)

# called in main
def run7():
    resetGyro(0) # reset the angle
    musicConcert() # do the expert & audience member dropoffs, and the hologram performer & music concert lights & sounds
    augmentedReality() # do the augmented reality
    expertDrops() # do the drop of the 2 experts and audience members

# internal function for testing
def mainRun7():
    initializeAndWaitForRobotReady()

    print("BATTERY = " + str(hub.battery.voltage()))
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    run7()

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    print("DONE")

# comment out for full run
waitForButtonPress()
mainRun7()