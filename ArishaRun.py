from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *

_MM_PER_INCH = 25.4

def ArishaRun_M2():
    goStraight(600, straightSpeed=500) 
    turnToAngle(30) 
    goStraight(100) 
    turnToAngle(-45) 

    # turn back and forward
    goStraight(150)
    goStraight(-50)
    right_med_motor.run_angle(1000, -1500) 
    goStraight(50)

    #go back
    goStraight(-100)
    turnToAngle(absoluteAngle=30, turnRate=100, turnAcceleration=100) 
    goStraight(-600, straightSpeed=500)
    # turnToAngle(absoluteAngle=0, turnRate=100, turnAcceleration=100) 
    # goStraight(-300) 
    # turnToAngle(absoluteAngle=30, turnRate=100, turnAcceleration=100) 
    # goStraight(-300) 
    right_med_motor.run_angle(1000, 1500) 

def ArishaRun_M1():
    left_med_motor.run_angle(800, 100)
    goStraight(350)
    right_med_motor.run_angle(800,1000)
    left_med_motor.run_angle(800,-100)
    goStraight(-350)
    right_med_motor.run_angle(800,-1000)




def ArishaRun_M1andM2():
    left_med_motor.run_angle(300, 200)
    goStraight(300)
    #right_med_motor.run_angle(800,200)
    left_med_motor.run_angle(300,-200)
    left_med_motor.run_angle(300,200)

    goStraight(-300)
    #right_med_motor.run_angle(800,-200)
    #go to M2
    turnToAngle(30) 
    left_med_motor.run_angle(300,-200)
    goStraight(415, straightSpeed=500) 
    turnToAngle(0) 
    goStraight(250) 
    left_med_motor.run_angle(300,200)
    turnToAngle_AA(-45) 

    # turn back and forward
    goStraight(150)
    goStraight(-50)
    right_med_motor.run_angle(1000, -1300) 
    goStraight(50)

    #go back
    goStraight(-75)
    turnToAngle(absoluteAngle=0, turnRate=100, turnAcceleration=100) 
    left_med_motor.run_angle(800,-300)
    goStraight(-600, straightSpeed=500)
    right_med_motor.run_angle(1000, 1300) 



def ArishaRun_M1andM2_newgyroStr():
    #left_med_motor.run_angle(300, 200)
    gyroStraightWithDrive(27, speed=500, targetAngle=0)
    gyroStraightWithDrive(2, speed=500, backward=True, targetAngle=0)
    #right_med_motor.run_angle(800,200)
    left_med_motor.run_angle(300,-150)
    left_med_motor.run_angle(300,150)

    goStraight(-300)
    #right_med_motor.run_angle(800,-200)
    #go to M2
    # turnToAngle(30) 
    # left_med_motor.run_angle(500,-130)
    # gyroStraightWithDrive(46, speed=500, targetAngle=30) 
    # turnToAngle(0) 
    # gyroStraightWithDrive(15, speed=500, targetAngle=0) 
    # left_med_motor.run_angle(300,130)
    # gyroStraightWithDrive(10, speed=500, targetAngle=0) 

    # # goStraight(250) 
    # turnToAngle_AA(-45) 
    # gyroStraightWithDrive(15, targetAngle=-45)
    # gyroStraightWithDrive(5, backward=True, targetAngle=-45)
    # right_med_motor.run_angle(1000, -1300) 
    # gyroStraightWithDrive(5, targetAngle=-45)

    #go to M2
    turnToAngle(90) 
    left_med_motor.run_angle(500,-130)
    gyroStraightWithDrive(25, speed=500, targetAngle=90)
    turnToAngle(0)
    wait(5000)
    gyroStraightWithDrive(55, speed=500, targetAngle=0) 
    wait(5000)
    left_med_motor.run_angle(300,130)
    gyroStraightWithDrive(10, speed=500, targetAngle=0) 

    # goStraight(250) 
    turnToAngle_AA(-45) 
    gyroStraightWithDrive(15, targetAngle=-45)
    gyroStraightWithDrive(5, backward=True, targetAngle=-45)
    right_med_motor.run_angle(1000, -1300) 
    gyroStraightWithDrive(5, targetAngle=-45)

    # # turn back and forward
    # goStraight(150)
    # goStraight(-50)
    # right_med_motor.run_angle(1000, -1300) 
    # goStraight(50)

    # #go back
    # goStraight(-75)
    # turnToAngle(absoluteAngle=0, turnRate=100, turnAcceleration=100) 
    # left_med_motor.run_angle(800,-300)
    # goStraight(-600, straightSpeed=500)
    # right_med_motor.run_angle(1000, 1300) 

def staticAttachmentTest():
    # # Everything with one comment is in the orignal code!!!
    # turnToAngle(-10)
    #goStraight(15*_MM_PER_INCH)
    gyroStraightWithDrive(38, targetAngle=0)
    turnToAngle_AA(45)
    turnToAngle_AA(0)
    # goStraight(-5*MM_PER_INCH)
    gyroStraightWithDrive(30,targetAngle=0, backward=True)
    #right_med_motor.run_angle(800,-200)
    #go to M2 
    # turnToAngle(45) 
    # goStraight(415, straightSpeed=500) 
    # turnToAngle(0) 
    # goStraight(200) 
    # left_med_motor.run_angle(800,300)
    # turnToAngle(-45) 

    #go to M2
    turnToAngle_AA(90) 
    gyroStraightWithDrive(20, targetAngle=90)
    wait(3000)
    turnToAngle_AA(0) 
    wait(3000)
    gyroStraightWithDrive(61, targetAngle=0)
    wait(3000)
    # left_med_motor.run_angle(800,300)
    turnToAngle(-45) 

    # turn back and forward
    goStraight(150)
    goStraight(-50)
    right_med_motor.run_angle(1000, -1300) 
    goStraight(50)

    #go back
    # goStraight(-75)
    # turnToAngle(absoluteAngle=0, turnRate=100, turnAcceleration=100) 
    # left_med_motor.run_angle(800,-300)
    # goStraight(-600, straightSpeed=500)
    # right_med_motor.run_angle(1000, 1300) 
    #go back

    # gyroStraightWithDrive(7, targetAngle=-45, backward=True)
    goStraight(-75)
    turnToAngle_AA(0)
    #left_med_motor.run_angle(800,-300)
    goStraight(-600, straightSpeed=500)
    right_med_motor.run_angle(1000, 1300) 

def test():
    turnToAngle_AA(90)
    wait(5000)
    turnToAngle_AA(0)
    wait(5000)
    turnToAngle_AA(-45)
    wait(5000)
    turnToAngle_AA(0)
    wait(5000)
    turnToAngle_AA(-45)
    wait(5000)
    turnToAngle_AA(0)

print("Calling func now")

resetRobot()
stopwatch = StopWatch()
start_time = stopwatch.time()#time.ticks_ms()  
#ArishaRun_M2()
#ArishaRun_M1andM2()
# ArishaRun_M1andM2_newgyroStr()
staticAttachmentTest()
# test()
end_time = stopwatch.time()
#logMessage("Time for run {} time(ms): {}".format(str(run), str(time.ticks_diff(end_time, start_time))), level=0)
print(str(start_time), str(end_time))
# AnyaRun()
# robot.straight(distance=500, then=Stop.Hold, wait=True)
# left_med_motor.run_angle(-1000, 2600)
print("DONE")