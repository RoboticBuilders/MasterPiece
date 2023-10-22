from Utilities import *
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def soundmixer_sidebucketarm():
    gyroStraightWithDrive(distanceInCm = 43, speed = 500, targetAngle = 0)
    gyroStraightWithDrive(distanceInCm = 18, speed = 200, targetAngle = 0)
    #wait(1000)
    turnToAngle(targetAngle=20, speed=50)
    turnToAngle(targetAngle=100, speed=50)
    #wait(1000)

def moviesetandlever_sidebucketarm():
    gyroStraightWithDrive(distanceInCm=24, speed=100, slowDown=True)
    turnToAngle(targetAngle=45, speed=250)
    gyroStraightWithDrive(distanceInCm=9, speed=100)
    right_med_motor.run_angle(speed=400, rotation_angle=-250)
    turnToAngle(targetAngle=25, speed=400)
    gyroStraightWithDrive(distanceInCm=-3, speed=250)
    gyroStraightWithDrive(distanceInCm=10, speed=200, backward=True)
    turnToAngle(targetAngle=330, speed=250)
    right_med_motor.run_angle(speed=250, rotation_angle=250)
    gyroStraightWithDrive(distanceInCm=5, speed=200, backward=True)
    turnToAngle(targetAngle=282, speed=250)
    gyroStraightWithDrive(distanceInCm=30, speed=500, backward=True)
 
def goto_soundmixer_bigbucket():
    gyroStraightWithDrive(distanceInCm = 42, speed = 200, backward = False, targetAngle = 0, slowDown = True)

def solve_soundmixer_bigbucket():
    right_med_motor.run_angle(speed=500, rotation_angle=-1500)
    gyroStraightWithDrive(distanceInCm = 4, speed = 200, backward = False, targetAngle = 0, slowDown = True)
    #right_med_motor.run_angle(speed=500, rotation_angle=-200)
    turnToAngle(targetAngle=20, speed=30)
    turnToAngle(targetAngle=120, speed=50)

def goto_movieset_bigbucket():
    gyroStraightWithDrive(distanceInCm = 32, speed = 200, slowDown = True)
    turnToAngle(targetAngle=45, speed=50)
    gyroStraightWithDrive(distanceInCm = 7, speed = 200, slowDown = True)

def solve_movieset_bigbucket():
    right_med_motor.run_angle(speed=300, rotation_angle=1500)
    gyroStraightWithDrive(distanceInCm = 7, speed = 200, backward = True, targetAngle = 45, slowDown = True)

def run2_sidebucketarm():
    initializeAndWaitForRobotReady()
    soundmixer_sidebucketarm()
    moviesetandlever_sidebucketarm()

def run2_bigbucket():
    initializeAndWaitForRobotReady()
    goto_soundmixer_bigbucket()
    solve_soundmixer_bigbucket()
    goto_movieset_bigbucket()
    solve_movieset_bigbucket()

def run2():
    run2_bigbucket()

run2()