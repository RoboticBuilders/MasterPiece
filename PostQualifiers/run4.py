from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

def immersiveExperianceFromBelow():
    angle = 0
    #Drive forward and stop right behind the camera in movie set
    gyroStraightWithDrive(distanceInCm=30, speed=400, targetAngle=angle)

    angle = -35
    #Turn to avoid the camera
    turnToAngle(targetAngle=angle, speed=400)
    gyroStraightWithDrive(distanceInCm=48, speed=400, targetAngle=-35)

    angle = -90
    turnToAngle(targetAngle=angle, speed=400)
    gyroStraightWithDrive(distanceInCm=35, speed=400, targetAngle=angle)
    left_med_motor.run_angle(speed=700, rotation_angle=1200)
    gyroStraightWithDrive(distanceInCm=20, speed=400, targetAngle=angle)

def lightShowTest():
    right_med_motor.run_angle(speed=1000, rotation_angle=3500)

def immersiveExperianceFromSide():
    left_med_motor.run_angle(speed=2000, rotation_angle=10000)
    left_med_motor.run_angle(speed=2000, rotation_angle=-10000)

def immersiveExperianceFromSideSlider():
    #Align it on the green part of museam, pushed against the wall
    gyroStraightWithDrive(distanceInCm=20,speed=700,targetAngle=0,backward=True)

    angle=90
    turnToAngle(targetAngle=angle, speed=700)
    gyroStraightWithDrive(distanceInCm=25,speed=400,targetAngle=angle,backward=True)

    left_med_motor.run_angle(speed=2000, rotation_angle=-2000)
    left_med_motor.run_angle(speed=2000, rotation_angle=1100)

def ThreeDCinemaUsingStaticArm():
    angle = 0
    gyroStraightWithDrive(distanceInCm = 30 , speed=400, targetAngle=angle)

def movieCameraAndRollingCameraStopper():
    left_med_motor.run_angle(speed=2000, rotation_angle=-1000)

    angle = 0
    gyroStraightWithDrive(distanceInCm = 10, speed=200, targetAngle=angle,backward=True)    
    angle = -20
    turnToAngle(targetAngle=angle, speed=400)

    left_med_motor.run_angle(speed=2000, rotation_angle=1000)

def run4():
    # ALIGNMENT: 3rd dark black line from the from the back wall
    gyroStraightWithDrive(distanceInCm = 48, speed = 500, targetAngle = 0)
    turnToAngle(targetAngle = -30, speed = 500)
    gyroStraightWithDrive(distanceInCm = 25, speed = 500, targetAngle = -30)
    turnToAngle(targetAngle = -90, speed = 500)
    gyroStraightWithDrive(distanceInCm = 40, speed = 500, targetAngle = -90)
    turnToAngle(targetAngle = -45, speed = 500)
    gyroStraightWithDrive(distanceInCm = 10, speed = 500, targetAngle = -45)

    left_med_motor.run_angle(speed=2000, rotation_angle=-3000)
    left_med_motor.run_angle(speed=2000, rotation_angle=1800)

    gyroStraight(distanceInCm = 5, speed = 500, targetAngle = -45)
    turnToAngle(targetAngle = -90, speed = 500)

    right_med_motor.run_angle(speed = 1000, rotation_angle = 1000)

    gyroStraight(distanceInCm = 15, speed = 300, targetAngle = -90)
    gyroStraight(distanceInCm = 7, speed = 50, targetAngle = -90)

    right_med_motor.run_angle(speed=1000, rotation_angle=3500)

left_med_motor.run_angle(speed=2000, rotation_angle=-3000)
left_med_motor.run_angle(speed=2000, rotation_angle=1800)
wait(5000)
right_med_motor.run_angle(speed=1000, rotation_angle=3500)
