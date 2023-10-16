from Utilities import *
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def soundmixer():
    gyroStraightWithDrive(distance = 50, speed = 200, backward = False, targetAngle = 0, slowDown = True)
    wait(1000)
    turnToAngle(targetAngle=20, speed=30)
    turnToAngle(targetAngle=100, speed=50)
    wait(1000)

def moviesetandlever():
    gyroStraightWithDrive(distance=24, speed=200, slowDown=True)
    wait(1000)
    turnToAngle(targetAngle=42)
    wait(1000)
    gyroStraightWithDrive(distance=5, speed=100, slowDown=True)
    wait(1000)
    right_med_motor.run_angle(speed=500, rotation_angle=-250)
    wait(1000)
    turnToAngle(targetAngle=35, speed=50)
    wait(1000)
    gyroStraightWithDrive(distance=-15, speed=50, slowDown=True)
    wait(1000)
    turnToAngle(targetAngle=-30, speed=30)
 
def run2():
    initializeAndWaitForRobotReady()
    soundmixer()
    moviesetandlever()

run2()





