from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *


def testDriveForTime():
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle=0, speed=500)
    drive_base.use_gyro(False)
    driveForTime(timeInMS = 500, stopAtEnd = True, speed = 300, turnRate = 0)
    wait(2000)

def testMedMotors():
    left_med_motor.run(1000)
    right_med_motor.run(1000)

    wait(10 * 1000)

    print(left_med_motor.angle())
    print(right_med_motor.angle())

def testStallDetect():
    stall_detect.avg_load(max_load_change = 1, minValidLoad = 30, minObservationsRequired = 15, min_dist = 300, debug = True)

def testParallelCode():
    right_med_motor.run_angle(speed=2000, rotation_angle = -800, wait = False)
   
    # Drive towards the scene change, catch the line.
    angle = 0
    gyroStraightWithDriveWithAccurateDistance(distance=50, speed=500, targetAngle=angle,
                                              backward=False)

testParallelCode()