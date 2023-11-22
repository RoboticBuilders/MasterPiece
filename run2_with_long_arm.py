from Utilities import *
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run2_A():
    # bring down the main arm
    right_med_motor.run_angle(speed=1000, rotation_angle = 2300)

    # Backoff a little befote turning to put the movie camera in the 
    # right place.
    wait(50)
    gyroStraightWithDrive(distanceInCm=10, speed=600, backward=True, targetAngle=0)
    turnToAngle(targetAngle=340, speed=500)

    # Pickup the arm slightly.
    right_med_motor.run_angle(speed=1000, rotation_angle = -500)

    # Backoff and gohome
    right_med_motor.run_angle(speed=1000, rotation_angle = -1000, wait=False)
    turnToAngle(targetAngle=10, speed=500)
    gyroStraightWithDrive(targetAngle=10, distanceInCm=25, speed=1000, backward=True)

def run2():
    resetGyro(0)
    run2_A()
