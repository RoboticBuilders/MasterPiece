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
    goStraight(_MM_PER_INCH*20, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    # wait(5000)
    turnToAngle(-45)
    # wait(5000)
    driveTillLine(speed=200, distanceInCM=200, target_angle=-45, doCorrection=False)
    # wait(5000)
    # goStraight(MM_PER_INCH*0.5)
    # wait(5000)
    turnToAngle(targetAngle=0,oneWheelTurn=True)
    # wait(5000)
    goStraight(_MM_PER_INCH*10, straightSpeed=800, straightAcceleration=DEFAULT_ACCELERATION*2)
    # wait(5000)
    goStraight(_MM_PER_INCH*-9, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    # wait(5000)
    turnToAngle(45)
    # wait(5000)
    goStraight(_MM_PER_INCH*10, straightSpeed=800, straightAcceleration=DEFAULT_ACCELERATION*2)
    # wait(5000)
    left_med_motor.run_angle(speed=-1000,rotation_angle=900)
    # wait(5000)
    goStraight(_MM_PER_INCH*-8, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    # wait(5000)
    turnToAngle(-30)
    # wait(5000)
    # robot.settings(1000, DEFAULT_ACCELERATION*2, origTurnSpeed, origTurnAccel)
    goStraight(_MM_PER_INCH*-25, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    # robot.settings(origSpeed, origAccel, origTurnSpeed, origTurnAccel)

def augmentedReality():
    left_med_motor.run_angle(speed=1000, rotation_angle=50)

def resetArm():
    wait(3000)
    left_med_motor.run_angle(speed=-1000,rotation_angle=150)


def ArishaAugmentedRealityTest():
    resetGyro(angle=45)
    goStraight(_MM_PER_INCH*-5.5, straightSpeed=300)
    turnToAngle_AA(-90)
    # wait(10000)
    goStraight(_MM_PER_INCH*14)
    # wait(10000)
    turnToAngle(targetAngle=0,oneWheelTurn=True)
    # wait(10000)
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

def dropOne():
    right_med_motor.run_angle(speed=-1000,rotation_angle=400)


print("Calling func now")
stopwatch = StopWatch()
start_time = stopwatch.time()
# AnyaRun()
# ArishaAugmentedRealityTest()

# dropOne()
# wait(15000)
# dropOne()
ArishaAugmentedRealityTest()
# right_med_motor.run_angle(speed=1000,rotation_angle=500)
# wait(3000)
# gyroStraightWithDrive(_CM_PER_INCH*5)
# gyroStraightWithDrive(_CM_PER_INCH*-5)
# dropOne()
# gyroStraightWithDrive(_CM_PER_INCH*5)

end_time = stopwatch.time()
print("Time is " + str((end_time-start_time)/1000) + " seconds")
# resetArm()
print("DONE")
