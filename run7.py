from pybricks.tools import wait, StopWatch
from Utilities import *

(origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
CIRCULAR_MOTION_ARM_DEGREES=480
CIRCULAR_MOTION_ARM_SPEED=1000
augmentedRealityWaitTime=0
EXPERT_ARM_TURN_ANGLE = 1000
DROP_OFF_SPEED = 300
EXPERT_ARM_CONTROL = right_med_motor
anyaRun2Wait = 0
anyaDropOffsWait_B5 = 0
anyaDropOffsWait = 0

def resetCircularMotionArm(wait=True):
    left_med_motor.run_angle(speed=CIRCULAR_MOTION_ARM_SPEED,rotation_angle=-1*CIRCULAR_MOTION_ARM_DEGREES, wait=wait)

def doMusicConcert():
    # go forward and turn towards the black line
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*17, targetAngle=0, speed=600)
    turnToAngle(-45)

    # catch the black line
    driveTillLine(speed=300, doCorrection=False, tag="Music Concert")

    # align against the wall to drop off Noah & Audience
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*1, targetAngle=-45, speed=600)
    turnToAngle(targetAngle=0, oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*6.5, targetAngle=0, speed=500)

    # lift the arm to deliver the expert and back off
    # left_med_motor.run_angle(speed=CIRCULAR_MOTION_ARM_SPEED,rotation_angle=-150) 
    left_med_motor.run_time(speed=-1*CIRCULAR_MOTION_ARM_SPEED, time=500, wait=True)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*10.5, targetAngle=10, backward=True, speed=400)

    # turn towards the Music Concert
    turnToAngle(45)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*5, targetAngle=45, speed=400) # 11/23 - was 10
    hub.display.char("X")
    driveForTime(timeInMS=1000, speed=400)
    # gyroStraightWithDrive(distanceInCm=CM_PER_INCH*3, targetAngle=45, speed=400) # 11/23 - was 10
    hub.display.char("Y")
    #driveForTime(timeInMS=200, stopAtEnd=False, speed=200, turnRate=15)
    # turnToAngle(targetAngle=53, forceTurn=FORCETURN_RIGHT, oneWheelTurn=True)
    hub.display.char("Z")
    # wait(anyaRun2Wait)
    # left_med_motor.run_angle(speed=CIRCULAR_MOTION_ARM_SPEED,rotation_angle=CIRCULAR_MOTION_ARM_DEGREES)
    left_med_motor.run_time(speed=CIRCULAR_MOTION_ARM_SPEED, time=1000, wait=True)

def doAugmentedReality():
    # resetGyro(angle=45)

    # Back up from music concert and turn towards Augmented Reality
    hub.display.char("A")
    # wait(1000)
    # drive_base.straight(distance=-5.5*MM_PER_INCH)
    driveTillBlackLine(speed=200, distanceInCM=15, target_angle=45, backward=True)
    hub.display.char("B")
    _angle=-90
    turnToAngle(_angle)
    hub.display.char("C")

    # Reset circular motion arm in parallel to avoid it hitting Craft Creator
    # resetCircularMotionArm(wait=False)
    left_med_motor.run_time(speed=-1*CIRCULAR_MOTION_ARM_SPEED, time=1000, wait=False)
    hub.display.char("D")

    # go to Augmented Reality
    gyroStraightWithDrive(distanceInCm=35, targetAngle=_angle)
    hub.display.char("E")
    # wait(augmentedRealityWaitTime)
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
    # wait(anyaDropOffsWait_B5)
    distGyro = gyroStraightWithDrive(distanceInCm=15*CM_PER_INCH, targetAngle=_angle, speed=500)
    # wait(anyaDropOffsWait_B5)

    # try to catch the white line near Immersive Experience
    distToWhiteLine = driveTillHsvRange(maxDistance=3*MM_PER_INCH, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100), tag="expert dropoffs")
    print("Distances covered so far: {}, {}".format(distGyro, distToWhiteLine))
    # wait(anyaDropOffsWait_B5)

    # distance from end of Augmented Reality to hitting Sound Mixer
    TOTAL_DIST_TO_TRAVEL = 21*MM_PER_INCH
    
    # if robot still hasn't gone total distance to travel -> go until total distance to travel
    if(distGyro + distToWhiteLine < TOTAL_DIST_TO_TRAVEL):
        gyroStraightWithDrive(distanceInCm=(TOTAL_DIST_TO_TRAVEL - distGyro - distToWhiteLine)/10, targetAngle=_angle, speed=500)
        # wait(anyaDropOffsWait_B5)
    else:
        print("No need to correct distance to {}".format(TOTAL_DIST_TO_TRAVEL))

    _angle=-45
    turnToAngle(_angle)
    # wait(anyaDropOffsWait_B5)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*2, targetAngle=_angle)
    # wait(anyaDropOffsWait)

    _angle=-90
    turnToAngle(_angle)
    # wait(anyaDropOffsWait_B5)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*7, targetAngle=_angle)
    # wait(anyaDropOffsWait)

    _angle=-45
    dropOneExpert(numDropoffRotations=1, wait=False)
    turnToAngle(_angle)
    gyroStraightWithDrive(speed=100, distanceInCm=2*CM_PER_INCH, targetAngle=_angle)
    # dropOneExpert(numDropoffRotations=1, wait=True)
    # wait(anyaDropOffsWait)
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

# waitForButtonPress()
# mainRun7()