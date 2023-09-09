from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

_MM_PER_INCH = 25.4

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
    turnToAngle(absoluteAngle=0,oneWheelTurn=True)
    # wait(5000)
    goStraight(MM_PER_INCH*10, straightSpeed=800, straightAcceleration=DEFAULT_ACCELERATION*2)
    # wait(5000)
    goStraight(MM_PER_INCH*-9, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    # wait(5000)
    turnToAngle(45)
    # wait(5000)
    goStraight(MM_PER_INCH*10, straightSpeed=800, straightAcceleration=DEFAULT_ACCELERATION*2)
    # wait(5000)
    left_med_motor.run_angle(speed=-1400,rotation_angle=900)
    # wait(5000)
    goStraight(_MM_PER_INCH*-8, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    # wait(5000)
    turnToAngle(-30)
    # wait(5000)
    # robot.settings(1000, DEFAULT_ACCELERATION*2, origTurnSpeed, origTurnAccel)
    goStraight(_MM_PER_INCH*-25, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)
    # robot.settings(origSpeed, origAccel, origTurnSpeed, origTurnAccel)

def resetArm():
    wait(3000)
    left_med_motor.run_angle(speed=-1000,rotation_angle=150)



print("Calling func now")
stopwatch = StopWatch()
start_time = stopwatch.time()
AnyaRun()
end_time = stopwatch.time()
print("Time is " + str((end_time-start_time)/1000) + " seconds")
resetArm()
print("DONE")