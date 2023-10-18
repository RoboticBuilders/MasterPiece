from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

resetGyro(0)


turnToAngle(330, speed=200, oneWheelTurn=True)

gyroStraightWithDrive(distanceInCm = 48, speed = 300, targetAngle = 330)

turnToAngle(305, speed=200, oneWheelTurn=True)
wait(500)

gyroStraightWithDrive(distanceInCm=55, speed=300, targetAngle=305)

turnToAngle(270, speed=200, oneWheelTurn=True)
wait(500)

gyroStraightWithDrive(distanceInCm=21, speed=200, targetAngle=270, backward=True)

wait(1000)

left_med_motor.run_angle(300, 360 * 3)
left_med_motor.run_angle(600, 360 * 4)

left_med_motor.run_angle(300, -360 * 4)


gyroStraightWithDrive(distanceInCm=7, speed=300, targetAngle=270)

turnToAngle(180, speed=200)

gyroStraightWithDrive(distanceInCm=20, speed=300, targetAngle=180)


turnToAngle(270, speed=200)

gyroStraightWithDrive(distanceInCm=23, speed=300, targetAngle=270)

gyroStraightWithDrive(distanceInCm=50, speed=300, targetAngle=270, backward=True)

turnToAngle(15, speed=200)

gyroStraightWithDrive(distanceInCm=110, speed=341, targetAngle=15)