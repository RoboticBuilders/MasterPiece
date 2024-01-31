from pybricks.tools import wait, StopWatch
from Utilities import *

### This is working code that we used on Jan 6th tests. 


'''
def musicConcert():
    # go forward and turn towards the black line
    angle = 0
    gyroStraightWithDriveWithAccurateDistance(distance=38, targetAngle=angle, speed=500)
    angle = -45
    turnToAngle(targetAngle = angle,speed = 300)
    
    # Now catch the black line
    gyroStraightWithDriveWithAccurateDistance(distance = 30,targetAngle = angle, speed = 300,tillBlackLine = True)
    
    # Move forward to pass the black line
    gyroStraightWithDriveWithAccurateDistance(distance=3, targetAngle=angle, speed=300)
    angle = 0
    turnToAngle(targetAngle=angle,speed=300)
    
    # Now drop off the expert
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle=angle, speed=500, stop=Stop.COAST, slowDown = False)
    gyroStraightWithDriveWithAccurateDistance(distance=6, targetAngle=angle, speed=300)
    angle = 10
    
    # Now backoff to go to music concert
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle=angle, backward=True, speed=400)
    
    angle = 50
    # Turn towards music concert
    turnToAngle(targetAngle = angle, speed = 300)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=13, targetAngle=45, speed=300)
    driveForTime(timeInMS=1000, speed=300)
    # Wait for a little and run Flippy to turn the speakers
    wait(100)

    left_med_motor.run_angle(-1000, 1500)

    wait(100)
'''



def musicConcert():
    # go forward and turn towards the black line
    gyroStraightWithDriveWithAccurateDistance(distance=43, targetAngle=0, speed=500)

    #hub.display.number(1)

    turnToAngle(targetAngle = -45, speed = 300)

    #hub.display.number(2)

    # catch the black line
    driveTillLine(speed=400, doCorrection=False, tag="Music Concert")

    #hub.display.number(3)

    # align against the wall to drop off Noah & Audience
    gyroStraightWithDriveWithAccurateDistance(distance=3, targetAngle=-45, speed=500)

    #hub.display.number(4)

    turnToAngle(targetAngle=0, speed = 300)

    #hub.display.number(5)
    
    gyroStraightWithDriveWithAccurateDistance(distance=26, targetAngle=0, speed=500, slowDown = False)

    # lift the arm to deliver the expert and back off
    gyroStraightWithDriveWithAccurateDistance(distance=26, targetAngle=10, backward=True, speed=400)

    # turn towards the Music Concert
    turnToAngle(targetAngle = 45, speed = 300)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=13, targetAngle=45, speed=300)
    driveForTime(timeInMS=1000, speed=300)

    # Wait for a little and run Flippy to turn the speakers
    wait(100)

    left_med_motor.run_angle(-1000, 1500)

    wait(100)

def augmentedReality():
    # Back up from music concert and turn towards Augmented Reality
    driveTillBlackLine(speed=300, distanceInCM=15, target_angle=45, backward=True)
    left_med_motor.run_angle(speed = 1000, rotation_angle = 1500, wait = False)
    _angle=-90
    turnToAngle(_angle)

    # go to Augmented Reality
    # gyroStraightWithDrive(distanceInCm=33, targetAngle=_angle, speed = 500)
    gyroStraightWithDriveWithAccurateDistance(distance = 33, speed = 600, targetAngle = _angle)

    _angle = -45
    turnToAngle(targetAngle=_angle,oneWheelTurn=True)

   # Now move forward to be setup to pull the augmented reality lever
    gyroStraightWithDriveWithAccurateDistance(distance=7, speed = 500, targetAngle=_angle)

    wait(120)
    # turnToAngle(targetAngle = _angle, speed = 300)
    drive_base.turn(angle = 45, wait = False)

    while not drive_base.done():
        if drive_base.stalled():
            drive_base.stop()
    gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 700, targetAngle = 0, backward = True)        
    angle = -90
    turnToAngle(targetAngle=angle,speed=300)
    gyroStraightWithDriveWithAccurateDistance(distance = 20, speed = 300, targetAngle = angle,backward = True)     

    '''
    
    drive_base.settings(500, 700, 500, 700)
    drive_base.straight(-70)

    # turn a little more and back up again to make sure the lever caught
    _angle = 30
    # turnToAngle(targetAngle=_angle,oneWheelTurn=True, speed = 700)
    wait(120)
    drive_base.turn(30)
    # gyroStraightWithDriveWithAccurateDistance(distance=13, speed = 500, targetAngle=_angle)
    drive_base.use_gyro(False)
    drive_base.straight(100)
    
    _angle = hub.imu.reset_heading(hub.imu.heading())
        
    drive_base.straight(-80)
    drive_base.use_gyro(True)
    '''

def expertDrops():
    # turn and start driving towards Sound Mixer
    _angle=-90
    turnToAngle(_angle-5)
    distGyro = gyroStraightWithDrive(distanceInCm=15*CM_PER_INCH, targetAngle=_angle, speed=500)

    # try to catch the white line near Immersive Experience
    distToWhiteLine = driveTillHsvRange(maxDistance=3*MM_PER_INCH, sensor=right_color, hueRange = range(205, 215), saturationRange=range(11, 30), valueRange=range(80, 100), tag="expert dropoffs")
    print("Distances covered so far: {}, {}".format(distGyro, distToWhiteLine))

    # distance from end of Augmented Reality to hitting Sound Mixer
    TOTAL_DIST_TO_TRAVEL = 8 * MM_PER_INCH
    
    # if robot still hasn't gone total distance to travel -> go until total distance to travel
    if(distGyro + distToWhiteLine < TOTAL_DIST_TO_TRAVEL):
        gyroStraightWithDrive(distanceInCm=(TOTAL_DIST_TO_TRAVEL - distGyro - distToWhiteLine)/10, targetAngle=_angle, speed=500)
    else:
        print("No need to correct distance to {}".format(TOTAL_DIST_TO_TRAVEL))
    # Now updated to negative for the new attachment
    right_med_motor.run_angle(speed = -600, rotation_angle = -1500, then = Stop.COAST, wait = False)

    gyroStraightWithDriveWithAccurateDistance(distance = 18, speed = 500, targetAngle = _angle)

    _angle = -45
    turnToAngle(targetAngle = _angle, speed = 300)

    gyroStraightWithDriveWithAccurateDistance(distance = 5.5, speed = 200, targetAngle = _angle)

def run7():
    resetRobot()
    musicConcert()
    augmentedReality()
    #expertDrops()

def mainRun7():
    initializeAndWaitForRobotReady()

    print("BATTERY = " + str(hub.battery.voltage()))
    stopwatch = StopWatch()
    start_time = stopwatch.time()

    run7()

    end_time = stopwatch.time()
    print("Time is " + str((end_time-start_time)/1000) + " seconds")

    print("DONE")

waitForButtonPress()
mainRun7()
#drive_base.curve(radius=-120,angle = 90)