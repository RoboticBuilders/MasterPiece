from pybricks.tools import wait, StopWatch
from Utilities import *

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

def musicconcertnew():
    angle = -20
    # First go forward at an angle to catch the black spur line in front
    # of the music concernt.
    if (gyroStraightWithDriveWithAccurateDistance(distance=70, targetAngle = angle, speed=1000, 
                                    tillBlackLine = True,
                                    color_sensor = right_color) == False):
        print("Run7: musicconcertnew: Missed black line catch infront of music concert")
    
    # Now turn towards craft creator 
    angle = 0
    turnToAngle(targetAngle = angle, speed = 500)

    # Now drop off the experts
    gyroStraightWithDriveWithAccurateDistance(distance=24, targetAngle=0, speed=700)

    # Now dropoff is done, lets do music concert
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance=25, targetAngle=angle, backward=True, speed=400)

    # turn towards the Music Concert
    turnToAngle(targetAngle = 45, speed = 300)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=13, targetAngle=45, speed=300)
    driveForTime(timeInMS=1000, speed=200)

    # Wait for a little and run Flippy to turn the speakers
    wait(100)
    left_med_motor.run_angle(-1000, 1500)
    wait(100)

    '''
    #Now turn towards craft creator 
    turnToAngle(targetAngle = -90, speed = 700)
    # Now curve to reach expert dropoff area
    drive_base.curve(radius=250,angle = 90)
    # Go straight and dropoff the expert
    gyroStraightWithDriveWithAccurateDistance(distance=15, targetAngle=0, speed=700)

    # Now dropoff is done, lets do music concert

    gyroStraightWithDriveWithAccurateDistance(distance=7, targetAngle=10, backward=True, speed=400)
    gyroStraightWithDriveWithAccurateDistance(distance=19, targetAngle=-20, backward=True, speed=400)

    # turn towards the Music Concert
    turnToAngle(targetAngle = 45, speed = 300)

    # Push the HP and align against it, and turn circular motion arm to do sounds lever
    gyroStraightWithDriveWithAccurateDistance(distance=13, targetAngle=45, speed=300)
    driveForTime(timeInMS=1000, speed=300)

    # Wait for a little and run Flippy to turn the speakers
    wait(100)

    left_med_motor.run_angle(-1000, 1500)

    wait(100)
    '''



def augmentedReality():
    '''
    # Back up from music concert and turn towards Augmented Reality
    angle = 45
    if (gyroStraightWithDriveWithAccurateDistance(distance=15, targetAngle = angle, speed=300, 
                                    tillBlackLine = True, backward=True,
                                    color_sensor = left_color) == False):
        print("Missed black line catch when backing from music concert")
    left_med_motor.run_angle(speed = 1000, rotation_angle = 1500, wait = False)
    gyroStraightWithDriveWithAccurateDistance(distance = 2, speed = 800, targetAngle = angle,backward=True)
    angle = -90
    turnToAngle(targetAngle = angle, speed = 500)

    
    # go to Augmented Reality
    # gyroStraightWithDrive(distanceInCm=33, targetAngle=_angle, speed = 500)
    gyroStraightWithDriveWithAccurateDistance(distance = 36, speed = 800, targetAngle = angle)
    '''
    
    _angle = -45
    turnToAngle(targetAngle=_angle,oneWheelTurn=True)

   # Now move forward to be setup to pull the augmented reality lever
    gyroStraightWithDriveWithAccurateDistance(distance=6, speed = 500, targetAngle=_angle)

    wait(120)
    # turnToAngle(targetAngle = _angle, speed = 300)
    drive_base.turn(angle = 35, wait = False)

    while not drive_base.done():
        if drive_base.stalled():
            drive_base.stop()
    gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 700, targetAngle = 0, backward = True)

    angle = -90
    turnToAngle(targetAngle=angle,speed=300)
    gyroStraightWithDriveWithAccurateDistance(distance = 30, speed = 1000, targetAngle = angle,backward = True)

    turnToAngle(targetAngle = 0, speed = 1000)
    turnToAngle(targetAngle = -90, speed = 750)
    

def expertDrops():
    gyroStraightWithDriveWithAccurateDistance(distance = 30, speed = 700, targetAngle = -90)
    # turn and start driving towards Sound Mixer
    distGyro = gyroStraightWithDrive(distanceInCm=15*CM_PER_INCH, targetAngle=-87, speed=500)

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
    right_med_motor.run_angle(speed = -600, rotation_angle = -1000, then = Stop.COAST, wait = False)

    gyroStraightWithDriveWithAccurateDistance(distance = 18, speed = 500, targetAngle = -75)

    _angle = -45
    turnToAngle(targetAngle = _angle, speed = 300)

    gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 600, targetAngle = _angle)

def resetFlippy():
    left_med_motor.run_angle(1000, 1500)

def run7():
    resetRobot()
    hub.imu.reset_heading(-90)
    #musicconcertnew()
    #resetFlippy()
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