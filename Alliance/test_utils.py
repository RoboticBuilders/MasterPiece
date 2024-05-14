from pybricks.hubs import PrimeHub
from pybricks.pupdevices  import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch
from Utilities import *


def testDriveForTime():
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle=0, speed=500)
    drive_base.use_gyro(False)
    driveForTime(timeInMS = 500, stopAtEnd = True, speed = 300, turnRate = 0)
    wait(2000)

def testMedMotors():
    left_med_motor.run(1000)
    right_med_motor.run(1000)

    wait(10 * 1000)

    print(left_med_motor.angle())
    print(right_med_motor.angle())

def testStallDetect():
    stall_detect.avg_load(max_load_change = 1, minValidLoad = 30, minObservationsRequired = 15, min_dist = 300, debug = True)

def testParallelCode():
    right_med_motor.run_angle(speed=2000, rotation_angle = -800, wait = False)
   
    # Drive towards the scene change, catch the line.
    angle = 0
    gyroStraightWithDriveWithAccurateDistance(distance=50, speed=500, targetAngle=angle,
                                              backward=False)
def testARlineFollow():
    angle = 45
    hub.imu.reset_heading(angle)
    
    wait(50)
    drive_base.straight(-70)
    if (gyroStraightWithDriveWithAccurateDistance(distance=7, targetAngle = angle, speed=300, 
                                    tillBlackLine = True, backward=True,
                                    color_sensor = left_color) == False):
        print("Missed black line catch when backing from music concert")
   
    #gyroStraightWithDriveWithAccurateDistance(distance = 6, speed = 200, targetAngle = angle, backward=True)
    drive_base.straight(-70)

    # Now drive towars the augmented reality
    angle = -90
    turnToAngle(targetAngle = angle, speed = 500)
    #waitForButtonPress()
    followBlackLinePID(distanceInMM=220, speed=100, edge=LINE_FOLLOWER_EDGE_RIGHT, controlColor = 63, color_sensor=right_color,
                       kp=0.3, ki=0, kd=1, correctionBasedSpeed = False, slowStart = True, 
                       slowDown = True, printDebugMessages=True)
    gyroStraightWithDriveWithAccurateDistance(distance=20, targetAngle = angle, speed=300, 
                                    tillBlackLine = False, backward=False,
                                    color_sensor = left_color)
    # Now open the slider to bring in the augmented reality.
    openAugmentedRealitySlider()

    #waitForButtonPress()

    # Backup to pull the lever
    drive_base.straight(-40)
    
    #closeAugmentedRealitySlider()
    closeAugmentedRealitySliderFully()
    #PullInTheAugmentedRealityLever()
    
    # Now backoff to push the lever in and turn to ensure the lever is turned
    # We backoff at an angle, because the augmented reality opens 
    # and we want to make sure we dont hit it.
    angle = -87  # was -82
    turnToAngle(targetAngle = angle, speed = 700)
    gyroStraightWithDriveWithAccurateDistance(distance = 33, speed = 1000, targetAngle = angle, backward = True)
    #closeAugmentedRealitySliderCompletely()
    
    # Now turn to ensure that we have pushed in the augmented reality. We turn and drive forward
    # then backoff till the white line and turn back to our heading.
    angle = -30
    turnToAngle(targetAngle = angle, speed = 1000)
    gyroStraightWithDriveWithAccurateDistance(distance = 17, speed = 250, targetAngle = angle)                                    

def turnToBlackLine(dir = "r", speed = 500, color_sensor = "left", min_dist = 0):
    def _getColor(color):
        if color == "left":
            color = left_color.hsv().v
        
        elif color == "right":
            color = right_color.hsv().v

        return color

    dist_travelled = 0

    left_motor.reset_angle()
    right_motor.reset_angle()

    if dir == "r":
        left_motor.run(speed)
        right_motor.run(-speed)

        while True:
            print(dist_travelled)

            if _getColor(color_sensor) > WHITE_COLOR and abs(dist_travelled) > min_dist:
                break

            dist_travelled = left_motor.angle()

        left_motor.stop()
        right_motor.stop()

    elif dir == "l":
        print(dist_travelled)

        right_motor.run(speed)
        left_motor.run(-speed)

        while True:
            if _getColor(color_sensor) > WHITE_COLOR and abs(dist_travelled) > min_dist:
                break

            dist_travelled = right_motor.angle()

        left_motor.stop()
        right_motor.stop()

def run6expertdropoff():
        left_med_motor.run_angle(speed=2000, rotation_angle=500)
def testtiming():
        runWithTiming(run6expertdropoff,"run6expertdropoff")

def testStallDetect():
    drive_base.straight(distance = 450, wait = False)
    stall_detect.avg_load(max_load_change = 1, minValidLoad = 30, minObservationsRequired = 15, min_dist = 50, debug = True)



#testParallelCode()
#gyroStraightWithDriveWithAccurateDistance(distance=50, targetAngle=0, backward=True, speed=300, tillWhiteLine = True, color_sensor = left_color)
#testARlineFollow()
#turnToBlackLine(dir = "l", speed = 150, color_sensor = "left", min_dist = 50)
# testtiming()
testStallDetect()