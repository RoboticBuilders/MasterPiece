from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from umath import *
from Utilities import *

def AroundTheWorld():
    
    resetRobot()
    
   
    angle = 20
    gyroStraightWithDriveWithAccurateDistance(distanceInCm=30,targetAngle=angle, speed=300)
    angle = 90
    turnToAngle(targetAngle=angle, speed=200)
    gyroStraightWithDriveWithAccurateDistance(distanceInCm=80, speed=300)
    angle=150
    turnToAngle(targetAngle=angle, speed=200)
    gyroStraightWithDriveWithAccurateDistance(distanceInCm=20, speed=300)

AroundTheWorld()

