# LEGO type:standard slot:2
# This is now the version of Round1 that we are committed to.
#
# This is the next version of the Round1 that we tried after TestRound1WithPowerPlantAsSeparateRun.py which was done after Round1FullRunWithFewerArms.py
# This file was created because after doing TestRound1WithPowerPlantAsSeparateRun we realized that the bucket arm can do the hybrid car,
# since now it does not have any units. This means that the going home for bringing the hybrid car, which is error prone can be avoided.
# The rest of the changes in TestRound1WithPowerPlantAsSeparateRun are all there in this file.
#
#
# This file also contains one more change in addition to the above. We realized that we could do the toy factory as part of run3
# this is because we have the units from the power plant from run2. This means that we need to do the toy factory in run3 and
# not do this in run6. However because we are already aligning against the toy factory in run3, we dont really need any additional
# code for run3. We only need to change run6 to not have the toyfactory.
#  
# Run1 : TV, wind turbine, rechargeable (note: no hybrid car.)
# Run2 : Power plant and go back to Right home.
# Run3 : Drop off units in rechargeable, hybrid car (DONE with bucket arm), toy factory, two water units (Like the Round1FullRunWithFewerArms we dont do the smart grid here.), 
#        one solar power unit and go to Left home. We are carrying the dinosaur. (Note we dont do the power plant here.)
# Run4 : Small run to get the one water unit and the hydro-electric unit.
# Run5 : No change (oil platform run)
# Run6 : Smart grid(done with a bucket arm), Water reservoir, power to X(done with a bucket arm), (Note no toy factory)
from spike import PrimeHub, ColorSensor,  Motor, MotorPair
from math import *
import collections
# Note that the "hub" import is needed, this is different from the PrimeHub import above, this is the way to access the battery.
import time, hub
from spike.operator import *
from spike.control import wait_for_seconds
from spike.control import *
import gc
import math
import random

# Various robot constants
AXLE_DIAMETER_CM = 12.7
AXLE_DIAMETER_CM_CORRECTED = 12.2
WHEEL_RADIUS_CM = 4.4
GLOBAL_LEVEL = 0
ANYA_RUN_START_OFFSET_TO_MAT_WEST = 0
TOTAL_DEGREES_TURNED = 0
LAST_TURN_LEFT = False

# Which Marvin is this.
# Amogh: A
# Rishabh-Nami: RN
# Anya:Arisha: AA
ROBOT = "A" 

primeHub = PrimeHub()

# Left large motor
motorC = Motor("C")
left_large_motor = motorC
# Right large motor
motorE = Motor("E")
right_large_motor = motorE

# The motor pair
wheels = MotorPair('C', 'E')

# Right medium motor
motorD = Motor("D")
right_medium_motor = motorD
# Left medium motor
motorF = Motor("F")
left_medium_motor = motorF

#Right color sensor
colorB = ColorSensor("B")
rightColorSensor = colorB # Easier alias to use in code

#Left color sensor
colorA = ColorSensor("A")
leftColorSensor = colorA #Easier alias to use in code

_CM_PER_INCH = 2.54

testX2 = [10]
testY2 = [10]

# This is based on emperical tests and by looking at the color sensor.
# This is also based on the new sensor mount which roughly puts the sensor
# at about 18-20mm of the ground.
BLACK_COLOR = 20
WHITE_COLOR = 90

def driverWithFewerArms():
    counter = 1
    arm_change_end_time = 0
    arm_change_start_time = 0
    while True:
        if counter == 7: 
            break
        # Skip printing for the first time the loop runs.
        if (counter != 1):
            arm_change_start_time = time.ticks_ms()
            logMessage("Waiting for arm change", level=0)

        primeHub.speaker.beep(90, 1)
        primeHub.right_button.wait_until_pressed()
        if (counter != 1):
            arm_change_end_time = time.ticks_ms()      
            logMessage("Time for arm change time(ms): {}".format(str(time.ticks_diff(arm_change_end_time, arm_change_start_time))), level=0)

        if counter == 1:
            doRunWithTiming(_run1)
        if counter == 2:
            doRunWithTiming(_run2)
        if counter == 3:
            doRunWithTiming(_run3)
        if counter == 4:
            doRunWithTiming(_run4)
        if counter == 5:
            doRunWithTiming(_run5)
        if counter == 6:
            doRunWithTiming(_run6)
        counter = counter + 1

#region Utilities
def _initialize(): 
    print("___________________________________________________")
    global TOTAL_DEGREES_TURNED
    TOTAL_DEGREES_TURNED = 0
    primeHub.motion_sensor.reset_yaw_angle()
    wheels.set_stop_action("brake")
    wheels.set_motor_rotation(2*3.14*WHEEL_RADIUS_CM, 'cm')
    isBatteryGood()

def resetTotalDegreesTurned():
    global TOTAL_DEGREES_TURNED
    TOTAL_DEGREES_TURNED = 0

def getyawangle():
    return primeHub.motion_sensor.get_yaw_angle()
    
def measureColor():
    while(True):
        primeHub.right_button.wait_until_pressed()
        sumLeftColor = 0
        sumRightColor = 0
        counter = 1
        while(counter < 200):
            left_light = colorA.get_reflected_light()
            right_light = colorB.get_reflected_light()
            sumLeftColor += left_light
            sumRightColor += right_light
            counter = counter + 1
        
        avgLeftColor = sumLeftColor / counter
        avgRightColor = sumRightColor / counter
        logMessage("Left color={} Right Color={}".format(str(avgLeftColor), str(avgRightColor)), level=0)
            
def doRunWithTiming(run):
    logMessage("Starting run {}".format(str(run)), level=0)
    start_time = time.ticks_ms()  
    run()
    end_time = time.ticks_ms()
    logMessage("Time for run {} time(ms): {}".format(str(run), str(time.ticks_diff(end_time, start_time))), level=0)

def logMessage(message = "", level=1):
    """
    level: parameter between 1-5. 5 is the most detailed level.

    Prints the message that is passed to the function
    The printing is controlled by the level parameter.
    The function will only print if the passed level is higher than the global level.
    If the global level is set to zero nothing will print.
    """
    if (level <= GLOBAL_LEVEL):
        print(message)
   

def moveArm(degrees = 0, speed = 0, motor = motorD):
    """
    MoveArm Information:
    - Purpose - MoveArm turns the specified amount of degrees
    - Parameters: Degrees(Int), Speed(Int), Motor(motorD or motorF)
    - Issues: None known
    """
    startDegrees = motor.get_degrees_counted()
    currentDegrees = motor.get_degrees_counted()
    motor.start_at_power(speed)
    while abs(currentDegrees - startDegrees) < abs(degrees):
        currentDegrees = motor.get_degrees_counted()
        
    motor.stop()


def correctedGyroAngleZeroTo360():
    """
        Returns a number between 0-360. Note that it will not return 180 because the yaw angle is never 180.
    """
    yaw = getyawangle()
    if (yaw < 0):
        return 360 + yaw
    else:
        return yaw

def gyroAngleZeroTo360():
        """
        Returns a number between 0-360. Note that it will not return 180 because the yaw angle is never 180.
        """
        yaw = primeHub.motion_sensor.get_yaw_angle()
        if (yaw < 0):
            return 360 + yaw
        else:
            return yaw

def calculateReducedTargetAngleAndCorrection(angle, correction):
    if correction == 0:
        return calculateReducedTargetAngle(angle), 0
    else:
        return angle, correction


def calculateReducedTargetAngle(angle):
    '''
    angle : between -179 and + 179
    '''
    global TOTAL_DEGREES_TURNED
    currentAngle = gyroAngleZeroTo360()

    anglein360 = angle
    if (angle < 0):
        anglein360 = angle + 360
    
    # Compute whether the left or the right
    # turn is smaller.
    degreesToTurnRight = 0
    degreesToTurnLeft = 0
    if (anglein360 > currentAngle):
        degreesToTurnRight = anglein360 - currentAngle
        degreesToTurnLeft = (360-anglein360) + currentAngle
    else:
        degreesToTurnLeft = currentAngle - anglein360
        degreesToTurnRight = (360-currentAngle) + anglein360
     
    def _calculatecorrection(degreesToTurn):
        global TOTAL_DEGREES_TURNED
        # Adjust the global degrees turned
        TOTAL_DEGREES_TURNED += degreesToTurn
    
        # Reduce the angle to turn based on correction.
        if (abs(degreesToTurn) <= 60):
            percentageToCorrect = 50-(0.73*abs(degreesToTurn))
            return (-1*degreesToTurn * percentageToCorrect) / 100
        elif (abs(degreesToTurn) <= 90):
            percentageToCorrect = 13.32 - (0.12*abs(degreesToTurn))
            return (-1*degreesToTurn * percentageToCorrect) / 100
        else:
            percentageToCorrect = 2.5
            return (-1*degreesToTurn * percentageToCorrect) / 100

        # Use this function if using Amogh's robot.
        return int((-1 * 0.025 * TOTAL_DEGREES_TURNED)) 

    degreesToTurn = 0
    if (degreesToTurnLeft < degreesToTurnRight):
        degreesToTurn = degreesToTurnLeft * -1  
    else:
        degreesToTurn = degreesToTurnRight
    
    degreesToCorrect = _calculatecorrection(degreesToTurn)
    reducedTargetAngle = angle + degreesToCorrect
    
    # Switch the reduced target angle to the proper -179 to + 179 space.
    if (reducedTargetAngle > 180):
        reducedTargetAngle = reducedTargetAngle - 360
    
    if (reducedTargetAngle < -180):
        reducedTargetAngle = 360 + reducedTargetAngle

    if reducedTargetAngle == 180:
        reducedTargetAngle = 179

    if reducedTargetAngle == -180:
        reducedTargetAngle = -179

    logMessage("currentAngle={} angleIn360={} angle={} reducedTargetAngleIn179Space={} TOTAL_DEGREES_TURNED={}".format(
        str(currentAngle),str(anglein360),str(angle), str(reducedTargetAngle),str(TOTAL_DEGREES_TURNED),str()))
    return  int(reducedTargetAngle)


def flushForTime(speed=30, timeInSeconds=2):
    wheels.start(steering=0, speed=speed)
    wait_for_seconds(timeInSeconds)
    wheels.stop()
    
def _turnToAngle(targetAngle, speed=20, forceTurn="None", slowTurnRatio=0.4, correction=0.05, oneWheelTurn="None"):
    """Turns the robot the specified angle.
    It calculates if the right or the left turn is the closest
    way to get to the target angle. Can handle both negative 
    targetAngle and negative gyro readings.
    targetAngle -- the final gyro angle to turn the robot to. This should be between -179 and +179
    speed -- the speed to turn.
    forceTurn -- Can be "None", "Right" or "Left" strings, forcing
    the robot to turn left or right independent of the shortest 
    path.
    slowTurnRatio -- A number between 0.1 and 1.0. Controls the 
    amount of slow turn. If set to 1.0 the entire turn is a slow turn
    the default value is 0.2, or 20% of the turn is slow.
    correction -- The correction value in ratio. If its set to 0.05, we are going to 
    addjust the turnAngle by 5%, if you dont want any correction set it to 0
    oneWheelTurn -- "Left", "Right" or "None"(default). Useful if one of your wheels is in perfect
    position and you just want the robot to turn with the other wheel

    Note about the algorithm. There are three angle spaces involved in this algo.
    1. Spike prime gyro angles: -179 to +179. This is the input targetAngle and also the readings from the gyro.
    2. Spike prime 0-360 space. We first convert spike prime gyro angles to 0-360 
       (this is because its easier to think in this space)
    """
    #logMessage("TurnToAngleStart current_angle={} targetAngle={}".format(str(getyawangle()), targetAngle), level=4)
    wheels.stop()
    currentAngle = gyroAngleZeroTo360()
    
    if (targetAngle < 0):
        targetAngle = targetAngle + 360
    
    # Compute whether the left or the right
    # turn is smaller.
    degreesToTurnRight = 0
    degreesToTurnLeft = 0
    if (targetAngle > currentAngle):
        degreesToTurnRight = targetAngle - currentAngle
        degreesToTurnLeft = (360-targetAngle) + currentAngle
    else:
        degreesToTurnLeft = currentAngle - targetAngle
        degreesToTurnRight = (360-currentAngle) + targetAngle
     
    degreesToTurn = 0
    direction = "None"
    if (forceTurn == "None"):
        if (degreesToTurnLeft < degreesToTurnRight):
            degreesToTurn = degreesToTurnLeft * -1
            direction = "Left"
        else:
            degreesToTurn = degreesToTurnRight
            direction = "Right"
    elif (forceTurn == "Right"):
        degreesToTurn = degreesToTurnRight
        direction = "Right"
    elif (forceTurn == "Left"):
        degreesToTurn = degreesToTurnLeft * -1
        direction = "Left"

    # Use the correction to correct the target angle and the degreesToTurn
    # note that the same formula is used for both left and right turns
    # this works because the degreesToTurn is +ve or -ve based
    # on which way we are turning.
    reducedTargetAngle = targetAngle
    if (correction != 0):
        if (abs(degreesToTurn) > 20):
            reducedTargetAngle = targetAngle - (degreesToTurn * correction)
            degreesToTurn = degreesToTurn * (1-correction)

    # Put the target angle back in -179 to 179 space.    
    reducedTargetAngleIn179Space = reducedTargetAngle
    # Changed from targetAngle to reducedTargetAngle as it goes into loop
    if (reducedTargetAngleIn179Space >= 180):
        reducedTargetAngleIn179Space = reducedTargetAngle - 360

    _turnRobotWithSlowDown(degreesToTurn, reducedTargetAngleIn179Space, speed, slowTurnRatio, direction, oneWheelTurn=oneWheelTurn)    
    currentAngle = correctedGyroAngleZeroTo360()
    #logMessage("TurnToAngle complete. GyroAngle:{} reducedtargetAngle(0-360):{} ".format(str(getyawangle()), str(reducedTargetAngleIn179Space)), level=4)

def _turnRobotWithSlowDown(angleInDegrees, targetAngle, speed, slowTurnRatio, direction, oneWheelTurn="None"):
    """
    Turns the Robot using a fast turn loop at speed and for the slowTurnRatio
    turns the robot at SLOW_SPEED.

    angleInDegrees -- Angle in degrees to turn. Can be +ve or -ve.
    targetAngle -- targetAngle should be in the -179 to 179 space
    speed -- Fast turn speed. 
    slowTurnRatio -- This is the % of the turn that we want to slow turn.
                     For example 0.2 means that 20% of the turn we want
                     to slow turn.
    oneWheelTurn -- Optional parameter with "None" as the default. Values can be "Left", "Right", "None".
    """
    SLOW_SPEED = 10
    currentAngle = getyawangle()
    
    # First we will do a fast turn at speed. The amount to turn is 
    # controlled by the slowTurnRatio.
    _turnRobot(direction, speed, oneWheelTurn)
    fastTurnDegrees =  (1 - slowTurnRatio) * abs(angleInDegrees)
    while (abs(currentAngle - targetAngle) > fastTurnDegrees):
        currentAngle = getyawangle()

    # After the initial fast turn that is done using speed, we are going to do a 
    # slow turn using the slow speed.
    _turnRobot(direction, SLOW_SPEED, oneWheelTurn)
    while (abs(currentAngle - targetAngle) > 1):
        currentAngle = getyawangle()

    wheels.stop()

def _turnRobotWithSlowDownAndStallDetection(angleInDegrees, targetAngle, speed, slowTurnRatio, direction, oneWheelTurn="None", expected_time=2):
    """
    Turns the Robot using a fast turn loop at speed and for the slowTurnRatio
    turns the robot at SLOW_SPEED.

    angleInDegrees -- Angle in degrees to turn. Can be +ve or -ve.
    targetAngle -- targetAngle should be in the -179 to 179 space
    speed -- Fast turn speed. 
    slowTurnRatio -- This is the % of the turn that we want to slow turn.
                     For example 0.2 means that 20% of the turn we want
                     to slow turn.
    oneWheelTurn -- Optional parameter with "None" as the default. Values can be "Left", "Right", "None".
    """
    SLOW_SPEED = 10
    currentAngle = getyawangle()
    
    # First we will do a fast turn at speed. The amount to turn is 
    # controlled by the slowTurnRatio.
    start_time = time.ticks_ms()      
    _turnRobot(direction, speed, oneWheelTurn)
    fastTurnDegrees =  (1 - slowTurnRatio) * abs(angleInDegrees)
    while (abs(currentAngle - targetAngle) > fastTurnDegrees) and (current_time - start_time) > expected_time:
        currentAngle = getyawangle()
        current_time = time.ticks_ms()

    # After the initial fast turn that is done using speed, we are going to do a 
    # slow turn using the slow speed.
    _turnRobot(direction, SLOW_SPEED, oneWheelTurn)
    while (abs(currentAngle - targetAngle) > 1):
        currentAngle = getyawangle()

    wheels.stop()

def _turnRobot(direction, speed, oneWheelTurn):
    if (oneWheelTurn == "None"):
        if (direction == "Right"):
            wheels.start_tank(speed, speed * -1)
        if (direction == "Left"):
            wheels.start_tank(speed * -1, speed)
    elif (oneWheelTurn == "Left"):
        left_large_motor.start(speed)
    else:
        right_large_motor.start(speed)

def gyroStraight(distance, speed = 20, backward = False, targetAngle = 0, multiplier=1.0, gradualAcceleration=True, slowDown=True):
    #logMessage("=========== GyroStraight Start distance={} current_angle={} targetAngle={}".format(str(distance), str(getyawangle()),str(targetAngle)), level=4)
    correctionMultiplier = multiplier
    initialDeg = abs(motorE.get_degrees_counted())
    if(distance < _CM_PER_INCH*3):
        _gyroStraightNoSlowDownNoStop(distance = distance, speed = 20, targetAngle=targetAngle, backward=backward, correctionMultiplier = correctionMultiplier)
        wheels.stop()
        return
    
    gradualAccelerationDistance = 0
    slowDistance = 0
    if slowDown == True:
        slowDistance = 0.2 * distance
        if(slowDistance > _CM_PER_INCH*2):
            slowDistance = _CM_PER_INCH*2

    # Run slow if the gradual acceleration is on.    
    if gradualAcceleration == True:
        gradualAccelerationDistance = _CM_PER_INCH*1
        _gyroStraightNoSlowDownNoStop(distance = gradualAccelerationDistance, speed = 20, targetAngle=targetAngle, backward=backward, correctionMultiplier = correctionMultiplier)
    
    # Do the middle part of the run
    _gyroStraightNoSlowDownNoStop(distance = distance - slowDistance - gradualAccelerationDistance, speed = speed, targetAngle=targetAngle, backward=backward, correctionMultiplier = correctionMultiplier)
    
    # Slow down at the end.
    if slowDown == True:
        _gyroStraightNoSlowDownNoStop(distance = slowDistance, speed = 20, targetAngle=targetAngle, backward=backward, correctionMultiplier = correctionMultiplier)

    wheels.stop()

    finalDeg = abs(motorE.get_degrees_counted())

    totalDistanceTravelled = convertDegToCM(finalDeg - initialDeg)
    #logMessage("Total distance travelled = {} error = {}".format(str(totalDistanceTravelled), str(distance-totalDistanceTravelled)), level=4)
    #logMessage("=========== GyroStraight complete distance={} current_angle={}".format(str(distance), str(getyawangle())), level=4)
    

def _gyroStraightNoSlowDownNoStop(distance, speed = 20, backward = False, targetAngle = 0, correctionMultiplier = 2):
    underBiasErrorMultiplier = 1 # 1.106
    errorAdjustedDistanceInCm = distance*underBiasErrorMultiplier

    #logMessage("GYROSTRAIGHT START: targetAngle  is {}".format(str(targetAngle)), level=4)
    degreesToCover = (errorAdjustedDistanceInCm * 360)/(WHEEL_RADIUS_CM * 2 * 3.1416)
    position_start = motorE.get_degrees_counted()
    if (backward): 
        while ((motorE.get_degrees_counted() - position_start)  >= degreesToCover * -1):
            # currentAngle = primeHub.motion_sensor.get_yaw_angle()
            correction = getCorrectionForDrive(targetAngle, correctionMultiplier = correctionMultiplier) # - currentAngle
            wheels.start(steering = -correction, speed=speed * -1)
    else:
         while ((motorE.get_degrees_counted() - position_start)  <= degreesToCover):           
            # currentAngle = primeHub.motion_sensor.get_yaw_angle()
            correction = getCorrectionForDrive(targetAngle, correctionMultiplier = correctionMultiplier)
            wheels.start(steering = correction, speed=speed)   

def _turnToAngle2(targetAngle, speed=20, forceTurn="None", slowTurnRatio=0.4, correction=0.05, oneWheelTurn="None"):
    degreesToTurn = getCorrectionForDrive(targetAngle=targetAngle, correctionMultiplier=1)
    motorDegToTurn = getMotorRotationDegreesForTurn(degreesToTurn=abs(degreesToTurn), oneWheelTurn=oneWheelTurn)
    # print("Deg to turn = " + str(motorDegToTurn))
    if(degreesToTurn < 0):
        direction = "Left"
    else:
        direction = "Right"
    turnForMotorRotations(degreesOfRotation=motorDegToTurn, direction=direction, speed=speed, oneWheelTurn=oneWheelTurn)
    
def getMotorRotationDegreesForTurn(degreesToTurn, oneWheelTurn="None"):
    motorRotationDegrees = degreesToTurn*(AXLE_DIAMETER_CM_CORRECTED / (2*WHEEL_RADIUS_CM)) # (2πr_Axle/360) * degreesToTurn * (360/2πr_Wheel)
    if(oneWheelTurn != "None"):
        motorRotationDegrees = 2*motorRotationDegrees
    return motorRotationDegrees

def turnForMotorRotations(degreesOfRotation, direction, speed=40, oneWheelTurn="None"):
    position_start_right = right_large_motor.get_degrees_counted()
    position_start_left = left_large_motor.get_degrees_counted()
    
    leftSpeed = 0
    rightSpeed = 0
    turnLeftRemaining = 0
    turnRightRemaining = 0
    if(direction == "Left"):
        if(oneWheelTurn == "Left" or oneWheelTurn == "None"):
            leftSpeed = speed
            turnLeftRemaining = degreesOfRotation
            # print("Left Turn: Right speed=" + str(rightSpeed) + ", Left Remaining=" + str(turnRightRemaining))
        if(oneWheelTurn == "Right" or oneWheelTurn == "None"):
            rightSpeed = speed
            turnRightRemaining = degreesOfRotation
            # print("Left Turn: Right speed=" + str(rightSpeed) + ", Right Remaining=" + str(turnRightRemaining))
    if(direction == "Right"):
        if(oneWheelTurn == "Left" or oneWheelTurn == "None"):
            leftSpeed = -1*speed
            turnLeftRemaining = degreesOfRotation
            # print("Right Turn: Left speed=" + str(leftSpeed) + ", Left Remaining=" + str(turnLeftRemaining))
        if(oneWheelTurn == "Right" or oneWheelTurn == "None"):
            rightSpeed = -1*speed
            turnRightRemaining = degreesOfRotation
            # print("Right Turn: Right speed=" + str(rightSpeed) + ", Right Remaining=" + str(turnRightRemaining))


    allowedError = 4 * pow(2, int(speed/10)-1) # Picked after some ad hoc testing for different speeds
    # print("Start positions: Left=" + str(position_start_left) + ", Right=" + str(position_start_right))
    while(abs(turnLeftRemaining) > allowedError or abs(turnRightRemaining) > allowedError):
        # print("left: " + str(turnLeftRemaining) + ", right: " + str(turnRightRemaining))
        if(abs(turnLeftRemaining) > allowedError):
            left_large_motor.start(speed=leftSpeed) #degrees = turnLeftRemaining, speed=20)
            turnLeftRemaining = position_start_left + (leftSpeed/abs(leftSpeed))*degreesOfRotation - left_large_motor.get_degrees_counted()
        else:
            left_large_motor.stop()
        if(abs(turnRightRemaining) > allowedError):
            right_large_motor.start(speed=rightSpeed) #degrees = -1*turnRightRemaining, speed=20)
            turnRightRemaining = position_start_right + (rightSpeed/abs(rightSpeed))*degreesOfRotation - right_large_motor.get_degrees_counted()
        else:
            right_large_motor.stop()
    left_large_motor.stop()
    right_large_motor.stop()


    # if (backward): 
    #     while ((motorE.get_degrees_counted() - position_start)  >= degreesToCover * -1):
           
    #         # currentAngle = primeHub.motion_sensor.get_yaw_angle()
    #         correction = getCorrectionForDrive(targetAngle, correctionMultiplier = correctionMultiplier) # - currentAngle
    #         wheels.start(steering = -correction, speed=speed * -1)
    # else:
    #      while ((motorE.get_degrees_counted() - position_start)  <= degreesToCover):
           
    #         # currentAngle = primeHub.motion_sensor.get_yaw_angle()
    #         correction = getCorrectionForDrive(targetAngle, correctionMultiplier = correctionMultiplier) # targetAngle - currentAngle
    #         wheels.start(steering = correction, speed=speed)

def getCorrectionForDrive(targetAngle, correctionMultiplier = 2):
    currentAngle = getyawangle()
    #primeHub.motion_sensor.get_yaw_angle()
    #logMessage("CurrentAngle: " + str(currentAngle) + " and targetAngle: " + str(targetAngle), 5)
    if( (currentAngle <= 0 and targetAngle <=0) or
            (currentAngle>=0 and targetAngle > 0) or
            (abs(currentAngle) <= 90 and abs(targetAngle)<=90)):
        correction = targetAngle - currentAngle
    elif (currentAngle >= 90):
        correction = (360 - abs(currentAngle) - abs(targetAngle))
    else:
        correction = -1*(360 - abs(currentAngle) - abs(targetAngle))

    return int(correction * correctionMultiplier)

def _turnAndDrive(targetAngle, distance, speed):
    #angle = targetAngle
    angle = calculateReducedTargetAngle(targetAngle)
    _turnToAngle(targetAngle = angle, speed = 25, correction=0)
    if distance != 0:
        gyroStraight(distance=distance, speed = speed, backward = False, targetAngle = angle)

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

def _driveTillLine(speed, distanceInCM, target_angle, gain = 1, colorSensorToUse="Left", blackOrWhite="Black", slowSpeedRatio = 0.6, distanceOnlyMode=False):
    """
    Drive
    _____
    This function drives the robot FORWARD using the motion sensor and the 80-20 formula.
    80% of distance at speed
    20% of distance with FINAL_SLOW_SPEED
    _____
    Speed - Speed the wheels travel at. Integer from -100 to 100
    DistanceInCM - Distance to travel in centimeters. Integer greater than 0
    TargetAngle - The angle the robot should drive at. Integer from 0 to 360
    Gain - The multiplier off the error. Integer greater than 0
    colorSensorToUse - "Left" or "Right". 
    blackOrWhite - "Black" or "White".
    distanceOnlyMode - Use this parameter when writing this function. You can set
                this to True, and then check that the distance you send to this
                function is correct by looking at the robot distance travelled.
    """
    wheels.stop()
   
    #logMessage("driveStraight for distance:{} target angle:{}".format(str(distanceInCM), str(target_angle)), level=2)
    initialDeg = abs(motorC.get_degrees_counted())
    remainingDistance = distanceInCM
    
    # First establish which color sensor to use.
    colorSensor = None
    if (colorSensorToUse == "Left"):
        colorSensor = colorA
    else:
        colorSensor = colorB

    # Now establish the termination condition to use.
    stoppingCondition = None
    if (blackOrWhite == "Black"):
        def blackStoppingCondition():
            light = colorSensor.get_reflected_light()
            return light <= BLACK_COLOR
        stoppingCondition = blackStoppingCondition
    elif (blackOrWhite == "White"):
        def whiteStoppingCondition():
            light = colorSensor.get_reflected_light()
            return light >= WHITE_COLOR
        stoppingCondition = whiteStoppingCondition
    elif (blackOrWhite == "Green"):
        stoppingCondition = lambda: colorSensor.get_color() == 'green'
    
    # If we are in the distance only mode, then set the stopping condition
    # to be only about distance.
    if (distanceOnlyMode == True):
        stoppingCondition = lambda: False

    FINAL_SLOW_SPEED=10
    # If the distance is small, then just drive over that distance at FINAL_SLOW_SPEED.
    if (distanceInCM < 5):
        reachedStoppingCondition = _driveStraightWithSlowDownTillLine(distanceInCM, FINAL_SLOW_SPEED, target_angle, gain, slowDown=False, reachedStoppingCondition=stoppingCondition)    
    else:
        # First drive 60% of the distance at speed
        distance60 = distanceInCM * slowSpeedRatio
        reachedStoppingCondition = _driveStraightWithSlowDownTillLine(distance60, speed, target_angle, gain, slowDown=False, reachedStoppingCondition=stoppingCondition)
        if reachedStoppingCondition == False:
            # Drive the remaining distance at slow speed
            distanceTravelled = convertDegToCM(abs(motorC.get_degrees_counted()) - initialDeg)
            remainingDistance = distanceInCM - distanceTravelled
            #logMessage("_driveTillLine: Distance travelled after first part = {} error={}".format(str(distanceTravelled),str(distanceTravelled-distance60)), level=4)
            reachedStoppingCondition = _driveStraightWithSlowDownTillLine(remainingDistance, FINAL_SLOW_SPEED, target_angle, gain, slowDown=False, reachedStoppingCondition=stoppingCondition)

    wheels.stop()
    finalDeg = abs(motorC.get_degrees_counted())

    totalDistanceTravelled = convertDegToCM(finalDeg - initialDeg)
    #logMessage("_driveTillLine: Total distance travelled={} error={}".format(str(totalDistanceTravelled), str(totalDistanceTravelled-distanceInCM)), level=2)
    return reachedStoppingCondition
    
def _driveStraightWithSlowDownTillLine(distance, speed, target_angle, gain, slowDown, reachedStoppingCondition):
    """
    Drive Straight
    ______________
    This is a internal function do not call directly. Call drive instead.

    The algorithm goes from speed to speed 10 until distance is travelled.
    slowDown: True if you want to slow down over the distance. Note that
    the function uses a combination of distance and the reachedStoppingCondition
    checks to stop.

    reachedStoppingCondition: This is a function that does not take any parameter and is expected to retur true when the loop should be terminated.
    return the output of the stoppingCondition.
    """
    startDistanceInDeg = abs(motorC.get_degrees_counted())
    #logMessage("startDistanceInDeg={}".format(str(int(startDistanceInDeg))), level=5)
    distanceInDeg = converCMToDeg(distance)
    currentSpeed = speed

    if (target_angle == -180):
        target_angle = 180

    # Drop the speed from speed to five in distanceInDeg.
    distanceInDegTravelled = 0
    
    FINAL_SLOW_SPEED=15
    wheels.start(0, int(currentSpeed))
    correction = previousCorrection = 0
    stopCondition = False
    while  distanceInDegTravelled <= distanceInDeg and stopCondition == False:
        if (slowDown == True):
            currentSpeed = currentSpeed-1
            if(currentSpeed < 15):
                currentSpeed = 15
       
        current_yaw_angle = primeHub.motion_sensor.get_yaw_angle()

        # This hackery is needed to handle 180 or -180 straight run.
        if (target_angle == 180 and current_yaw_angle < 0):
            current_yaw_angle = (360 + current_yaw_angle)

        previousCorrection = correction
        correction = target_angle - current_yaw_angle
        
        turn_rate = correction * gain
        #logMessage("Left color={} Right color={} currrentSpeed={} distanceInDegTravelledInCM={} distanceInCM={} distanceInDegTravelled={} distanceToTravelInDeg={} target_angle={} current_yaw_angle={} correction={}".format(
        #    str(colorA.get_reflected_light()), str(colorB.get_reflected_light()), str(int(currentSpeed)), str(convertDegToCM(distanceInDegTravelled)), str(distance),
        #    str(distanceInDegTravelled), str(distanceInDeg), str(target_angle), str(current_yaw_angle), str(correction)), level=5)

        if (abs(correction) > 1):
            wheels.start(turn_rate, int(currentSpeed))

        distanceInDegTravelled = abs(motorC.get_degrees_counted()) - startDistanceInDeg
        stopCondition = reachedStoppingCondition()

    #logMessage("DrivestraightWiuthSlowDownTillLine completed", level=5)
    return stopCondition
    
def _driveBackwardTillLine(distance, speed, target_angle, colorSensorToUse="Left", blackOrWhite="Black", gain=1, useAngularCorrection=True, distanceOnlyMode=False):
    wheels.stop()
    # First establish which color sensor to use.
    colorSensor = None
    if (colorSensorToUse == "Left"):
        colorSensor = colorA
    else:
        colorSensor = colorB

    # Now establish the termination condition to use.
    stoppingCondition = None
    if (blackOrWhite == "Black"):
        def blackStoppingCondition():
            light = colorSensor.get_reflected_light()
            return light <= BLACK_COLOR
        stoppingCondition = blackStoppingCondition
    elif (blackOrWhite == "White"):
        def whiteStoppingCondition():
            light = colorSensor.get_reflected_light()
            return light >= WHITE_COLOR
        stoppingCondition = whiteStoppingCondition
    elif (blackOrWhite == "Green"):
        stoppingCondition = lambda: colorSensor.get_color() == 'green'

    if distanceOnlyMode == True:
        stoppingCondition = lambda: False

    startDistanceInDeg = abs(motorC.get_degrees_counted())
    distanceInDeg = converCMToDeg(distance)
    currentSpeed = -1*speed

    if (target_angle == -180):
        target_angle = 180

    # Drop the speed from speed to five in distanceInDeg.
    distanceInDegTravelled = 0
    
    FINAL_SLOW_SPEED=15
    wheels.start(0, int(currentSpeed))
    stopCondition = False
    while  distanceInDegTravelled <= distanceInDeg and stopCondition == False:
        
        if useAngularCorrection == True:
            current_yaw_angle = primeHub.motion_sensor.get_yaw_angle()

            # This hackery is needed to handle 180 or -180 straight run.
            if (target_angle == 180 and current_yaw_angle < 0):
                current_yaw_angle = (360 + current_yaw_angle)
            correction = target_angle - current_yaw_angle
            
            turn_rate = -1 * correction * gain
            if (abs(correction) > 1):
                wheels.start(turn_rate, int(currentSpeed))
        
        distanceInDegTravelled = abs(motorC.get_degrees_counted()) - startDistanceInDeg
        stopCondition = stoppingCondition()
    wheels.stop()
    #logMessage("DrivestraightWiuthSlowDownTillLine completed", level=5)
    
    return stopCondition
    
def isGyroGood():
    """
    Is Gyro Good
    ____________
    This function checks if the gyro is drifting or not. If it is not, then is returns true.
    Otherwise, it returns false and plays a beep noise.
    ____________
    It is recommended to use this function BEFORE the match, as it takes ~ 6 seconds to complete.
    """
    
    angle1 = primeHub.motion_sensor.get_yaw_angle()
    time.sleep(5)
    angle2 = primeHub.motion_sensor.get_yaw_angle()

    if abs(angle1 - angle2) > 2:
        primeHub.speaker.beep(60, 1)
        print("Please reset gyro")
        return False
    
    return True
   

def isBatteryGood():
    
    logMessage("Battery voltage: " + str(hub.battery.voltage()), level=1)
    
    if hub.battery.voltage() < 7600:
        primeHub.speaker.beep(120, 1)
        print("Please recharge robot")
        return False

    return True
   
def wait_until_either_color(sensor1, sensor2, color, message):
    while True:
        if((color == "black" and (sensor1.get_reflected_light() <= BLACK_COLOR or sensor2.get_reflected_light() <= BLACK_COLOR)) or (color == "white" and (sensor1.get_reflected_light() >= WHITE_COLOR or sensor2.get_reflected_light() >= WHITE_COLOR))):
            #logMessage(message, level=1)
            return

def wait_until_both_color(sensor1, sensor2, color, message):    
    while True:
        if((color == "black" and (sensor1.get_reflected_light() <= BLACK_COLOR and sensor2.get_reflected_light() <= BLACK_COLOR)) or (color == "white" and (sensor1.get_reflected_light() >= WHITE_COLOR and sensor2.get_reflected_light() >= WHITE_COLOR))):
                #logMessage(message, level=1)
                return

def wait_until_color(sensor, color, message):
    while(True):
        if ((color == "black" and sensor.get_reflected_light() <= BLACK_COLOR) or (color == "white" and  sensor.get_reflected_light() >= WHITE_COLOR)):
            #logMessage(message, level=1)
            wheels.stop()
            return


 # ------------------------------------------------------------------- End Utilities --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 #endregion

#region Arisha
def _run5():
    primeHub.motion_sensor.reset_yaw_angle()

    getToOilPlatform_v2Point2()
    activeOilPlatform()
    goBackHomeFromOilPlatform()

    # pullTruckGoStraight()

def getToOilPlatform_v2Point2():
    #print("Running now getToOilPlatform")
    #working version1
    gyroStraight(distance=_CM_PER_INCH*16.8, speed=60, targetAngle=0) #was 90
    # time.sleep(5)
    _turnToAngle(45)
    # time.sleep(5)
    gyroStraight(distance=_CM_PER_INCH*3, speed=60, targetAngle=45) #was 90
    _driveTillLine(speed = 30, distanceInCM = _CM_PER_INCH*6, target_angle = 45, blackOrWhite="White") # was 12 inches ####
    #time.sleep(5)

    _turnToAngle(targetAngle=-1, oneWheelTurn="Right", speed=40)
    #time.sleep(5)
    gyroStraight(distance=_CM_PER_INCH*11.5, speed=30, targetAngle=-2) # was 10.5 ####
    #time.sleep(10)
    #motorD.start(speed=-30)
    # gyroStraight(distance=_CM_PER_INCH*9.5, speed=30, targetAngle=0) # was 10.5 ####

def activeOilPlatform():
    # gyroStraight(targetAngle = 0,  distance = _CM_PER_INCH*2.5, speed=40)
    # motorD.start(speed=-30)

    # time.sleep(10)
    for i in range(3):
        motorF.run_for_degrees(degrees=700, speed=100)
        if (i<=1):
            motorF.run_for_degrees(degrees=-700, speed=100)
        # if (i>=1):
        # motorD.start(speed=-30)
        # time.sleep(5)
    # gyroStraight(distance=2, speed=40, targetAngle=0, backward=True)
    # time.sleep(0.5)
    motorD.run_for_degrees(degrees=-1000, speed=100)

    
    wheels.move(amount = 4, unit = "in", steering = 0, speed = -40)
    # motorD.stop()
    #time.sleep(10)


def goBackHomeFromOilPlatform():
    _turnToAngle(30)
    gyroStraight(distance=24*_CM_PER_INCH, speed=100, targetAngle=30, backward=True) # Back home doesnt require accuracy
    # wheels.move(amount = 20, unit = "in", steering = 0, speed = -100) # Back home doesnt require accuracy
   #turnToAngle(30)
   #wheels.move(amount = 11, unit = "in", steering = 0, speed = -30) # Back home doesnt require accuracy

def scale(amt):
    in_min  =  BLACK_COLOR
    in_max  =  WHITE_COLOR
    out_min = -10
    out_max =  10
    return (amt - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#endregion Arisha
#region Nami    
def _newrun4withHeavyArm():
    primeHub.motion_sensor.reset_yaw_angle()
    angle = 0
    #Lift arm
    moveArm(degrees = 120, speed = -75, motor = motorF)
    #Go forward towards the hydrodam
    gyroStraight(distance = 27,speed = 50, targetAngle = angle)

    motorF.start_at_power(50)
    wait_for_seconds(0.3)
    motorF.stop()
    #Hit the black part of hydrodam
    #moveArm(degrees = 75, speed = 100, motor = motorF)
    #Move the arm back up so the energy unit can fall out
    moveArm(degrees = 75, speed = -100, motor= motorF)
    # This is needed to let the energy unit fall out from hydrodam
    time.sleep_ms(500)
    #Move arm back down to bring the water unit and energy unit home
    moveArm(degrees = 120, speed = 75,motor = motorF)
     #Go back home
    gyroStraight(distance = 30, speed = 50, backward = True, targetAngle = angle)

def _run4():
    # This is the new run3 with just doing the hydrodam. 
    # It picks the water unit in front of hydrodam and brings back the hydrodam unit.

    primeHub.motion_sensor.reset_yaw_angle()
    angle = 0
    #Lift arm
    moveArm(degrees = 120, speed = -75, motor = motorF)
    #Go forward towards the hydrodam
    gyroStraight(distance = 27,speed = 50, targetAngle = angle)
    #Hit the black part of hydrodam
    moveArm(degrees = 110, speed = 100, motor = motorF)
    #Move the arm back up so the energy unit can fall out
    moveArm(degrees = 110, speed = -100, motor= motorF)
    # This is needed to let the energy unit fall out from hydrodam
    time.sleep_ms(500)
    #Move arm back down to bring the water unit and energy unit home
    moveArm(degrees = 120, speed = 75,motor = motorF)
    #Go back home
    gyroStraight(distance = 30, speed = 50, backward = True, targetAngle = angle)

def _run6():
    def _doSmartGrid():
        # Turn and move forward 
        angle = -90
        _turnToAngle(targetAngle = angle, speed = 30, slowTurnRatio = 0.7)
        gyroStraight(distance=6, speed = 30, backward = False, targetAngle = angle)

        # Bring down the abucket arm and keep it down till we back off.
        # This is the part that does the smart grid.
        motorD.start_at_power(100)

        # Distance changed to 6 from 4 on 1/9/2023 because it was not backing up enough
        gyroStraight(distance=6, speed = 30, backward = True, targetAngle = angle)
        motorD.stop()

        # Move forward slightly before picking up the arm
        gyroStraight(distance=1, speed = 35, backward = False, targetAngle = angle)

        # Bring up the bucket arm before doing the water units.
        motorD.start_at_power(-100)
        wait_for_seconds(0.3)
        motorD.stop()
        
    primeHub.motion_sensor.reset_yaw_angle()
    angle = 0
    
    angle = -5
    #_turnToAngle(targetAngle=angle, speed=25)
    gyroStraight(distance= 60, speed= 65, targetAngle= angle)
    
    # Turn slightly to catch the n-s line in front of the power plant
    angle = -8
    _turnToAngle(targetAngle=angle, speed=25)
    if _driveTillLine(speed=45, distanceInCM=27, target_angle=angle, colorSensorToUse="Left", blackOrWhite="Black", slowSpeedRatio=0.9) == False:
        logMessage("Run6:_run6 NOTE -----------> Missed Catching the n-s line in front of power plant", level=0)
    
    # Turn towards the power plant and then try to catch the black line running e-w line in front of the smart grid.
    angle = -95
    _turnToAngle(targetAngle = angle, speed = 25, slowTurnRatio = 0.9)

    # Drive forward to drop off the enerfy units and innovation project
    gyroStraight(distance=15, speed= 50, targetAngle= angle)

    # First bring up the buecket arm so we can pull the smart grid
    # This will also drop off the innovation project and the enerfy units.
    motorD.start_at_power(-100)
    wait_for_seconds(0.3)
    motorD.stop()

    if _driveTillLine(speed=50, distanceInCM=35, target_angle = angle, colorSensorToUse="Left", blackOrWhite="Black",slowSpeedRatio=0.4) == False:
        logMessage("Run6:_run6 NOTE -----------> Missed Catching the e-w line in front of smart grid", level=0)

    # We use the bucket arm to do the smart grid.
    _doSmartGrid()

    # Added 1/9/2023 to stop the robot from snagging on the Smart Grid
    angle = -90
    gyroStraight(speed = 25, distance = 4, backward = True, targetAngle = angle)

    # Backoff from the smart grid some more.
    #gyroStraight(distance=2, speed = 25, backward = True, targetAngle = angle)

    # Align against the hydro-electric power plant.
    angle = 133
    _turnToAngle(targetAngle = angle, speed = 25, slowTurnRatio = 0.3)
    gyroStraight(speed=25, distance=10, targetAngle=angle)

    # Drop off the water units
    motorF.start(-50)
    flushForTime(speed=25, timeInSeconds=1.5)
    motorF.start(-100)
    wait_for_seconds(1.5)
    motorF.stop()
    
    # Backoff to leave the water reservoir(This code was uncommented on 1/9/2023 to avoid the arm touching the units)
    gyroStraight(distance=10, speed = 40, backward = True, targetAngle = angle)
    
#endregion Nami

#region Rishabh

def _run1():
    def _watchTV():
        angle=0
        # Drive to Watch Television. We do this in two parts. First fast and
        # then do it slow so the energy unit does not fall off.
        gyroStraight(distance = 35, speed = 60, backward = False, targetAngle = angle)
        gyroStraight(distance = 6, speed = 20, backward = False, targetAngle = angle)
        
        # Backup from Watch Television
        gyroStraight(distance = 8, speed = 50, backward = True, targetAngle =angle)

    def _getToWindTurbine():
        turnspeed = 30
        angle = -28    
        _turnToAngle(targetAngle = angle, speed = turnspeed, slowTurnRatio = 0.9, correction=0.16)

        # We should have turned such that we are able to find the black line in front of the wind turbine.
        if (_driveTillLine(speed=60, distanceInCM=30, target_angle=angle, colorSensorToUse="Right", blackOrWhite="Black", slowSpeedRatio=0.9) == False):
            logMessage("NOTE -----------> Missed Catching the line before wind turbine", level=0)
        gyroStraight(distance = 6, speed = 20, backward = False, targetAngle = angle)

        # After catching the black line, drive forward and turn to face the windmill
        angle=40
        _turnToAngle(targetAngle = angle, speed = turnspeed, slowTurnRatio = 0.9, correction=0.16)

    def _windTurbine():
        angle = 40
        gyroStraight(distance=20, speed = 20, backward = False, targetAngle = angle)

        # Push the lever the remaining two times
        for i in range(3): 
            # Backup so the robot can push the Wind Turbine again
            gyroStraight(distance=6, speed = 30, backward = True, targetAngle = angle)
            # Drive forward to push the Wind Turbine
            #flushForTime(speed=20, timeInSeconds=0.6)
            gyroStraight(distance=9, speed = 20, backward = False, targetAngle = angle)

    def _pickUpRechargeableBattery():
        turnspeed = 35
        # Backoff from the windwill and flush against the rechargeable battery.
        # We go back fast first, and then slow down to flush.
        
        # First back off a little to be able to turn.
        angle = 40
        gyroStraight(distance=10, speed = 55, backward = True, targetAngle = angle)

        _turnToAngle(targetAngle = angle, speed = turnspeed)
        gyroStraight(distance=5, speed = 45, backward = True, targetAngle = angle)
        
        # Flush against the toy factory
        _turnToAngle(targetAngle = angle, speed = turnspeed)
        #gyroStraight(distance=6, speed = 35, backward = True, targetAngle = angle)
        flushForTime(speed=-35, timeInSeconds=0.5)
        
    def _goHome():
        # Backoff from the toy factory to be able to turn
        angle = 40
        gyroStraight(distance=2, speed = 40, backward = False, targetAngle = angle)

        angle = 135
        _turnToAngle(targetAngle = angle, speed = 35, slowTurnRatio = 0.9)
        gyroStraight(distance=70, speed = 100, backward = False, targetAngle = angle)

        #angle = -70
        #_turnToAngle(targetAngle = angle, speed = 25, slowTurnRatio = 0.6)
        #gyroStraight(distance=35, speed = 80, backward = True, targetAngle = angle)

    #moveArm(degrees = 150, speed = 50, motor = motorD)
    primeHub.motion_sensor.reset_yaw_angle()
    _watchTV()
    _getToWindTurbine()
    _windTurbine()
    _pickUpRechargeableBattery()
    _goHome()

#endregion
def _run3():

    def _doRechargablebattery():
        straightSpeed = 55
        angle = 0
        correction=0
        #angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
        gyroStraight(distance=35, speed=straightSpeed,targetAngle=angle,backward=False)

        angle = -40
        #angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
        _turnToAngle(targetAngle = angle, speed = 25, slowTurnRatio = 0.9)
        gyroStraight(distance=40, speed=straightSpeed,targetAngle=angle,backward=False)

        # Flush with the toy factory using the bucket.
        angle = -140
        #angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
        _turnToAngle(targetAngle = angle, speed = 25, slowTurnRatio = 0.9)
        gyroStraight(distance=7, speed=50,targetAngle=angle,backward=False)

        # This distance used to be 10, made it 14 if we are using a front attachment
        # tyo drop off units at the toy factory as part of this run.
        gyroStraight(distance=14, speed=30,targetAngle=angle,backward=False)

        # Backoff a little bit before opening the buicket.
        gyroStraight(distance=3, speed=45,targetAngle=angle,backward=True)

        # Drop off the units by lifting the bucket. 
        moveArm(degrees = 130, speed = -75, motor = motorF)

        # Backoff from the toy factory.
        gyroStraight(distance=8,speed=45,targetAngle=angle,backward=True)   

        # Drop the bucket so we have less chance of snagging.
        moveArm(degrees = 120, speed = 50, motor = motorF)

    def _doHybridCar():
        angle = -90
        # Intentionally doing a slow turn.
        _turnToAngle(targetAngle = angle, speed = 20, slowTurnRatio = 0.2)
        if _driveTillLine(speed=35, distanceInCM=45, target_angle=angle, colorSensorToUse="Left", blackOrWhite="White", slowSpeedRatio=0.6) == False:
            logMessage("Note --------------------> Missed line between hybrid car and toy factory", level=0)

        # Turn towards the hybrid car.
        angle = -42
        _turnToAngle(targetAngle = angle, speed = 20, slowTurnRatio = 0.2)
        gyroStraight(distance=12, speed = 35, backward = False, targetAngle = angle)

        # Turn towards the hybrid car before lifting the arm.
        angle = -38
        _turnToAngle(targetAngle = angle, speed = 20, slowTurnRatio = 0.9)
        
        # Lift up the hybrid car using the bucket arm.
        moveArm(degrees = 130, speed = -50, motor = motorF)
        
        # wait a little and drop the arm to allow the hybrid car to roll off.
        time.sleep(0.1)
        moveArm(degrees = 130, speed = 75, motor = motorF)

        # Turn back before backing off.
        angle = -43
        _turnToAngle(targetAngle = angle, speed = 20, slowTurnRatio = 0.9)

        # Backoff from the hybrid car.
        angle = -90
        if _driveBackwardTillLine(distance=15, speed=30,target_angle=angle, colorSensorToUse="Right", blackOrWhite="Black", gain=2) == False:
            logMessage("Note --------------------> Missed backward line catch after hybrid car", level=0)
        gyroStraight(distance=5, speed = 30, backward = True, targetAngle = angle)

    def _gotoSmartGrid():
        straightSpeed = 60
        angle=-110
        correction = 0
        angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
        _turnToAngle(targetAngle = angle, speed = 25, slowTurnRatio = 0.6, correction=correction)
        gyroStraight(distance=25,speed=straightSpeed,targetAngle=angle,backward=False)
        motorF.start_at_power(-50)
        if _driveTillLine(speed=45, distanceInCM=10, target_angle=angle, colorSensorToUse="Left", blackOrWhite="Black",slowSpeedRatio=1) == False:
            logMessage("Note --------------------> Missed n-s line in front of smart grid", level=0)
        #gyroStraight(distance=15,speed=straightSpeed,targetAngle=angle,backward=False)

    def _picktwoWaterUnits():
        # Pick up the bucket arm to be able to pick up the water units.
        #moveArm(degrees = 130, speed = -75, motor = motorF)
 
        # Turn towards the water reservoir to pick up the two water units
        angle = -110
        correction=0
        angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
        #_turnToAngle(targetAngle=angle, speed=25, slowTurnRatio=0.6, correction=correction)
        gyroStraight(distance=18, speed = 30, backward = False, targetAngle = angle)
        motorF.stop()
        
        # Drop the arm to get the water units.
        moveArm(degrees = 150, speed = 75, motor = motorF)
        angle = -90
        angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
        _turnToAngle(targetAngle=angle, speed=25, slowTurnRatio=0.4, correction=correction)
        gyroStraight(distance=8, speed = 45, backward = True, targetAngle = angle)

    def _pickSolarFarmUnitwithFlushing():
         # Now go to solar farm to pick the energy unit
        angle = 155
        _turnToAngle(targetAngle = angle, speed = 25)
        #gyroStraight(distance = 8, speed = 20, backward = True, targetAngle = angle)
        _driveBackwardTillLine(distance = 10, speed = 35, target_angle = angle, colorSensorToUse = "Right", blackOrWhite = "Black")
        gyroStraight(distance=7, speed = 35, backward = True, targetAngle = angle)

        # Collect the solar farm unit
        angle = -178
        _turnToAngle(targetAngle = angle, speed = 25)
        
        # flush with the wall, Reset the gyro after the flush.
        flushForTime(speed=-30, timeInSeconds=0.5)
        primeHub.motion_sensor.reset_yaw_angle()        

        # Now find the line in front of the smart grid.        
        angle = 0
        if _driveTillLine(speed = 35, distanceInCM = 15, target_angle = angle, colorSensorToUse = "Left", blackOrWhite = "Black") == False:
            logMessage("Note --------------------> Missed e-w line in front of solar farm grid", level=0)
           
        #gyroStraight(distance = 4, speed = 40, backward = False, targetAngle = angle)

    def _goHome():
        # Go Home
        angle = 80
        correction = 0
        angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
        _turnToAngle(targetAngle = angle, speed = 35, slowTurnRatio = 0.6, correction=correction)
        gyroStraight(distance=25, speed = 80, backward = False, targetAngle = angle, multiplier=1.0, gradualAcceleration=False, slowDown=False)

        angle = 35
        angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
        _turnToAngle(targetAngle = angle, speed = 35, slowTurnRatio = 0.6, correction=correction)
        gyroStraight(distance=80, speed = 100, backward = False, targetAngle = angle, multiplier=1.0, gradualAcceleration=False, slowDown=False)
    
    primeHub.motion_sensor.reset_yaw_angle()
    _doRechargablebattery()
    _doHybridCar()
    _gotoSmartGrid()
    _picktwoWaterUnits()
    _pickSolarFarmUnitwithFlushing()
    _goHome()

#region Function Calls
def _run2():
    primeHub.motion_sensor.reset_yaw_angle()
    # Drive to power plant.
    angle = 17
    correction = 0
    angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
    _turnToAngle(targetAngle = angle, speed = 35, slowTurnRatio = 0.6, correction=correction)
    gyroStraight(targetAngle = angle,  distance = 65, speed=60) 
    _driveTillLine(speed = 35, distanceInCM = 24, target_angle = angle, colorSensorToUse="Left", blackOrWhite="Black")
    gyroStraight(targetAngle = angle,  distance = 4, speed=25) 

    #Reached powerplant now turn towards powerplant and move forward
    angle = -90
    angle, correction = calculateReducedTargetAngleAndCorrection(angle, correction)
    _turnToAngle(targetAngle = angle, speed = 35, slowTurnRatio = 0.1, correction=correction)

    # Bring up the power plant. We do a two part attempt to open the power plant.
    # We try first to pick up the arm and then try again by going back a little.
    #moveArm(degrees = 150, speed = -75, motor = motorD)
    gyroStraight(targetAngle = angle,  distance = 16, speed=25) 
    motorD.start_at_power(75)
    wait_for_seconds(0.2)
    motorD.stop()
    
    #Bring the arm down to do power plant
    #moveArm(degrees = 120, speed = -75, motor = motorD)
    #gyroStraight(distance = 1, speed = 20, backward=True, targetAngle=angle)
    #moveArm(degrees = 175, speed = 100, motor = motorD)
    gyroStraight(distance=5, speed = 15, backward = True, targetAngle = angle)

    angle = -170
    _turnToAngle(targetAngle = angle, speed = 35, slowTurnRatio = 0.6, correction=correction)
    gyroStraight(targetAngle = angle,  distance = 90, speed=100) 

def testSmartGridArm():
    angle = -5
    if _driveTillLine(speed=30, distanceInCM=20, target_angle = angle, colorSensorToUse="Left", blackOrWhite="Black",slowSpeedRatio=0.6) == False:
        logMessage("Run6:_run6 NOTE -----------> Missed Catching the e-w line in front of smart grid", level=0)

    motorD.start_at_power(-100)
    wait_for_seconds(0.4)
    motorD.stop()
    
    # Turn and move forward 
    angle = 0
    _turnToAngle(targetAngle = angle, speed = 30, slowTurnRatio = 0.7)
    gyroStraight(distance=4, speed = 30, backward = False, targetAngle = angle)

    # Bring down the abucket arm and keep it down till we back off.
    motorD.start_at_power(100)
    gyroStraight(distance=5, speed = 30, backward = True, targetAngle = angle)
    motorD.stop()

    # Move forward slightly before picking up the arm
    gyroStraight(distance=1, speed = 35, backward = False, targetAngle = angle)
    # Bring up the bucket arm before doing the water units.
    motorD.start_at_power(-100)
    wait_for_seconds(0.4)
    motorD.stop()


# This is used for testing only.
def resetArmForRun6Testing():
    angle = 133
    gyroStraight(distance=10, speed = 40, backward = True, targetAngle = angle)

    # Bring up the water unit arm for the next run
    motorF.start(100)
    wait_for_seconds(2.3)
    motorF.stop()

    # Bring down the bucket arm for the next test
    motorD.start_at_power(100)
    wait_for_seconds(0.2)
    motorD.stop()

def TestStallDetection():
    startDegrees = motorD.get_degrees_counted()
    currentDegrees = motorD.get_degrees_counted()
    motorD.start_at_power(25)
    motorD.set_stall_detection(True)
    while abs(currentDegrees - startDegrees) < abs(150):
        currentDegrees = motorD.get_degrees_counted()
        state= motorD.was_stalled()
        #print("out: " + str(state))
        if(state == True):
            print("motorD is stalled")
            motorD.stop()
        if(motorD.was_interrupted()):
            print("motorD interrupted")

        
    motorD.stop()
   

print("Battery voltage: " + str(hub.battery.voltage())) 
_initialize()
TestStallDetection()
#doRunWithTiming(_run2)
#resetArmForRun6Testing()
#testSmartGridArm()
#driverWithFewerArms()
#resetArmForRun6Testing()
raise SystemExit
#endregion

