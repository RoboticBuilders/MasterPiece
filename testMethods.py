def testAxleLogic(degrees,speed,direction):
    print("Start Test")
    startmotorCDegrees =  motorC.get_degrees_counted()
    startmotorEDegrees = motorE.get_degrees_counted()
    print("MotorC degrees counted: " + str(startmotorCDegrees) + " motorE degrees counted: " + str(startmotorEDegrees))
    arcLengthInCM = (22*AXLE_DIAMETER_CM*degrees)/(7*360)
    toturndegrees = converCMToDeg(arcLengthInCM)

    print("Arc Length in CM: " + str(arcLengthInCM) + " toturndegrees: " + str(toturndegrees))
    if (direction == "Left"):
        motors.move_tank(toturndegrees, "degrees", speed * -1, speed)
    else:
        motors.move_tank(toturndegrees, "degrees", speed, -1 * speed)
    motors.stop()
    time.sleep(2)
    endmotorCDegrees =  motorC.get_degrees_counted()
    endmotorEDegrees = motorE.get_degrees_counted()
    print("MotorC degrees counted: " + str(endmotorCDegrees) + " motorE degrees counted: " + str(endmotorEDegrees))
    print("motorCDiff: " + str(endmotorCDegrees -startmotorCDegrees) + " motor E Diff: " + str(endmotorEDegrees - startmotorEDegrees))
    currentAngle = gyroAngleZeroTo360()
    logMessage("Axle:" + str(currentAngle) , level=3)
  
def squareTest():
    
    drive(speed = 30, distanceInCM = 30, target_angle = 0)

    turnToAngle(targetAngle = -90, speed = 30)
    drive(speed = 30, distanceInCM = 30, target_angle = -90)

    turnToAngle(targetAngle = -180, speed = 30)
    drive(speed = 30, distanceInCM = 30, target_angle = -180)

def testGyro():
    wheels.move(amount = 29, unit = "in", steering = 0, speed = 60)
    # gyroStraight(targetAngle = 0,  distance = _CM_PER_INCH*16)
    # gyroStraight(targetAngle = 0,  distance = _CM_PER_INCH*2, backward =True)
    # gyroStraight(targetAngle = 0,  distance = _CM_PER_INCH*2)
    # gyroStraight(targetAngle = 0,  distance = _CM_PER_INCH*2, backward=True)
    # gyroStraight(targetAngle = 0,  distance = _CM_PER_INCH*2)
    # gyroStraight(targetAngle = 0,  distance = _CM_PER_INCH*3, backward=True)


def testTurnToAngle(speed=20, slowturnratio = 0.4, correction=0.16):
    random.seed(5)
    targetAngle = -30
    increment = -30
    while(True):
        #targetAngle = random.randint(-178, 0)
        print("Asking turnToAngle to turn to " + str(targetAngle))
        #newturnToAngle(targetAngle=targetAngle, speed=20, forceTurn="None", slowTurnRatio=0.4, correction=0.05, oneWheelTurn="None")
        _turnToAngle(targetAngle=targetAngle, speed=speed, forceTurn="None", slowTurnRatio=slowturnratio, correction=correction, oneWheelTurn="None")
        time.sleep(10)
        targetAngle += increment

        if targetAngle < -175 and increment == -30:
            targetAngle = -175
            increment = 30

        if targetAngle > 0 and increment == 30:
            targetAngle = 0
            increment = -30

def testCoordinateSystem():
    for index in range(len(testX2)):
        robotTest = robot(0,0)
        robotTest.goto(testX2[index], testY2[index], 0, 10)


