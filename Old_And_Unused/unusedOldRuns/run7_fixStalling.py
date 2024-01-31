from pybricks.tools import wait, StopWatch
from Utilities import *

(origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
CIRCULAR_MOTION_ARM_DEGREES=480
CIRCULAR_MOTION_ARM_SPEED=1000
EXPERT_ARM_TURN_ANGLE = 380
DROP_OFF_SPEED = 300
EXPERT_ARM_CONTROL = right_med_motor

def resetCircularMotionArm(wait=True):
    left_med_motor.run_angle(speed=CIRCULAR_MOTION_ARM_SPEED,rotation_angle=-1*CIRCULAR_MOTION_ARM_DEGREES, wait=wait)

debugStalling=False
debugStallingWaitTime=3000
def doMusicConcert():
    # go forward and turn towards the black line
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*17, targetAngle=0, speed=600)
    turnToAngle(-45)

    # catch the black line
    driveTillLine(speed=300, doCorrection=False, tag="Music Concert")

    # align against the wall to drop off Noah & Audience
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*1, targetAngle=-45, speed=600)
    turnToAngle(targetAngle=0, oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*4, targetAngle=0, speed=500) # was 6.5 before driveForTime change
    if(debugStalling):
        hub.speaker.beep()
        hub.display.char("W")
        wait(debugStallingWaitTime)
    driveForTime(timeInMS=1000, speed=500)
    if(debugStalling):
        hub.speaker.beep()
        hub.display.char("X")
        wait(debugStallingWaitTime)

    # lift the arm to deliver the expert and back off
    left_med_motor.run_angle(speed=CIRCULAR_MOTION_ARM_SPEED,rotation_angle=-150)
    if(debugStalling):
        hub.speaker.beep()
        hub.display.char("Y")
        wait(debugStallingWaitTime)

    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*10.5, targetAngle=10, backward=True, speed=400)
    if(debugStalling):
        hub.speaker.beep()
        hub.display.char("Z")
        wait(debugStallingWaitTime)

    # turn towards the Music Concert
    _angle=45
    turnToAngle(_angle)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*5, targetAngle=_angle, speed=400) # 11/23 - was 10
    if(debugStalling):
        hub.speaker.beep()
        hub.display.char("A")
        wait(debugStallingWaitTime)
    driveForTime(timeInMS=1000, speed=400)
    if(debugStalling):
        hub.display.char("B")
        hub.speaker.beep()
        wait(debugStallingWaitTime)
    # turnToAngle(targetAngle=53, forceTurn=FORCETURN_RIGHT, oneWheelTurn=True)
    driveForTime(timeInMS=100, stopAtEnd=False, speed=200, turnRate=-15)
    if(debugStalling):
        hub.display.char("C")
        hub.speaker.beep()
        wait(debugStallingWaitTime)
    left_med_motor.run_angle(speed=CIRCULAR_MOTION_ARM_SPEED,rotation_angle=CIRCULAR_MOTION_ARM_DEGREES)
    if(debugStalling):
        hub.display.char("D")
        hub.speaker.beep()
        wait(debugStallingWaitTime)

def doAugmentedReality():
    # resetGyro(angle=45)

    # Back up from music concert and turn towards Augmented Reality
    goStraight(MM_PER_INCH*-5, straightSpeed=300)
    _angle=-90
    turnToAngle(_angle)

    # Reset circular motion arm in parallel to avoid it hitting Craft Creator
    resetCircularMotionArm(wait=False)

    # go to Augmented Reality
    gyroStraightWithDrive(distanceInCm=35, targetAngle=_angle)
    _angle = -45
    turnToAngle(targetAngle=_angle,oneWheelTurn=True)

    # back up to pull Augmented Reality lever
    gyroStraightWithDrive(distanceInCm=3, targetAngle=_angle)

    # turn a little more and back up again to make sure the lever caught
    _angle = 25
    turnToAngle(targetAngle=_angle,oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=12, targetAngle=_angle, backward=True)

    # go forward to fully push the lever
    _angle = 35
    turnToAngle(targetAngle=_angle,oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=12, targetAngle=_angle)

    # back up from Augmented Reality
    _angle=30
    turnToAngle(targetAngle=_angle,oneWheelTurn=True, forceTurn=FORCETURN_LEFT)
    gyroStraightWithDrive(distanceInCm=12, targetAngle=_angle, backward=True)

def dropOneExpert(numDropoffRotations=1, wait=True):
    right_med_motor.run_angle(speed=DROP_OFF_SPEED,rotation_angle=numDropoffRotations*EXPERT_ARM_TURN_ANGLE, wait=wait)

def resetExpertDropOffArm(numRotations=2):
    if(numRotations>0):
        right_med_motor.run_angle(speed=-DROP_OFF_SPEED,rotation_angle=numRotations*EXPERT_ARM_TURN_ANGLE)

def ballerina5_ExpertDropOffs():
    # turn and start driving towards Sound Mixer
    _angle=-90
    turnToAngle(_angle)
    distGyro = gyroStraightWithDrive(distanceInCm=15*CM_PER_INCH, targetAngle=_angle, speed=500)

    # try to catch the white line near Immersive Experience
    distToWhiteLine = driveTillHsvRange(maxDistance=3*MM_PER_INCH, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100), tag="expert dropoffs")
    print("Distances covered so far: {}, {}".format(distGyro, distToWhiteLine))

    # distance from end of Augmented Reality to hitting Sound Mixer
    TOTAL_DIST_TO_TRAVEL = 21*MM_PER_INCH
    
    # if robot still hasn't gone total distance to travel -> go until total distance to travel
    if(distGyro + distToWhiteLine < TOTAL_DIST_TO_TRAVEL):
        gyroStraightWithDrive(distanceInCm=(TOTAL_DIST_TO_TRAVEL - distGyro - distToWhiteLine)/10, targetAngle=_angle, speed=500)
    else:
        print("No need to correct distance to {}".format(TOTAL_DIST_TO_TRAVEL))

    _angle=-45
    turnToAngle(_angle)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*2, targetAngle=_angle)

    _angle=-90
    turnToAngle(_angle)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*7, targetAngle=_angle)

    _angle=-45
    dropOneExpert(numDropoffRotations=1, wait=False)
    turnToAngle(_angle)
    gyroStraightWithDrive(speed=100, distanceInCm=2*CM_PER_INCH, targetAngle=_angle)
    while(not EXPERT_ARM_CONTROL.done()):
        wait(10)

def run7():
    resetGyro(0)
    doMusicConcert()
    doAugmentedReality()
    ballerina5_ExpertDropOffs()

def mainRun7():
    print("Calling func now")
    initializeAndWaitForRobotReady()

    print("BATTERY = " + str(hub.battery.voltage()))
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    run7()

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    # Reset dropoff arm
    wait(5000)
    resetExpertDropOffArm()

    print("DONE")

waitForButtonPress()
mainRun7()