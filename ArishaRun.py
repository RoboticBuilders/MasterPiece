from Utilities import _MM_PER_INCH
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *
import Utilities

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

#Latest version with pick up Noah the expert
def staticAttachmentTest2_pickupNoah():
 
    #gyroStraightWithDrive(38, targetAngle=0)
    goStraight(15 * _MM_PER_INCH)
    turnToAngle(50, speed=500)
    turnToAngle_AA(0)
    goStraight(-6* _MM_PER_INCH )
    
    
    
    #go to M2
    wait(10000)
    turnToAngle_AA(90) 
    goStraight(260)
    turnToAngle_AA(0) 
    wait(10000)

    #wait(3000)
    #goStraight(24*_MM_PER_INCH)
    goStraight(17*_MM_PER_INCH)
    #wait(3000)
    #driveTillLine(speed=200, distanceInCM=70, target_angle=0, doCorrection=False)
    #wait(3000)
    wait(10000)
    turnToAngle_AA(-45) 
    wait(10000)
    # turn back and forward
    goStraight(150)
    wait(3000)
    goStraight(-60)
    wait(3000)
    right_med_motor.run_angle(1000, -1300) 
    #goStraight(50)

    # goback and pick up another expert
    goStraight(-65)
    turnToAngle_AA(45)
    wait(3000)
    goStraight(3 * _MM_PER_INCH)
    wait(3000)
    turnToAngle_AA(90)
    wait(3000)
    goStraight(350)
    #turnToAngle(-170, forceTurn=FORCETURN_RIGHT)
    turnToAngle_AA(-170)
    goStraight(300)
    turnToAngle(-140)
    goStraight(500)

    # #go back
    # # goStraight(-75)
    # # turnToAngle(absoluteAngle=0, turnRate=100, turnAcceleration=100) 
    # # left_med_motor.run_angle(800,-300)
    # # goStraight(-600, straightSpeed=500)
    # # right_med_motor.run_angle(1000, 1300) 
    # #go back

    # # gyroStraightWithDrive(7, targetAngle=-45, backward=True)
    # goStraight(-75)
    # turnToAngle_AA(0)
    # #left_med_motor.run_angle(800,-300)
    # goStraight(-600, straightSpeed=500)
    # right_med_motor.run_angle(1000, 1300) 

#Testing drive till line
def MissionM1_M2_pickupNoah():  ## Arisha Run must use

    #3D Cinema
    left_med_motor.run_angle(500, 150, wait=False)
    #was 14 inches now 10
    gyroStraightWithDrive(9 * Utilities._CM_PER_INCH, targetAngle=0, speed=300)
    # wait(3000)
    left_med_motor.run_angle(500, -150)
    left_med_motor.run_angle(500, 150)
    #goStraight(-5)
    #gyroStraightWithDrive(-5* Utilities._CM_PER_INCH, targetAngle=0)
    gyroStraightWithDrive(distanceInCm=-13, targetAngle=0, speed=500)
    # wait(3000)
    
    
    #go to M2
    turnToAngle(90) 
    #goStraight(218) #218mm
    left_med_motor.run_angle(500, -150, wait=False)
    gyroStraightWithDrive(distanceInCm=19, targetAngle=90)
    #driveTillHsvRange(214, 230, left_color)
    driveTillHsvRange(maxDistance=3*_MM_PER_INCH, sensor=left_color, hueRange = range(214, 230) )
    
    # wait(5000)
    # driveTillColor(Color.BLUE)
    turnToAngle(0) 
    # wait(5000)
    #left_med_motor.run_angle(500, -150, wait=False)
    #if the driveTillLine fails can use goStraight 17
    # goStraight(17*_MM_PER_INCH)
    gyroStraightWithDrive(7*Utilities._CM_PER_INCH, targetAngle=0)
    left_med_motor.run_angle(500, 150, wait=False)
    gyroStraightWithDrive(7*Utilities._CM_PER_INCH, targetAngle=0)
    # wait(5000)

    driveTillLine(speed=200, doCorrection=False, sensor=left_color, blackOrWhite="Black")
    #driveTillBlackLine(speed=200,distanceInCM=100, target_angle=0)
    # wait(5000)
    turnToAngle(-45) 
    # wait(10000)
    gyroStraightWithDrive(distanceInCm=15, targetAngle=-45)
    wait(3000)
    goStraight(-50)
    wait(3000)
    #gyroStraightWithDrive(distanceInCm=5, targetAngle=-45, backward=True) ##   !@%^&*#@#$%^&^%$#$^&^@@#$%$
    #wait(3000)
    #gyroStraightWithDrive(distanceInCm=6, speed=50, targetAngle=-45, backward=True)
    #goStraight(-60)
    #wait(3000)
    #right_med_motor.run_angle(1000, -1300) 

    right_med_motor.run_angle(800, 300) 

    #pick up noah
    gyroStraightWithDrive(-65/10, targetAngle=-45, speed=500)
    turnToAngle(45)
    gyroStraightWithDrive(3 * Utilities._CM_PER_INCH, targetAngle=45, speed=500)
    turnToAngle(90)
    left_med_motor.run_angle(500, -150, wait=False)
    #was 18 with increase in speed brought down to 10

    gyroStraightWithDrive(28, targetAngle=90,speed=500)
    turnToAngle(175, forceTurn=FORCETURN_RIGHT)
    gyroStraightWithDrive(25, targetAngle=175,speed=500)
    turnToAngle(-130)
    gyroStraightWithDrive(40, targetAngle=-130, speed=1000)## was go forward 50 not 40
    # turnToAngle(-100)## was not there before remove if does not work
    # gyroStraightWithDrive(35, targetAngle=-100)## was not there before remove if does not work


print("Calling func now")

resetRobot()
stopwatch = StopWatch()
start_time = stopwatch.time()#time.ticks_ms()  
#ArishaRun_M2()
#ArishaRun_M1andM2()
# ArishaRun_M1andM2_newgyroStr()
#staticAttachmentTest()
# staticAttachmentTest2()
# staticAttachmentTestDriveTillLine()
# resetGyro(angle=90)
# driveTillColor(Color.BLUE)
#driveTillLine(speed=150, doCorrection=False, sensor=left_color, blackOrWhite="Black")
# MissionM1_M2_pickupNoah()
# right_med_motor.run_angle(speed=1000, rotation_angle=-300) 
# gyroStraightWithDrive2(distanceInCm=15, targetAngle=0)
# wait(1000)
# gyroStraightWithDrive2(distanceInCm=15, targetAngle=0)
# goStraight(distance=-50)
# print("Second call now ----------------------------")
# wait(1500)
# gyroStraightWithDrive(distanceInCm=-5, targetAngle=0)
#gyroStraightWithDrive(30, speed=300, targetAngle=0)
#testHsv()
#driveTillHueRange(214, 230, left_color)
# turnToAngle(-90)
# goStraight(240)
# wait(5000)
#driveTillLine(speed=150, doCorrection=False, sensor=right_color, blackOrWhite="White")
#driveTillBlackLine(speed=200,distanceInCM=100, target_angle=0)
#testHsv()
# testColor()
#bigger gear
# right_med_motor.run_angle(1000, -300) 
# end_time = stopwatch.time()
# right_med_motor.run_angle(1000, 1300) 
# right_med_motor.run_angle(1000, -1300) 
#small gears
# right_med_motor.run_angle(1000, 300) 
# end_time = stopwatch.time()
# right_med_motor.run_angle(1000, -300) 
# right_med_motor.run_angle(1000, 300) 
#logMessage("Time for run {} time(ms): {}".format(str(run), str(time.ticks_diff(end_time, start_time))), level=0)
MissionM1_M2_pickupNoah()
end_time = stopwatch.time()
print(str(start_time), str(end_time))

# AnyaRun()
# robot.straight(distance=500, then=Stop.Hold, wait=True)


print("DONE")

