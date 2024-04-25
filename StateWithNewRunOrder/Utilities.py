from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase, DriveBase
from pybricks.tools import wait, StopWatch
from umath import *

hub = PrimeHub()

# Here are the final ports for all the motors and sensors.
# Please don't change these
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
left_med_motor = Motor(Port.B) 
right_med_motor = Motor(Port.D)

#left_color = None
left_color = ColorSensor(Port.A)
right_color = ColorSensor(Port.F)

hub = PrimeHub()

wheel_radius = 44
axle_track = 118
drive_base = robot = GyroDriveBase(
    left_motor,
    right_motor,
    wheel_diameter=88,
    axle_track= 122)

DEFAULT_SPEED = 300
DEFAULT_ACCELERATION = 500
DEFAULT_TURN_RATE = 300
DEFAULT_TURN_ACCEL = 300

# Color defaults
BLACK_COLOR = 24
WHITE_COLOR = 82

CM_PER_INCH = 2.54
MM_PER_INCH = CM_PER_INCH*10

# Constants for Force turn.
FORCETURN_RIGHT = 0
FORCETURN_LEFT = 1
FORCETURN_NONE = 2

# Line follower constants.
LINE_FOLLOWER_EDGE_LEFT = 0
LINE_FOLLOWER_EDGE_RIGHT = 1

# Color sensor to use
LEFT_COLOR_SENSOR = 0
RIGHT_COLOR_SENSOR = 1
AXLE_DIAMETER_CM = 12.2
WHEEL_RADIUS_CM = 4.4

GLOBAL_LEVEL = 1


def resetRobot():
    robot.settings(straight_speed=DEFAULT_SPEED, straight_acceleration=DEFAULT_ACCELERATION, turn_rate=DEFAULT_TURN_RATE, turn_acceleration=DEFAULT_TURN_ACCEL)
    robot.reset()
    left_med_motor.reset_angle(0)
    right_med_motor.reset_angle(0)
    hub.imu.reset_heading(0)
    drive_base.reset()
    
def resetGyro(angle:int = 0):
    hub.imu.reset_heading(angle)

def initializeAndWaitForRobotReady():
    left_med_motor.reset_angle(0)
    right_med_motor.reset_angle(0)
    getDriveBase().heading_control.target_tolerances(speed=50, position=5)   
    while True:
        if (hub.imu.ready() == True):
            break
    hub.imu.reset_heading(0)
    drive_base.reset()
    print("voltage: " + str(hub.battery.voltage()))
    hub.speaker.beep()

def runWithTiming(function, name):
    sw = StopWatch()
    sw.resume()
    startTime = sw.time()
    function()
    endTime = sw.time()
    print("RunTime : " + name + " : " + str(endTime - startTime))
    sw.pause()
    return endTime - startTime

# level can be any number between 0-5
# 5 = Print the most detailed messages
# 1 = Print only the most important messages.
def logMessage(message, level):
    if (level <= GLOBAL_LEVEL):
        print(message)

def getAverageAngle():
    return (left_motor.angle() + right_motor.angle()) / 2

def convertDegToCM(degrees):
    return degrees * WHEEL_RADIUS_CM * pi * 2 / 360

def converCMToDeg(distance):
    return distance * 360 / (WHEEL_RADIUS_CM * pi * 2)

def convertInchesToCM(distanceInInches):
    """
    Convert Inches To CM
    ____________________
    """
    return CM_PER_INCH * distanceInInches

def getDriveBase():
    return drive_base

def stopDriveBase():
    drive_base.drive(speed = 0, turn_rate = 0)
    
def waitForButtonPress():
    # Wait for any button to be pressed, and save the result.
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
    button = pressed[0]
    while any(pressed):
        pressed = hub.buttons.pressed()
    return button

def getHeadingValue():
    return str(hub.imu.heading())

def setDriveBaseSettings(straight_speed, straight_acceleration=DEFAULT_ACCELERATION, turn_rate=DEFAULT_TURN_RATE, turn_acceleration=DEFAULT_TURN_ACCEL):
    drive_base.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)

def getDriveBaseSettings():
    return drive_base.settings()

# Input: color_sensor
# LEFT_COLOR_SENSOR
# RIGHT_COLOR_SENSOR
def getReflectedLight(color_sensor):
    if (color_sensor == LEFT_COLOR_SENSOR):
        return left_color.reflection()
    else:
        return right_color.reflection()

def printDriveBaseValues():
    straight_speed, straight_acceleration, turn_rate, turn_acceleration = drive_base.settings()
    print("straight_speed: " + str(straight_speed))
    print("straight_accelration: " + str(straight_acceleration))
    print("turn_rate: " + str(turn_rate))
    print("turn_acceleration: " + str(turn_acceleration))


# Convert angle to zero to 359 space.
# negative angles are also converted into zero to 359 space.
def _convertAngleTo360(angle):
    negative = False
    if angle < 0:
        angle = abs(angle)
        negative = True

    degreesLessThan360 = angle
    if angle >= 360:
        degreesLessThan360 = angle % 360
    
    if negative == True:
        degreesLessThan360 = 360 - degreesLessThan360

    return degreesLessThan360

# targetAngle should be in 0-359 space.
# Notes on parameters that work:
# speed: 200
# turn_acceleration: (200,400). The deceleration of 400 impacts the turn more than the acceleration.
# straight_speed: Anything above 200 generally works.
# straight_acceleration: Anything above 200 generally works and does not seem to impact the turn accuracy.
# right_correction: Appropriate value of 0.07. Note that this should only be +ve. That means we only correct for overshoot.
# left_correction: Appropriate value of 0.07. Note that this should only be +ve. 
# forceTurn: FORCETURN_RIGHT, FORCETURN_LEFT
#def turnToAngle(targetAngle, speed=300, turn_acceleration=200, turn_deceleration=400, 
#                right_correction=0.07, left_correction = 0.07, forceTurn = FORCETURN_NONE):
def turnToAngle(targetAngle, speed=300, turn_acceleration=200, turn_deceleration=400, 
                right_correction=0.07, left_correction = 0.07, forceTurn = FORCETURN_NONE, oneWheelTurn = False,
                then = Stop.COAST):
    """
    Turns the robot to the specified absolute angle.
    It calculates if the right or the left turn is the closest
    way to get to the target angle. Can handle negative gyro readings.
    The input should however be in the 0-359 space.
    """
    def _calculateCorrectionForTurn(correction, rotations):
        if rotations * 0.02 < correction:
            return correction - (rotations * 0.02)
        else:
            return 0

    # setup the speed to turn.
    straight_speed, straight_acceleration, prevTurnSpeed, prevTurnAcceleration = drive_base.settings()
    drive_base.settings(straight_speed=straight_speed,straight_acceleration=straight_acceleration,
                        turn_rate=speed,turn_acceleration=(turn_acceleration, turn_deceleration))

    direction = None
    currentAngle = hub.imu.heading()
    rotations = currentAngle / 360
    currentAngle = _convertAngleTo360(currentAngle)
    
    if targetAngle >= currentAngle:
        rightTurnDegrees = targetAngle - currentAngle
        leftTurnDegrees = 360 - targetAngle + currentAngle
    else: 
        leftTurnDegrees = currentAngle - targetAngle
        rightTurnDegrees = 360 - currentAngle + targetAngle

    # Figure out the degrees to turn using the correction and the 
    # shortest turning side. Either left or Right.
    degreesToTurn = 0  
    if ((rightTurnDegrees < leftTurnDegrees and forceTurn != FORCETURN_LEFT) or forceTurn == FORCETURN_RIGHT):
        direction = "Right"
        correction = _calculateCorrectionForTurn(right_correction, rotations)
        degreesToTurn = rightTurnDegrees - (correction * rightTurnDegrees)
    else:
        direction = "Left"
        correction = _calculateCorrectionForTurn(left_correction, rotations)
        degreesToTurn = (leftTurnDegrees - (correction * leftTurnDegrees) )* -1
    
    #print("Before drive_base turn currentAngle = " + str(currentAngle) + " degreesToTurn= " + str(degreesToTurn) + "current heading before turn= " + str( hub.imu.heading()) )
    # Use the gyro drive base to turn.
    if oneWheelTurn == False:
        drive_base.turn(degreesToTurn, then=then, wait=True)

    if oneWheelTurn == True:
        if forceTurn == FORCETURN_RIGHT:
            left_motor.run_angle(speed, degreesToTurn * axle_track / wheel_radius)
        elif forceTurn == FORCETURN_LEFT:
            right_motor.run_angle(-1 * speed, degreesToTurn * axle_track / wheel_radius)
        elif degreesToTurn > 0:
            left_motor.run_angle(speed, degreesToTurn * axle_track / wheel_radius)
        elif degreesToTurn < 0:
            right_motor.run_angle(-1 * speed, degreesToTurn * axle_track / wheel_radius)
        else:
            print("ERROR")
        #wait(500)
    
    #print("After turn current heading = " + str( hub.imu.heading()))

    # After the turn we expect that the robot is now correctly pointing in the 
    # direction that we want. Reset the gyro to the angle.
    #hub.imu.reset_heading(targetAngle)

    # Reset the settings to the previous settings.
    drive_base.settings(straight_speed=straight_speed,straight_acceleration=straight_acceleration,
                        turn_rate=prevTurnSpeed,turn_acceleration=prevTurnAcceleration)

def gyroStraightWithDrive(distanceInCm, speed=DEFAULT_SPEED, backward = False, targetAngle = None, 
                          multiplier=2, slowDown=True, slowDistanceMultipler = 0.2):
    global prevValues, correctionPos, savedNums
    stopDriveBase()
    drive_base.reset()

    # If targetAngle is not set explicitly, set it to current heading for convenience
    # rather than assuming all callers want to follow 0-degrees
    if(targetAngle == None):
        targetAngle = hub.imu.heading()
    
    # For convenience, allow caller to specify negative distance to go backward and adjust
    # parameters accordingly. The rest of this function does not work with negative distance
    # so convert that to positive here.
    if (distanceInCm < 0):
        backward = True
        distanceInCm = -1*distanceInCm

    slowSpeed = 100
    midSpeed = speed
    if (backward): 
        slowSpeed = slowSpeed * -1
        midSpeed = midSpeed * -1

    prevValues = []
    correctionPos  = 0
    savedNums = 5

    distanceInMM=distanceInCm * 10
    distanceInMM20 = distanceInMM * 0.2
    
    # Cap the acceleration part of the algo to 20mm
    if distanceInMM20 > 20:
        distanceInMM20 = 20

    slowDistanceInMM = distanceInMM * slowDistanceMultipler

    # If the distance to travel is small, then just use slow speed.
    if distanceInMM < 30:
        midSpeed = slowSpeed = 50
    elif distanceInMM > 500:
        slowDistanceInMM = distanceInMM * 0.1

    # Calculate the speed reduction per distance travelled. We do
    # this upfront, to enable integer multiplication in the loop.
    speedPerDistanceReduction = slowSpeed / distanceInMM

    #print("distance: " + str(distanceInMM) + " distanceInMM20: " + str(distanceInMM20) + 
    #      " slowDistanceInMM: " + str(slowDistanceInMM) +
    #      " speedPerDistanceReduction: " + str(speedPerDistanceReduction)
    #      ) 

    origDistanceDrivenMM = drive_base.distance()
    distanceDrivenMM = origDistanceDrivenMM
    # print("Initial: {}: {}, {}, {}".format(speed, distanceDrivenMM, origDistanceDrivenMM, distanceInMM))
    while (abs(distanceDrivenMM)-abs(origDistanceDrivenMM) < distanceInMM):
        
        distanceDrivenMM = abs(drive_base.distance())
        if (distanceDrivenMM <= distanceInMM20):
            _speed = slowSpeed
        elif (slowDown == True and distanceDrivenMM >= (distanceInMM - slowDistanceInMM)):
            _speed = slowSpeed - (speedPerDistanceReduction * (distanceDrivenMM -(distanceInMM - slowDistanceInMM)))
        else:
            _speed = midSpeed
        
        correction = getCorrectionForDrive(targetAngle, correctionMultiplier = multiplier, adjustCorrection = True)
        # print("{}, {}, {}: {}, {}, {}".format(drive_base.distance_control.stalled(), _speed, correction, drive_base.distance(), origDistanceDrivenMM, distanceInMM))
        drive_base.drive(speed = _speed, turn_rate = correction)
        wait(5)
        #print("distance drive: " + str(distanceDrivenMM) + " speed: " + str(speed))  

    drive_base.drive(0, 0)
    
    # return distance driven to caller
    return (drive_base.distance() - origDistanceDrivenMM)

def getCorrectionForDrive(targetAngle, correctionMultiplier, adjustCorrection = False):
    global prevValues, savedNums, correctionPos
    currentAngle = hub.imu.heading()
    currentAngle = _convertAngleTo360(currentAngle)
    avgCorrection = 0

    if targetAngle >= currentAngle:
        rightTurnDegrees = targetAngle - currentAngle
        leftTurnDegrees = 360 - targetAngle + currentAngle
    else: 
        leftTurnDegrees = currentAngle - targetAngle
        rightTurnDegrees = 360 - currentAngle + targetAngle

    # Figure out the degrees to turn using the correction and the 
    # shortest turning side. Either left or Right.
    degreesToTurn = 0  
    if (rightTurnDegrees < leftTurnDegrees):
        degreesToTurn = rightTurnDegrees 
    else:
        degreesToTurn = -1*leftTurnDegrees

    correction = degreesToTurn
    newCorrection = int(correction * correctionMultiplier)
    if adjustCorrection == True:
        if correction > 2 or correction < -2:
            avgCorrection = sum(prevValues) / savedNums
            newCorrection = (correction + avgCorrection/2) * correctionMultiplier
            if correctionPos < savedNums:
                prevValues.append(correction)
            else:
                #print(str(correctionPos))
                prevValues[correctionPos % savedNums] = correction
            correctionPos = correctionPos + 1
    #print("GetCorrectionForDrive: CurrentAngle: " + str(currentAngle) + " and targetAngle: " + str(targetAngle) + " correction: " + str(correction) + " averageCorrection: " + str(avgCorrection) + " newCorrection: " + str(newCorrection))
    if newCorrection > 20:
        newCorrection = 20
    return newCorrection


#######################################################################################################
# BELOW THIS IS MERGED CODE FROM utilities.py
# We need to merge this with other code.
#######################################################################################################

# def driveTillHueRange(hueRange, hueRangeHigh, sensor=left_color, speed=DEFAULT_SPEED):
def driveTillHsvRange(hueRange, saturationRange=None, valueRange=None, sensor=left_color, speed=DEFAULT_SPEED, maxDistance=0, tag=""):
    origDistanceDrivenMM = drive_base.distance()
    robot.drive(speed = speed, turn_rate = 0)
    # while()
    hsv = sensor.hsv()
    while(not(hsv.h in hueRange and (saturationRange is None or hsv.s in saturationRange) and (valueRange is None or hsv.v in valueRange))): #> hueRange and sensor.hsv().h < hueRangeHigh)):
        if(maxDistance > 0 and (drive_base.distance() - origDistanceDrivenMM > maxDistance)):
            print("Did not find HSV but reached maxDistance {} for {}".format(maxDistance, tag))
            break
        hsv = sensor.hsv()
        # print(hsv)
    logMessage("HSV values: h:{}, s:{}, v:{} for {}".format(sensor.hsv().h, sensor.hsv().s, sensor.hsv().v, tag), level=5)
    robot.drive(0, 0)
    # robot.stop()
    # robot.straight(distance=0, then=Stop.BRAKE, wait=True)
    return (drive_base.distance() - origDistanceDrivenMM)

def testHsv(sensor=left_color):
    while  True:
        print("(h,s,v) = {}".format(sensor.hsv()))
        wait(100)

def testColor(sensor=left_color):
    while  True:
        print("Color: {}".format(sensor.color()))

# pickup Expert Attachment constants
RUN6_PICKUP_EXPERT_ATTACHMENT_DOWN = 1
RUN6_PICKUP_EXPERT_ATTACHMENT_UP = 2

# Expects the arm to start down.
def run6PositionPickUpExpertAttachment(position=RUN6_PICKUP_EXPERT_ATTACHMENT_DOWN, wait=True, speed = 300):
    if position == RUN6_PICKUP_EXPERT_ATTACHMENT_DOWN:
        right_med_motor.run_target(speed + 200, 150, Stop.HOLD, wait)
    else:
        right_med_motor.run_target(speed, 0, Stop.HOLD, wait)


def driveForTime(timeInMS, stopAtEnd=True, speed=DEFAULT_SPEED, turnRate=0):
    drive_base.use_gyro(False)
    stopwatch = StopWatch()
    start = stopwatch.time()
    end = 0
    while end - start < timeInMS:
        robot.drive(speed=speed, turn_rate=turnRate)
        end = stopwatch.time()
    
    if(stopAtEnd):
        robot.drive(speed=0, turn_rate=0)
    
    drive_base.use_gyro(True)

def gyroStraightWithDriveWithAccurateDistance(distance, speed, backward = False, targetAngle = 0, 
                          multiplier=2, gradualAcceleration=True, 
                          slowDown=True, slowDistanceMultipler = 0, printDebugMesssages=False,
                          skipCorrectionCalculation = False,
                          tillBlackLine = False,
                          tillWhiteLine = False,
                          color_sensor = left_color,
                          detectStall = False,
                          useSlowerAccelerationForBackward = True, # Use this parameter when you want to just go fast home.
                          stop = Stop.HOLD):
                         
    global prevValues, correctionPos, savedNums
    savedNums = 5
    prevValues = []
    correctionPos  = 0

    def _getValueInternal(color_sensor):
        return color_sensor.hsv().v

    def _stopDriveBaseInternal(stop=Stop.HOLD):
        drive_base.straight(distance=0,then=stop)
        if (stop == Stop.HOLD):
            left_motor.hold()
            right_motor.hold()


    # Convert angle to zero to 359 space.
    # negative angles are also converted into zero to 359 space.
    def _convertAngleTo360Internal(angle):
        negative = False
        if angle < 0:
            angle = abs(angle)
            negative = True

        degreesLessThan360 = angle
        if angle >= 360:
            degreesLessThan360 = angle % 360
        
        if negative == True:
            degreesLessThan360 = 360 - degreesLessThan360

        return degreesLessThan360
                          

    def _getCorrectionForDriveInternal(targetAngle, correctionMultiplier, adjustCorrection = False, 
                          printDebugMesssages = False):
        global prevValues, correctionPos, savedNums
        currentAngle = hub.imu.heading()
        currentAngle = _convertAngleTo360Internal(currentAngle)
        avgCorrection = 0

        if targetAngle >= currentAngle:
            rightTurnDegrees = targetAngle - currentAngle
            leftTurnDegrees = 360 - targetAngle + currentAngle
        else: 
            leftTurnDegrees = currentAngle - targetAngle
            rightTurnDegrees = 360 - currentAngle + targetAngle

        # Figure out the degrees to turn using the correction and the 
        # shortest turning side. Either left or Right.
        degreesToTurn = 0  
        if (rightTurnDegrees < leftTurnDegrees):
            degreesToTurn = rightTurnDegrees 
        else:
            degreesToTurn = -1*leftTurnDegrees

        if (printDebugMesssages == True):
            print("degreesToTurn=" + str(degreesToTurn) + " current_angle=" + str(currentAngle) + 
                " target_angle="+str(targetAngle))

        correction = degreesToTurn
        newCorrection = int(correction * correctionMultiplier)
        if adjustCorrection == True:
            if correction > 2 or correction < -2:
                avgCorrection = sum(prevValues) / savedNums
                newCorrection = (correction + avgCorrection/2) * correctionMultiplier
                if correctionPos < savedNums:
                    prevValues.append(correction)
                else:
                    #print(str(correctionPos))
                    prevValues[correctionPos % savedNums] = correction
                correctionPos = correctionPos + 1
        #print("GetCorrectionForDrive: CurrentAngle: " + str(currentAngle) + " and targetAngle: " + str(targetAngle) + " correction: " + str(correction) + " averageCorrection: " + str(avgCorrection) + " newCorrection: " + str(newCorrection))
        if newCorrection > 20:
            newCorrection = 20
        return newCorrection

    if backward == True and useSlowerAccelerationForBackward == True:
        drive_base.settings(straight_speed=400,straight_acceleration=300,
                        turn_rate=400,turn_acceleration=(100, 400))

    def blackStoppingCondition(color_sensor):
        #light = getReflectedLight()
        light = _getValueInternal(color_sensor)
        return light <= BLACK_COLOR

    def whiteStoppingCondition(color_sensor):
        #light = getReflectedLight()
        light = _getValueInternal(color_sensor)
        return light >= WHITE_COLOR

    stopping_condition_function = None
    if (tillBlackLine == True and tillWhiteLine == True):
        raise ValueError("Only tillBlackLine or tillWhiteLine should be true, not both.")
    elif (tillBlackLine == True):
        stopping_condition_function = blackStoppingCondition
    elif (tillWhiteLine == True):
        stopping_condition_function = whiteStoppingCondition

    drive_base.reset()
    #stopDriveBase(stop)
    prevValues = []
    correctionPos  = 0
    savedNums = 5
    counter = 0

    if (slowDown == False):
        slowDistanceMultipleInternal = 0
    else:
        slowDistanceMultipleInternal = (0.4 / 500) * (speed - 500) + 0.4

    # If the user has given as slowDistanceMultiplier use that.
    if (slowDistanceMultipler != 0):
        slowDistanceMultipleInternal = slowDistanceMultipler

    distanceInMM=distance * 10
    startSlowDistanceMM = 20
    finalSlowDistanceMM = 20
    slowDownDistanceMM = distanceInMM * slowDistanceMultipleInternal
    midDistanceMM = distanceInMM - startSlowDistanceMM - finalSlowDistanceMM - slowDownDistanceMM
    
    # Slow speed is used for both the start and final distances.
    slowSpeed = 100
    midSpeed = speed

    # Calculate the speed reduction per distance travelled. We do
    # this upfront, to enable integer multiplicaation in the loop.
    # deceleration is always a +ve number.
    if (slowDownDistanceMM != 0):
        deceleration = (midSpeed - slowSpeed) / slowDownDistanceMM

    if (backward): 
        slowSpeed = slowSpeed * -1
        midSpeed = midSpeed * -1
    
    if (printDebugMesssages):
        print(
          "distanceInMM: " + str(distanceInMM) + 
          " startSlowDistanceMM: " + str(startSlowDistanceMM) +
          " midDistanceMM: " + str(midDistanceMM) +
          " slowDownDistanceMM: " + str(slowDownDistanceMM) +
          " finalSlowDistanceMM: " + str(finalSlowDistanceMM) +
          " slowSpeed: " + str(slowSpeed) +
          " midSpeed: " + str(midSpeed))
    
    distanceDrivenMM = drive_base.distance()
    drive_base.drive(speed = slowSpeed, turn_rate = 0)

    stopCondition = False
    if (printDebugMesssages == True):
        print("distancedrivenMM: " + str(distanceDrivenMM) + " distanceInMM: " +  str(distanceInMM))
    while (distanceDrivenMM < distanceInMM):
        if (tillBlackLine == True or tillWhiteLine == True):
            stopCondition = stopping_condition_function(color_sensor)


        if ((tillBlackLine == True or tillWhiteLine == True) and stopCondition == True):
            break
        elif (detectStall == True and drive_base.stalled() == True):
            break

        distanceDrivenMM = abs(drive_base.distance())

        # If the total distance to travel is small, just use the slowSpeed 
        # and override all the other speeds.
        if (distanceInMM <= 50):  
            speed = slowSpeed
        elif (distanceDrivenMM <= startSlowDistanceMM):
            speed = slowSpeed
        elif (distanceDrivenMM <= midDistanceMM + startSlowDistanceMM):
            speed = midSpeed
        elif (slowDown == True and 
              distanceDrivenMM <= midDistanceMM + startSlowDistanceMM + slowDownDistanceMM):
            if (backward == False):
                speed = midSpeed - (deceleration * (distanceDrivenMM - (midDistanceMM + startSlowDistanceMM)))
            else:
                speed = midSpeed + (deceleration * (distanceDrivenMM - (midDistanceMM + startSlowDistanceMM)))    
        elif (distanceDrivenMM <= distanceInMM):
            speed = slowSpeed
         
        if skipCorrectionCalculation == False:
            correction = _getCorrectionForDriveInternal(targetAngle, correctionMultiplier = multiplier, 
                                           adjustCorrection = True, 
                                           printDebugMesssages=printDebugMesssages)
        else:
            correction = 0

        # Override correction if its small.
        #if (correction < 1): 
        #    correction = 0
        #if(counter % 100 == 0):
        #    print("correction=" + str(correction) + " speed=" + str(speed)
        #          + " distanceDrivenMM=" + str(distanceDrivenMM))
        counter = counter + 1
        drive_base.drive(speed = speed, turn_rate = correction)
        wait(5)

    drive_base.stop()
    _stopDriveBaseInternal(stop)

    if backward == True and useSlowerAccelerationForBackward == True:
        drive_base.settings(straight_speed=400,straight_acceleration=1000,
                        turn_rate=400,turn_acceleration=(150, 400))

    return stopCondition 


### New stall detection by Rishabh:
class stall_detect:
    def getLoad():
        left_load = abs(left_motor.load())
        right_load = abs(right_motor.load())
        currLoad = int((left_load + right_load) / 2)
        return currLoad
                
    # stalls based on load
    def load(max_load = 100, min_stopping_condition = 40, debug = False):

        while drive_base.done() == False: # while either motor is still moving
            #load = stall_detect.getCurrentLoad(3, minAllowedLoad = min_stopping_condition)
            load = stall_detect.getLoad()
            if load  > max_load: # if there is extra load
                if debug == True:
                    print("Stopping stall detection with " + str(load) + " load.") # print debug messages

                # stop the motors
                left_motor.stop()
                right_motor.stop()

                # exit the loop
                break

            else: # if there is no extra load
                if debug == True:
                    print("Continuing stall detection with " + str(load) + " load.") # print debug messages

                continue # keep running the loop

    # stalls based on running average of load
    def avg_load(max_load_change, minValidLoad = 30, minObservationsRequired = 5, min_dist = 0, debug = False):
        loadArr = []

        main_counter = 0
        if min_dist > 0:
            drive_base.reset()

        while drive_base.done() == False: # while the code is still running
            # calculate load
            currLoad = stall_detect.getCurrentLoad(3, minValidLoad)

            if(currLoad < minValidLoad):
                continue
            
            if(len(loadArr)>=minObservationsRequired):
                # calculate average of running average
                load_sum = 0
                for i in range(len(loadArr)):
                    load_sum = load_sum + loadArr[i]

                avgLoad = int(load_sum / (1+len(loadArr)))

                # if the load is greater than 50% more than the running average
                if len(loadArr) >= minObservationsRequired and currLoad >= int(avgLoad * (max_load_change + 1)) and currLoad > minValidLoad and drive_base.distance() > min_dist:

                    # stop the motors
                    left_motor.stop()
                    right_motor.stop()

                    if debug == True:
                        print("Stopping stall detection with " + str(currLoad) + " load and " + str(int(avgLoad * (max_load_change + 1))) + " stopping condition and " + str(main_counter) + " readings") # print debug messages

                    # exit the function
                    break

                else:
                    if debug == True:
                        print("Continuing stall detection with " + str(currLoad) + " load and " + str(int(avgLoad * (max_load_change + 1))) + " stopping condition." + str(main_counter) + " readings") # print debug messages
                        print(loadArr)

                loadArr[main_counter % minObservationsRequired] = currLoad
            else:
                loadArr.append(currLoad)
                print("not enough observations. Adding {} to the array.".format(currLoad))

            main_counter += 1
            wait(5)

    def getCurrentLoad(numObs, minAllowedLoad, delayBetweenReadingsMs=1):
        totalLoad = 0 #[0, 0, 0]
        for i in range(0, numObs):
            currLoad = 0
            while(currLoad < minAllowedLoad):
                left_load = abs(left_motor.load())
                right_load = abs(right_motor.load())
                currLoad = int((left_load + right_load) / 2)
                print("Current load {} is less than min {}".format(currLoad, minAllowedLoad))
            # totalLoad[i] = currLoad
            totalLoad = totalLoad + currLoad
            #wait(delayBetweenReadingsMs)
        return int(totalLoad/numObs)

    # stalls based on angle change
    def angle_change(max_iterations = 5, deadzone = 10, debug = False):
        # define reading arrays
        right_readings = []
        left_readings = []

        while drive_base.done() == False: # while either motor is still moving
            if int((len(right_readings) + len(left_readings)) / 2) > 5: # if there are more than 5 readings
                # append new readings
                right_readings.append(right_motor.angle())
                left_readings.append(left_motor.angle())

                # calculate the motor speed for proportional calculations
                right_speed = right_motor.speed()
                left_speed = left_motor.speed()
                speed = int((right_speed + left_speed) / 2)

                # calculate the reading diff
                right_reading_diff = right_readings[-1] - right_readings[-1 * max_iterations]
                left_reading_diff = left_readings[-1] - left_readings[-1 * max_iterations]
                reading_diff = int((right_reading_diff + left_reading_diff) / 2)

                if reading_diff < int((deadzone * speed) / 100): # if the readings haven't changed enough
                    # stop the motors
                    right_motor.stop()
                    left_motor.stop()
                    
                    if debug == True:
                        print("Stopping stall detection with angle change of " + str(reading_diff) + " degrees.") # print debug messages

                    # exit the loop
                    break

                else:
                    if debug == True:
                        print("Continuing stall detection with angle change of " + str(reading_diff) + " degrees.")

            else: # if there are less than 5 readings
                # append new readings
                right_readings.append(right_motor.angle())
                left_readings.append(left_motor.angle())