from pybricks.tools import wait, StopWatch
from Utilities import *

def musicConcert():
    # go forward and turn towards the black line
    gyroStraightWithDriveWithAccurateDistance(distance=CM_PER_INCH*17, targetAngle=0, speed=500)

    hub.display.number(1)

    turnToAngle(-45, speed = 300)

    hub.display.number(2)

    # catch the black line
    driveTillLine(speed=400, doCorrection=False, tag="Music Concert")

    hub.display.number(3)

    # align against the wall to drop off Noah & Audience
    gyroStraightWithDriveWithAccurateDistance(distance=CM_PER_INCH*1, targetAngle=-45, speed=500)

    hub.display.number(4)

    turnToAngle(targetAngle=0, oneWheelTurn=False, speed = 300)

    hub.display.number(5)
    
    gyroStraightWithDriveWithAccurateDistance(distance=CM_PER_INCH*10.5, targetAngle=0, speed=500, slowDown = False)

    # lift the arm to deliver the expert and back off
    gyroStraightWithDriveWithAccurateDistance(distance=CM_PER_INCH*10.5, targetAngle=10, backward=True, speed=400)

    # turn towards the Music Concert
    turnToAngle(45)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=CM_PER_INCH*5, targetAngle=45, speed=300) # 11/23 - was 10
    driveForTime(timeInMS=1000, speed=300)
    wait(100)
    left_med_motor.run_angle(-1000, 1500)

def augmentedReality():
    # Back up from music concert and turn towards Augmented Reality
    driveTillBlackLine(speed=300, distanceInCM=15, target_angle=45, backward=True)
    left_med_motor.run_angle(speed = 1000, rotation_angle = 1500, wait = False)
    _angle=-90
    turnToAngle(_angle)

    # go to Augmented Reality
    # gyroStraightWithDrive(distanceInCm=33, targetAngle=_angle, speed = 500)
    gyroStraightWithDriveWithAccurateDistance(distance = 33, speed = 600, targetAngle = _angle)
    _angle = -45
    turnToAngle(targetAngle=_angle,oneWheelTurn=True)

    # back up to pull Augmented Reality lever
    gyroStraightWithDriveWithAccurateDistance(distance=7, speed = 500, targetAngle=_angle)

    _angle = 0
    turnToAngle(targetAngle = _angle, speed = 300)
    gyroStraightWithDriveWithAccurateDistance(distance = 7, speed = 700, targetAngle = 0, backward = True)

    # turn a little more and back up again to make sure the lever caught
    _angle = 20
    turnToAngle(targetAngle=_angle,oneWheelTurn=True, speed = 700)
    gyroStraightWithDriveWithAccurateDistance(distance=13, speed = 500, targetAngle=_angle)
    # turnToAngle(targetAngle = _angle, speed = 300)
    # gyroStraightWithDrive(distanceInCm=12, targetAngle=_angle, backward=True)
    
    # _angle = hub.imu.heading()
    # gyroStraightWithDriveWithAccurateDistance(distance = 8, speed = 300, targetAngle = _angle, backward = True, multiplier = 0.1)
    drive_base.straight(-120)

def expertDrops():
    # turn and start driving towards Sound Mixer
    _angle=-90
    turnToAngle(_angle-5)
    distGyro = gyroStraightWithDrive(distanceInCm=15*CM_PER_INCH, targetAngle=_angle, speed=500)

    # try to catch the white line near Immersive Experience
    distToWhiteLine = driveTillHsvRange(maxDistance=3*MM_PER_INCH, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100), tag="expert dropoffs")
    print("Distances covered so far: {}, {}".format(distGyro, distToWhiteLine))

    # distance from end of Augmented Reality to hitting Sound Mixer
    TOTAL_DIST_TO_TRAVEL = 8 * MM_PER_INCH
    
    # if robot still hasn't gone total distance to travel -> go until total distance to travel
    if(distGyro + distToWhiteLine < TOTAL_DIST_TO_TRAVEL):
        gyroStraightWithDrive(distanceInCm=(TOTAL_DIST_TO_TRAVEL - distGyro - distToWhiteLine)/10, targetAngle=_angle, speed=500)
    else:
        print("No need to correct distance to {}".format(TOTAL_DIST_TO_TRAVEL))

    right_med_motor.run_angle(speed = -600, rotation_angle = 1500, then = Stop.COAST, wait = False)

    gyroStraightWithDriveWithAccurateDistance(distance = 18, speed = 500, targetAngle = _angle)

    _angle = -45
    turnToAngle(targetAngle = _angle, speed = 300)

    gyroStraightWithDriveWithAccurateDistance(distance = 4, speed = 200, targetAngle = _angle)

def run7():
    resetRobot()
    musicConcert()
    augmentedReality()
    expertDrops()

def mainRun7():
    initializeAndWaitForRobotReady()

    print("BATTERY = " + str(hub.battery.voltage()))
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    run7()

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    print("DONE")

# waitForButtonPress()
# mainRun7()
