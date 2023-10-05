from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

_MM_PER_INCH = 25.4
_CM_PER_INCH = 2.54

(origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()

def AnyaRun():
    goStraight(_MM_PER_INCH*17, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)# he go straight was 20 in
    driveTillHsvRange(214,224,right_color)
    wait(5000)
    turnToAngle(targetAngle=-45, oneWheelTurn=False)
    wait(5000)
    driveTillLine(speed=200, doCorrection=False)
    wait(5000)
    turnToAngle(targetAngle=0,oneWheelTurn=True)
    wait(5000)
    goStraight(_MM_PER_INCH*10, straightSpeed=500, straightAcceleration=DEFAULT_ACCELERATION*2)
    wait(5000)
    #goStraight(_MM_PER_INCH*-7, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    goStraight(_MM_PER_INCH*-10, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    wait(5000)
    turnToAngle(45)
    wait(5000)
    goStraight(_MM_PER_INCH*10, straightSpeed=800, straightAcceleration=DEFAULT_ACCELERATION*2)
    wait(5000)
    left_med_motor.run_angle(speed=-1000,rotation_angle=900)
    ArishaAugmentedRealityTest()




def AnyaRun_gyroStraight():
    #goStraight(_MM_PER_INCH*17, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)# he go straight was 20 in
    gyroStraightWithDrive(distanceInCm=43, targetAngle=0)
    driveTillHsvRange(range(214,224),right_color)
    # wait(5000)
    turnToAngle(targetAngle=-45, oneWheelTurn=True)
    wait(5000)
    driveTillLine(speed=200, doCorrection=False)
    wait(5000)
    gyroStraightWithDrive(distanceInCm=3, targetAngle=-45)
    # wait(5000)
    turnToAngle(targetAngle=0,oneWheelTurn=True)
    # wait(5000)
    #goStraight(_MM_PER_INCH*10, straightSpeed=500, straightAcceleration=DEFAULT_ACCELERATION*2)
    gyroStraightWithDrive(distanceInCm=25, targetAngle=0, slowDistanceMultipler=0.3)
    # wait(5000)
    #goStraight(_MM_PER_INCH*-7, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    #goStraight(_MM_PER_INCH*-10, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    gyroStraightWithDrive(distanceInCm=24, targetAngle=0, backward=True)
    # wait(5000)
    turnToAngle(45)
    wait(5000)
    #goStraight(_MM_PER_INCH*10, straightSpeed=800, straightAcceleration=DEFAULT_ACCELERATION*2)
    gyroStraightWithDrive(distanceInCm=25, targetAngle=45 )
    wait(5000)
    left_med_motor.run_angle(speed=-1000,rotation_angle=1150)
    ArishaAugmentedRealityTest_GyroStraight()

def resetCircularMotionArm():
    left_med_motor.run_angle(speed=1000,rotation_angle=230)


def ArishaAugmentedRealityTest():
    # resetGyro(angle=45)
    goStraight(_MM_PER_INCH*-4.5, straightSpeed=300)# was 5.5 back (-5.5)
    turnToAngle_AA(-90)
    # wait(10000)
    goStraight(_MM_PER_INCH*14)
    # wait(10000)
    turnToAngle(targetAngle=0,oneWheelTurn=True)
    goStraight(_MM_PER_INCH*2)
    wait(5000)
    goStraight(_MM_PER_INCH*-5.5)  # you might want to try 6 or 6.5
    turnToAngle(75) # take out if does not work added by arisha's brain
    # wait(10000)
    # turnToAngle(targetAngle=70, oneWheelTurn=True)
    # wait(10000)
    # goStraight(_MM_PER_INCH*-2)
    # wait(10000)
    # turnToAngle_AA(absoluteAngle=90)
    # wait(10000)
    # # goStraight(_MM_PER_INCH*-2)
    # # wait(5000)
    # # turnToAngle_AA(absoluteAngle=80)
    # # wait(5000)
    # goStraight(_MM_PER_INCH*10)
    # # goStraight(_MM_PER_INCH*-15)
    # wait(5000)

def ArishaAugmentedRealityTest_GyroStraight():
    # resetGyro(angle=45)
    goStraight(_MM_PER_INCH*-4.5, straightSpeed=300)# was 5.5 back (-5.5)
    _angle=-90
    turnToAngle(_angle)
    wait(10000)
    
    #gyroStraightWithDrive(distanceInCm=37, targetAngle=-90)
    gyroStraightWithDrive(distanceInCm=30, targetAngle=_angle)
    wait(15000)
    driveTillHsvRange(maxDistance=2*_MM_PER_INCH, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100) )
    wait(5000)
    # wait(10000)
    # gyroStraightWithDrive(distanceInCm=4, targetAngle=-90)
    _angle = -45
    turnToAngle(targetAngle=_angle,oneWheelTurn=True) ## was target angle ((0))
    gyroStraightWithDrive(distanceInCm=3, targetAngle=_angle) # I might need to delete test line!!!!!
    _angle = 25
    turnToAngle(targetAngle=_angle,oneWheelTurn=True) ## was target angle ((0))  # add on line take off if not work
    # gyroStraightWithDrive(distanceInCm=3, targetAngle=0) # I might need to delete also test line!!!!!
    #goStraight(_MM_PER_INCH*2)
    # gyroStraightWithDrive(distanceInCm=5, targetAngle=0)
    # wait(5000)
    #goStraight(_MM_PER_INCH*-5.5)  # you might want to try 6 or 6.
    gyroStraightWithDrive(distanceInCm=8, targetAngle=_angle, backward=True)
    wait(10000)

EXPERT_ARM_TURN_ANGLE = 350
DROP_OFF_SPEED = 500
def dropOneExpert():
    right_med_motor.run_angle(speed=DROP_OFF_SPEED,rotation_angle=EXPERT_ARM_TURN_ANGLE)

def resetExpertDropOffArm(numRotations=2):
    if(numRotations>0):
        right_med_motor.run_angle(speed=-DROP_OFF_SPEED,rotation_angle=numRotations*EXPERT_ARM_TURN_ANGLE)

anyaRun2Wait = 0
def AnyaRun2():
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*16.5, targetAngle=0, speed=400)
    turnToAngle(-45)
    # wait(anyaRun2Wait)
    driveTillLine(speed=200, doCorrection=False)
    # wait(anyaRun2Wait)
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*1, targetAngle=-45, speed=400)
    turnToAngle(targetAngle=0, oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*6.5, targetAngle=0)
    # gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*6.5, targetAngle=0, speed=400)
    # lift the arm to deliver the expert
    left_med_motor.run_angle(speed=-1000,rotation_angle=100)    
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*8, targetAngle=0, backward=True, speed=400)
    # goStraight(distance=_MM_PER_INCH*9.5, backward=True, wait=False)
    # wait(anyaRun2Wait)
    # left_med_motor.run_angle(speed=-3000,rotation_angle=150)
    turnToAngle(45)
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*10, targetAngle=45, speed=400)
    turnToAngle(targetAngle=53, forceTurn=FORCETURN_RIGHT, oneWheelTurn=True)
    wait(anyaRun2Wait)
    left_med_motor.run_angle(speed=1000,rotation_angle=600)

anyaDropOffsWait = 0
def AnyaDropOffs(numDropoffs=2):
    #Get to starting position - only for testing!!!
    # gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*8, targetAngle=0, backward=True)
    # turnToAngle(45)
    # gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*10, targetAngle=45)


    # gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*4.5, targetAngle=45, backward=True)# was 5.5 back (-5.5)
    # turnToAngle(-90)
    # wait(3000)
    # left_med_motor.run_angle(speed=-3000,rotation_angle=550)

    # gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*19, targetAngle=-90)
    resetCircularMotionArm()
    gyroStraightWithDrive(distanceInCm=1)
    turnToAngle(-90)
    wait(anyaDropOffsWait)
    distGyro = gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*6, targetAngle=-90)
    wait(anyaDropOffsWait)
    distToWhiteLine = driveTillHsvRange(maxDistance=17*_MM_PER_INCH, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100) )
    print("Distances covered so far: {}, {}".format(distGyro, distToWhiteLine))
    wait(anyaDropOffsWait)
    if(distGyro + distToWhiteLine < 30*_MM_PER_INCH):
        # driveTillLine(speed=200, sensor=left_color, maxDistance=12*_MM_PER_INCH)
        gyroStraightWithDrive(distanceInCm=(_MM_PER_INCH*29 - distGyro - distToWhiteLine)/10, targetAngle=-90)
        wait(anyaDropOffsWait)

    if(numDropoffs>0):
        wait(anyaDropOffsWait)
        # turnToAngle(targetAngle=-110)
        dropOneExpert()
        turnToAngle(-75)
        gyroStraightWithDrive(distanceInCm=-2*_CM_PER_INCH, targetAngle=-75)
        turnToAngle(-90, oneWheelTurn=True, forceTurn=FORCETURN_RIGHT)

    if(numDropoffs>1):
        # gyroStraightWithDrive(distanceInCm=5*_CM_PER_INCH, targetAngle=-90)
        # turnToAngle(225)
        # wait(anyaDropOffsWait)
        # # driveTillLine(speed=200, sensor=right_color, maxDistance=5*_MM_PER_INCH)
        # gyroStraightWithDrive(distanceInCm=3*_CM_PER_INCH, targetAngle=-135)
        # wait(anyaDropOffsWait)
        # turnToAngle(180, oneWheelTurn=True, forceTurn=FORCETURN_LEFT)
        # wait(anyaDropOffsWait)
        # gyroStraightWithDrive(distanceInCm=7*_CM_PER_INCH, targetAngle=-180)
        # wait(anyaDropOffsWait)
        # dropOneExpert()
        # try2
        wait(3000)
        gyroStraightWithDrive(distanceInCm=3*_CM_PER_INCH, targetAngle=-90)
        turnToAngle(177, oneWheelTurn=True, forceTurn=FORCETURN_LEFT)
        wait(3000)
        gyroStraightWithDrive(distanceInCm=5*_CM_PER_INCH, targetAngle=177)
        turnToAngle(targetAngle=170)
        wait(3000)
        dropOneExpert()



print("Calling func now")
stopwatch = StopWatch()
start_time = stopwatch.time()

AnyaRun2()
ArishaAugmentedRealityTest_GyroStraight()

# # Set dropoffs to 0, 1, or 2
dropoffs=2
AnyaDropOffs(numDropoffs=dropoffs)

# dropOneExpert()
# dropOneExpert()

# driveTillHsvRange(sensor=right_color, hueRange = range(205, 215), saturationRange=range(19, 30), valueRange=range(85, 100) )
# testHsv(sensor=right_color)
# gyroStraightWithDrive(distanceInCm=23, targetAngle=0)
# driveTillHueRange(hueRange=range(0,1), saturationRange=range(0,1), valueRange=range(99,101))

# testHsv()

end_time = stopwatch.time()
print("Time is " + str((end_time-start_time)/1000) + " seconds")
gyroStraightWithDrive(distanceInCm=15)
resetExpertDropOffArm(numRotations=dropoffs)
# resetArm()
print("DONE")
