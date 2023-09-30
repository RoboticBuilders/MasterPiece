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
WHITE_COLOR = 90

_CM_PER_INCH = 2.54
_MM_PER_INCH = _CM_PER_INCH*10

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

def resetRobot():
    robot.settings(straight_speed=DEFAULT_SPEED, straight_acceleration=DEFAULT_ACCELERATION, turn_rate=DEFAULT_TURN_RATE, turn_acceleration=DEFAULT_TURN_ACCEL)
    robot.reset()

def resetGyro(angle:int = 0):
    hub.imu.reset_heading(angle)

def initializeAndWaitForRobotReady():
    getDriveBase().heading_control.target_tolerances(speed=50, position=5)   
    while True:
        if (hub.imu.ready() == True):
            break
    hub.imu.reset_heading(0)
    drive_base.reset()
    print("voltage: " + str(hub.battery.voltage()))
    hub.speaker.beep()

def runWithTiming(function,name):
    sw = StopWatch()
    sw.resume()
    startTime = sw.time()
    function()
    endTime = sw.time()
    print(name + " : " + str(endTime - startTime))
    sw.pause()
    return endTime - startTime

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
    return _CM_PER_INCH * distanceInInches

def getDriveBase():
    return drive_base

def stopDriveBase():
    left_motor.hold()
    right_motor.hold()

def waitForLeftButtonPress():
    # Wait for any button to be pressed, and save the result.
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
        if (Button.LEFT in pressed):
            return

def getHeadingValue():
    return str(hub.imu.heading())

def setDriveBaseSettings(straight_speed, straight_acceleration, turn_rate, turn_acceleration):
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
                right_correction=0.07, left_correction = 0.07, forceTurn = FORCETURN_NONE, oneWheelTurn = False):
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
        drive_base.turn(degreesToTurn, then=Stop.HOLD, wait=True)

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

def driveTillDistance(distanceinCM, speed, backward=False, wait=True):
    # Get the drivebase settings
    straight_speed, straight_acceleration, turn_rate, turn_acceleration = getDriveBaseSettings()
    setDriveBaseSettings(speed, straight_acceleration, turn_rate, turn_acceleration)

    distanceToDriveInMM = distanceinCM * 10
    if backward == True:
        distanceToDriveInMM = distanceToDriveInMM * -1

    # Drive forward using the drive base command.
    drive_base.straight(distanceToDriveInMM, wait=wait)

    # restore the default drive base settings
    setDriveBaseSettings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)

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
    # this upfront, to enable integer multiplicaation in the loop.
    speedPerDistanceReduction = slowSpeed / distanceInMM

    #print("distance: " + str(distanceInMM) + " distanceInMM20: " + str(distanceInMM20) + 
    #      " slowDistanceInMM: " + str(slowDistanceInMM) +
    #      " speedPerDistanceReduction: " + str(speedPerDistanceReduction)
    #      ) 

    origDistanceDrivenMM = drive_base.distance()
    distanceDrivenMM = origDistanceDrivenMM
    while (abs(distanceDrivenMM)-abs(origDistanceDrivenMM) < distanceInMM):
        distanceDrivenMM = abs(drive_base.distance())
        if (distanceDrivenMM <= distanceInMM20):
            speed = slowSpeed
        elif (slowDown == True and distanceDrivenMM >= (distanceInMM - slowDistanceInMM)):
            speed = slowSpeed - (speedPerDistanceReduction * (distanceDrivenMM -(distanceInMM - slowDistanceInMM)))
        else:
            speed = midSpeed
        
        correction = getCorrectionForDrive(targetAngle, correctionMultiplier = multiplier, adjustCorrection = True)
        drive_base.drive(speed = speed, turn_rate = correction)
        wait(5)
        #print("distance drive: " + str(distanceDrivenMM) + " speed: " + str(speed))  

    drive_base.stop()
    stopDriveBase()     

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

# This method is line the _driveTillLine, however it only works for black and it assumes a white->black line
# it first searches for the white line and then searches for the black line.
# It will return false if the line is not found (either the white line or the black following the white.)
def driveTillBlackLine(speed, distanceInCM, target_angle, gain = 1, color_sensor=LEFT_COLOR_SENSOR,
                       blackSpeed = 200, backward=False):
    drive_base.stop()
   
    remainingDistance = distanceInCM
    FINAL_SLOW_SPEED = 200

    def blackStoppingCondition():
        light = getReflectedLight(color_sensor)
        return light <= BLACK_COLOR

    def whiteStoppingCondition():
        light = getReflectedLight(color_sensor)
        return light >= WHITE_COLOR
    
    # First drive at speed till we find white.
    reachedStoppingCondition = _driveStraightWithSlowDownTillLine(distanceInCM, speed, target_angle, gain, 
                                                                  reachedStoppingCondition=whiteStoppingCondition,
                                                                  backward=backward)

    # If we found the white line, then we next search for the black line very slowly.
    # If we dont find the black line now, then we stop at distance and return false.
    if reachedStoppingCondition == True:
        #print("withing the reachedFirstStopping condition.")
        BLACK_FIND_SPEED = blackSpeed
        distanceTravelled = abs(drive_base.distance()) / 10
        remainingDistance = distanceInCM - distanceTravelled
        #print("remainingDistance: " + str(remainingDistance) + " distanceTravelled: " + str(distanceTravelled))
        reachedStoppingCondition = _driveStraightWithSlowDownTillLine(remainingDistance, BLACK_FIND_SPEED, 
                                                                      target_angle, gain,
                                                                      reachedStoppingCondition=blackStoppingCondition,
                                                                      backward=backward)
    
    drive_base.stop()
    return reachedStoppingCondition   

def _driveStraightWithSlowDownTillLine(distance, speed, target_angle, gain, 
                                       reachedStoppingCondition, backward):
    """
    Drive Straight
    ______________
    This is a internal function do not call directly. Call drive instead.

    The algorithm goes from speed to speed 10 until distance is travelled.
    slowDown: True if you want to slow down over the distance. Note that
    the function uses a combination of distance and the reachedStoppingCondition
    checks to stop.

    reachedStoppingCondition: This is a function that does not take any parameter and is expected to return true when the loop should be terminated.
    return the output of the stoppingCondition.
    """
    drive_base.reset()
    startDistance = abs(drive_base.distance() / 10)
    currentSpeed = speed

    # Drop the speed from speed to five in distanceInDeg.
    distanceTravelled = 0
    
    FINAL_SLOW_SPEED=300
    if backward == False:
        drive_base.drive(int(currentSpeed),0)
    else:
        drive_base.drive(int(currentSpeed) * -1,0)

    stopCondition = False
    while  abs(distanceTravelled) <= distance and stopCondition == False:
        turn_rate = getCorrectionForDrive(target_angle, gain)
        if (abs(turn_rate) > 1):
            if backward == False:
                drive_base.drive(int(currentSpeed),turn_rate)
            else:
                drive_base.drive(int(currentSpeed) * -1, turn_rate)

        distanceTravelled = abs(drive_base.distance() / 10) - startDistance
        stopCondition = reachedStoppingCondition()

    drive_base.stop()
    stopDriveBase()

    #logMessage("DrivestraightWiuthSlowDownTillLine completed", level=5)
    return stopCondition

# Input:
# edge: LINE_FOLLOWER_EDGE_LEFT, LINE_FOLLOWER_EDGE_RIGHT 
def followBlackLine(speed, distance, control_color, edge, gain = 1, slowDown = True, color_sensor=LEFT_COLOR_SENSOR):
    drive_base.reset()
    stopDriveBase()

    distanceInMM=distance * 10
    distanceInMM20 = distanceInMM * 0.2
    
    # Cap the acceleration part of the algo to 20mm
    if distanceInMM20 > 20:
        distanceInMM20 = 20

    slowDistanceInMM = distanceInMM * 0.5
    slowSpeed = 100
    midSpeed = speed

    # If the distance to travel is small, then just use slow speed.
    if distanceInMM < 30:
        midSpeed = slowSpeed = 50
    elif distanceInMM > 500:
        slowDistanceInMM = distanceInMM * 0.1

    # Calculate the speed reduction per distance travelled. We do
    # this upfront, to enable integer multiplicaation in the loop.
    speedPerDistanceReduction = slowSpeed / distanceInMM

    #print("distance: " + str(distanceInMM) + " distanceInMM20: " + str(distanceInMM20) + 
    #      " slowDistanceInMM: " + str(slowDistanceInMM) +
    #      " speedPerDistanceReduction: " + str(speedPerDistanceReduction)
    #      ) 

    distanceDrivenMM = drive_base.distance()
    while (distanceDrivenMM < distanceInMM):
        distanceDrivenMM = abs(drive_base.distance())           
        if (distanceDrivenMM <= distanceInMM20):
            speed = slowSpeed
        elif (slowDown == True and (distanceDrivenMM >= (distanceInMM - slowDistanceInMM))):
            speed = slowSpeed - (speedPerDistanceReduction * (distanceDrivenMM -(distanceInMM - slowDistanceInMM)))
        else:
            speed = midSpeed
        
        if edge == LINE_FOLLOWER_EDGE_RIGHT:
            turn_rate = (getReflectedLight(color_sensor) - control_color) * -gain
        else:
            turn_rate = (getReflectedLight(color_sensor) - control_color) * gain

        if (abs(turn_rate) > 1):
            drive_base.drive(speed = speed, turn_rate = turn_rate)
        wait(5)
        #print("distance drive: " + str(distanceDrivenMM) + " speed: " + str(speed))   

    drive_base.stop()
    stopDriveBase()

#######################################################################################################
# BELOW THIS IS MERGED CODE FROM utilities.py
# We need to merge this with other code.
#######################################################################################################

def goStraight(distance, wait=True, backward = False, straightSpeed=DEFAULT_SPEED, straightAcceleration=DEFAULT_ACCELERATION, turnRate=DEFAULT_TURN_RATE, turnAcceleration=DEFAULT_TURN_ACCEL):
    """
    Drives the robot straight for a specified distance.

    distance -- Distance to travel in mm

    wait -- [Optional, default=True] wait for action to finish before returning from function

    backward -- [Optional, default=False] set to True to move backwards, else robot will move forward

    straightSpeed -- [Optional, default= (Number, mm/s) Straight-line speed of the robot.

    straightAcceleration -- (Number, mm/s²) Straight-line acceleration and deceleration of the robot. Provide a tuple with two values to set acceleration and deceleration separately.

    turnRate -- (Number, deg/s) Turn rate of the robot.

    turnAcceleration (Number, deg/s²) Angular acceleration and deceleration of the robot. Provide a tuple with two values to set acceleration and deceleration separately.
    """
    (origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
    robot.settings(straightSpeed, straightAcceleration, turnRate, turnAcceleration)

    if(backward):
        robot.straight(-1*distance, wait=wait)
    else: 
        robot.straight(distance, wait=wait)
    
    robot.settings(origSpeed, origAccel, origTurnSpeed, origTurnAccel)

def turnToAngle_AA(absoluteAngle:int, turnRate:int=DEFAULT_TURN_RATE, turnAcceleration=DEFAULT_TURN_ACCEL, wait=True, oneWheelTurn=False):
    """
    Turns the robot to the specific Gyro angle

    absoluteAngle -- Target angle the robot should get to (range -179 to 180)

    wait -- [Optional, default=True] wait for action to finish before returning from function
    """
    (origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
    robot.settings(origSpeed, origAccel, turnRate, turnAcceleration)

    angleToTurn = absoluteAngle - robot.angle()
    if oneWheelTurn==False:
        robot.turn(angleToTurn)
    elif oneWheelTurn==True:
        deg = (((6.28*AXLE_DIAMETER_CM)*(angleToTurn/360))/(6.28*WHEEL_RADIUS_CM))*360
        if angleToTurn < 0:
            right_motor.run_angle(speed=origTurnSpeed, rotation_angle=deg)
        elif angleToTurn > 0:
            print(deg)
            left_motor.run_angle(speed=origTurnSpeed,rotation_angle=deg)

    robot.settings(origSpeed, origAccel, origTurnSpeed, origTurnAccel)

def driveTillLine(speed, doCorrection=True, sensor=left_color, blackOrWhite="Black"):
    
    def _compareValue(sensor, value):
        return sensor.hsv().v in value

    if (blackOrWhite=="Black"):
        func = _compareValue
        vRange = range(0, 35)
    else:
        func = _compareValue
        vRange = range(100, 100)

    robot.drive(speed = speed, turn_rate = 0)
    while(func(sensor, vRange) != True):
        hsv = sensor.hsv()
        print(hsv)
    print("Stopping at (h,s,v) = {}".format(sensor.hsv()))

    robot.stop()
    robot.straight(distance=0, then=Stop.BRAKE, wait=True)

    if(doCorrection):
        (origSpeed, origAccel, origTurnSpeed, origTurnAccel) = robot.settings()
        robot.settings(100, 100, 100, 100)
        robot.straight(distance=-40, then=Stop.HOLD, wait=True)
        robot.settings(origSpeed, origAccel, origTurnSpeed, origTurnAccel)

def driveTillColor(color, sensor=left_color, speed=DEFAULT_SPEED):
    robot.drive(speed = speed, turn_rate = 0)
    while(sensor.color() != color):
        print(sensor.color())
    print(sensor.color())
    robot.stop()
    robot.straight(distance=0, then=Stop.BRAKE, wait=True)

# def driveTillHueRange(hueRange, hueRangeHigh, sensor=left_color, speed=DEFAULT_SPEED):
def driveTillHueRange(hueRange, saturationRange=None, valueRange=None, sensor=left_color, speed=DEFAULT_SPEED):
    robot.drive(speed = speed, turn_rate = 0)
    # while()
    hsv = sensor.hsv()
    while(not(hsv.h in hueRange) or not(hsv.s in saturationRange) or not(hsv.v in valueRange)): #> hueRange and sensor.hsv().h < hueRangeHigh)):
        hsv = sensor.hsv()
        print(hsv)
    print(sensor.hsv().h)
    robot.drive(0, 0)
    # robot.stop()
    # robot.straight(distance=0, then=Stop.BRAKE, wait=True)

def testHsv(sensor=left_color):
    while  True:
        print("(h,s,v) = {}".format(sensor.hsv()))

def testColor(sensor=left_color):
    while  True:
        print("Color: {}".format(sensor.color()))

