from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *
import Utilities

_MM_PER_INCH = 25.4
_CM_PER_INCH = 2.54

(origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()

def AnyaRun():
    goStraight(_MM_PER_INCH*17, straightSpeed=1000, straightAcceleration=DEFAULT_ACCELERATION*2)# he go straight was 20 in
    driveTillHueRange(214,224,right_color)
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
    driveTillHueRange(214,224,right_color)
    # wait(5000)
    turnToAngle(targetAngle=-45, oneWheelTurn=True)
    # wait(5000)
    driveTillLine(speed=200, doCorrection=False)
    # wait(5000)
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

def resetRightArm():
    right_med_motor.run_angle(speed=-500,rotation_angle=720)

def resetLeftArm():
    wait(3000)
    left_med_motor.run_angle(speed=-1000,rotation_angle=230)


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
    turnToAngle(-90)
    # wait(10000)
    #goStraight(_MM_PER_INCH*14)
    gyroStraightWithDrive(distanceInCm=37, targetAngle=-90)
    # wait(10000)
    gyroStraightWithDrive(distanceInCm=4, targetAngle=0)
    turnToAngle(targetAngle=0,oneWheelTurn=True)
    #goStraight(_MM_PER_INCH*2)
    # gyroStraightWithDrive(distanceInCm=5, targetAngle=0)
    wait(5000)
    #goStraight(_MM_PER_INCH*-5.5)  # you might want to try 6 or 6.
    gyroStraightWithDrive(distanceInCm=14, targetAngle=0, backward=True)
    turnToAngle(75) # t

def dropOne():
    right_med_motor.run_angle(speed=500,rotation_angle=360)


def AnyaRun2():
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*20, targetAngle=0)
    turnToAngle(-45)
    # wait(3000)
    driveTillLine(speed=200, doCorrection=False)
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*1, targetAngle=-45)
    turnToAngle(targetAngle=0, oneWheelTurn=True)
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*6.5, targetAngle=0)
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*9.5, targetAngle=0, backward=True)
    turnToAngle(45)
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*10, targetAngle=45)
    left_med_motor.run_angle(speed=-1000,rotation_angle=1150)

def AnyaDropOffs():
    wait(5000)
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*4, targetAngle=45, backward=True)
    wait(2000)
    turnToAngle(targetAngle=-90)
    wait(2000)
    gyroStraightWithDrive(distanceInCm=_CM_PER_INCH*42, targetAngle=-90)
    turnToAngle(-95)
    wait(2000)
    dropOne ()
    wait(5000)
    dropOne()



print("Calling func now")
stopwatch = StopWatch()
start_time = stopwatch.time()

AnyaRun2()
AnyaDropOffs()
resetRightArm()
resetLeftArm()


end_time = stopwatch.time()
print("Time is " + str((end_time-start_time)/1000) + " seconds")
# resetArm()
print("DONE")
