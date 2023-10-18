from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

resetGyro(0)
turnToAngle(-30, speed=200, oneWheelTurn=True)
resetGyro(0)

wait(2000)


gyroStraightWithDrive(48)
wait(2000)

turnToAngle(-45, speed=200, oneWheelTurn=True)
resetGyro(0)
wait(2000)

gyroStraightWithDrive(38)
wait(2000)

turnToAngle(25, speed=200)
wait(2000)

gyroStraightWithDrive(15)
wait(2000)

turnToAngle(-30, speed=200, oneWheelTurn=True)
resetGyro(0)
wait(2000)


gyroStraightWithDrive(-27)
wait(2000)

left_med_motor.run_angle(300, 360 * 4)
wait(5000)

left_med_motor.run_angle(300, -360 * 4)
wait(1000)

gyroStraightWithDrive(7)
wait(2000)

turnToAngle(-90, speed=200)
wait(2000)

gyroStraightWithDrive(20)
wait(2000)
resetGyro(0)

turnToAngle(90, speed=200)
wait(2000)

gyroStraightWithDrive(23)

gyroStraightWithDrive(-50)
resetGyro(0)

turnToAngle(115, speed=200)
resetGyro(0)

gyroStraightWithDrive(110)


#turnToAngle(-43.5, speed=200, turn_acceleration=400)
#resetGyro(0)

#gyroStraightWithDrive(43.55)
#wait(2000)

#turnToAngle(69, speed=200, turn_acceleration=400)
#resetGyro(0)

#gyroStraightWithDrive(18)

#turnToAngle(-92, speed=100)

#resetGyro(0)

#gyroStraightWithDrive(17.5)