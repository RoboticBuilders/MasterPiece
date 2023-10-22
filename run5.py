from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

(origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
CIRCULAR_MOTION_ARM_DEGREES=450
CIRCULAR_MOTION_ARM_SPEED=1000
augmentedRealityWaitTime=0
EXPERT_ARM_TURN_ANGLE = 140
DROP_OFF_SPEED = 400
EXPERT_ARM_CONTROL = right_med_motor
anyaRun2Wait = 0
anyaDropOffsWait_B5 = 0
anyaDropOffsWait = 0

def resetCircularMotionArm(wait=True):
    left_med_motor.run_angle(speed=CIRCULAR_MOTION_ARM_SPEED,rotation_angle=-1*CIRCULAR_MOTION_ARM_DEGREES, wait=wait)

def doMusicConcert():
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*17, targetAngle=0, speed=600)
    turnToAngle(-45)
    # wait(anyaRun2Wait)
    driveTillLine(speed=300, doCorrection=False)
    # wait(anyaRun2Wait)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*1, targetAngle=-45, speed=600)
    turnToAngle(targetAngle=0, oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*6.5, targetAngle=0, speed=500)
    # lift the arm to deliver the expert
    left_med_motor.run_angle(speed=CIRCULAR_MOTION_ARM_SPEED,rotation_angle=-100)    
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*8, targetAngle=10, backward=True, speed=400)
    turnToAngle(45)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*10, targetAngle=45, speed=400)
    turnToAngle(targetAngle=53, forceTurn=FORCETURN_RIGHT, oneWheelTurn=True)
    wait(anyaRun2Wait)
    left_med_motor.run_angle(speed=CIRCULAR_MOTION_ARM_SPEED,rotation_angle=CIRCULAR_MOTION_ARM_DEGREES)

def doAugmentedReality():
    # resetGyro(angle=45)
    # Back up from music concert
    goStraight(MM_PER_INCH*-5, straightSpeed=300)# was 5.5 back (-5.5)
    _angle=-90
    #wait(10000)
    turnToAngle(_angle)
    resetCircularMotionArm(wait=False)

    #wait(10000)
    #37 to ensure that the masterpiece mission doesnt come in the way
    gyroStraightWithDrive(distanceInCm=35, targetAngle=-90) #----Changed
    # gyroStraightWithDrive(distanceInCm=30, targetAngle=_angle)
    wait(augmentedRealityWaitTime)
    _angle = -45
    turnToAngle(targetAngle=_angle,oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=3, targetAngle=_angle)
    # _angle = 25
    _angle = 25
    turnToAngle(targetAngle=_angle,oneWheelTurn=True) ## was target angle ((0))  # add on line take off if not work
    # gyroStraightWithDrive(distanceInCm=3, targetAngle=0) # I might need to delete also test line!!!!!
    #goStraight(MM_PER_INCH*2)
    # gyroStraightWithDrive(distanceInCm=5, targetAngle=0)
    # wait(5000)
    #goStraight(MM_PER_INCH*-5.5)  # you might want to try 6 or 6.
    gyroStraightWithDrive(distanceInCm=12, targetAngle=_angle, backward=True)
    wait(augmentedRealityWaitTime)
    _angle = 35
    turnToAngle(targetAngle=_angle,oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=12, targetAngle=_angle)
    _angle=30
    turnToAngle(targetAngle=_angle,oneWheelTurn=True, forceTurn=FORCETURN_LEFT)
    gyroStraightWithDrive(distanceInCm=12, targetAngle=_angle, backward=True)

def dropOneExpert(numDropoffRotations=1, wait=True):
    right_med_motor.run_angle(speed=DROP_OFF_SPEED,rotation_angle=numDropoffRotations*EXPERT_ARM_TURN_ANGLE, wait=wait)

def resetExpertDropOffArm(numRotations=2):
    if(numRotations>0):
        right_med_motor.run_angle(speed=-DROP_OFF_SPEED,rotation_angle=numRotations*EXPERT_ARM_TURN_ANGLE)

def ballerina5_ExpertDropOffs():
    gyroStraightWithDrive(distanceInCm=1)
    _angle=-90
    turnToAngle(_angle)
    wait(anyaDropOffsWait_B5)
    #was 6 followed by 12 for driveTillLine
    distGyro = gyroStraightWithDrive(distanceInCm=15*CM_PER_INCH, targetAngle=_angle, speed=500)
    wait(anyaDropOffsWait_B5)
    distToWhiteLine = driveTillHsvRange(maxDistance=3*MM_PER_INCH, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100) )
    print("Distances covered so far: {}, {}".format(distGyro, distToWhiteLine))
    wait(anyaDropOffsWait_B5)
    TOTAL_DIST_TO_TRAVEL = 21*MM_PER_INCH # was 17
    if(distGyro + distToWhiteLine < TOTAL_DIST_TO_TRAVEL):
        # driveTillLine(speed=200, sensor=left_color, maxDistance=12*MM_PER_INCH)
        gyroStraightWithDrive(distanceInCm=(TOTAL_DIST_TO_TRAVEL - distGyro - distToWhiteLine)/10, targetAngle=_angle, speed=500)
        wait(anyaDropOffsWait_B5)
    else:
        print("No need to correct distance to {}".format(TOTAL_DIST_TO_TRAVEL))

    _angle=-45
    turnToAngle(_angle)
    wait(anyaDropOffsWait_B5)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*2, targetAngle=_angle)
    wait(anyaDropOffsWait)
    _angle=-90
    turnToAngle(_angle)
    wait(anyaDropOffsWait_B5)
    gyroStraightWithDrive(distanceInCm=CM_PER_INCH*7, targetAngle=_angle)
    wait(anyaDropOffsWait)
    # wait(10000)
    # turnToAngle(-75)
    # gyroStraightWithDrive(distanceInCm=-2*CM_PER_INCH, targetAngle=-75)
    # turnToAngle(-90, oneWheelTurn=True, forceTurn=FORCETURN_RIGHT)

    #New strategy
    # gyroStraightWithDrive(distanceInCm=5*CM_PER_INCH, targetAngle=-90)
    _angle=-45
    turnToAngle(_angle)
    dropOneExpert(numDropoffRotations=2, wait=False)
    gyroStraightWithDrive(speed=100, distanceInCm=2*CM_PER_INCH, targetAngle=_angle)
    wait(anyaDropOffsWait)
    while(not EXPERT_ARM_CONTROL.done()):
        wait(10)

def run5():
    doMusicConcert()
    doAugmentedReality()
    ballerina5_ExpertDropOffs()

def mainRun5():
    print("Calling func now")
    initializeAndWaitForRobotReady()

    print("BATTERY = " + str(hub.battery.voltage()))
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    doMusicConcert()
    # resetGyro(45)
    doAugmentedReality()

    # Set dropoffs to 0, 1, or 2
    dropoffs=2
    ballerina5_ExpertDropOffs()

    # dropOneExpert(numDropoffRotations=2, wait=True)

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    # Reset dropoff arm
    wait(5000)
    resetExpertDropOffArm()

    print("DONE")

# mainRun5()