import csv, math
from time import *
from turtle import Turtle, Screen
import os

screen = Screen()
turtle = Turtle()
screen2 = Screen()

def initializeGraphics():
    
    screen.update()
    screen.title("PathFinder: Visualization of calculated path.")
    
    screen.setup(950, 545)
    screen.setworldcoordinates(0,0,202,114)
        
    screen.mode('world')
    turtle.pen(fillcolor="black", pencolor="blue", pensize=5)
    screen.bgpic("./superpowered_darker_wireframe.GIF")
    canvas = screen.getcanvas()
    canvas.itemconfig(screen._bgpic, anchor="sw")
    screen.delay(20)
    screen.update()

class Robot:
    currentLocationX = 0
    currentLocationY = 0
    currentRobotAngle = 0
    angle = 0
    slope = 0
    distance = 0
    quadrant2 = 0

    def __init__(self,x,y):
        self.currentLocationX = x
        self.currentLocationY = y
        self.angle = 0
        self.slope = 0
        self.distance = 0
        self.quadrant2 = 0

    def addActions(self, speed, robotActions):
        robotActions.append("turnToAngle(targetAngle={}, speed={})".format(self.angle, speed))
        robotActions.append("gyroStraight(distance={}, speed={}, backward={}, targetAngle={})".format(self.distance, speed, "False", self.angle))

    def goto(self,x2,y2,endAngle,speed):
        self.angle = 0
        self.slope = 0
        self.quadrant2 = 0
        self.distance = 0
        x1 = self.currentLocationX
        y1 = self.currentLocationY
        a1 = self.currentRobotAngle

        def _calculateSlope(x1,y1,x2,y2):
            lineSlope = (y1 - y2)/(x1-x2)
            self.slope = lineSlope

        def _findQuadrant(x1,y1,x2,y2):
            greatestDistance = 0
            xDiff = x1 - x2
            yDiff = y1 - y2
            maxX = 0
            maxY = 0
            minX = 0
            minY = 0
            if abs(xDiff) > abs(yDiff):
                greatestDistance = abs(xDiff)
            if abs(yDiff) > abs(xDiff):
                greatestDistance = abs(yDiff)
            if abs(xDiff) == abs(yDiff):
                greatestDistance = abs(xDiff)
            #else:
            #    print("URGENT: Error in finding quadrants around robot.")

            maxX = x1 + greatestDistance
            minX = x1 - greatestDistance
            maxY = y1 + greatestDistance
            minY = y1 - greatestDistance
            _findEndQuadrant(x1,y1,x2,y2,maxX,maxY,minX,minY)

        def _findEndQuadrant(x1,y1,x2,y2,maxX,maxY,minX,minY):
            endQuadrant = 0
            #print(x1,y1,x2,y2,maxX,maxY,minX,minY)
            if x2 >= x1 and x2 <= maxX and y2 >= y1 and y2 <= maxY:
                endQuadrant = 1
            
            if x2 >= minX and x2 <= x1 and y2 >= y1 and y2 <= maxY:
                endQuadrant = 2
            
            if x2 >= minX and x2 <= x1 and y2 >= minY and y2 <= y1:
                endQuadrant = 3
            
            if x2 >= x1 and x2 <= maxX and y2 >= minY and y2 <= y1:
                endQuadrant = 4

            #if endQuadrant == 0:
            #    print("URGENT: Error in finding quadrant of end location")

            self.quadrant2 = endQuadrant
            
        def _calculateAngle(slope):
            lineSlope = slope
            if x1 == 0 and x2 == 0:
                self.angle = 0
            angleRadians = math.atan(lineSlope)
            angleDegrees = math.degrees(angleRadians)
            self.angle = round(angleDegrees)

        def _fixAngle(endQuadrant, rAngle):
            turnAngle = rAngle

            if endQuadrant == 1:
                turnAngle = -1 * rAngle

            if endQuadrant == 2:
                turnAngle = -90 - (90-abs(rAngle))

            if endQuadrant == 3:
                turnAngle = 90 + (90-abs(rAngle))
            
            if endQuadrant == 4:
                turnAngle = -1* rAngle 
            
            self.angle = round(turnAngle)

        def _findDistance(x1,y1,x2,y2):
            distanceToDrive = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
            self.distance = round(distanceToDrive)

        #def _move(speed):
        #    _turnToAngle(targetAngle = self.angle, speed = speed)
        #    drive(speed = speed, distanceInCM = self.distance, target_angle = self.angle)

        _findQuadrant(x1,y1,x2,y2)
        # skip the slope calculation if we are travelling vertically
        if (x1 != x2):
            _calculateSlope(x1,y1,x2,y2)
            _calculateAngle(self.slope) 
            _fixAngle(self.quadrant2, self.angle)
        else:
            if (y2 > y1):
                self.angle = -90
            else:
                self.angle = 90
        _findDistance(x1,y1,x2,y2)
        #_move(speed)
        #print(str(self.angle))
        #print(str(self.distance))
        self.currentLocationX = x2
        self.currentLocationY = y2
        #_turnToAngle(targetAngle = endAngle, speed = speed)

class Mission(object):
    def __init__(self, name, bottomLeft, topRight):
        self.name = name
        self.bottomLeft = bottomLeft
        self.topRight = topRight

    def getName(self):
        return self.name

    def getBottomLeft(self):
        return self.bottomLeft

    def getTopRight(self):
        return self.topRight

    def findClosestIntersectionPoint(self, robotLine):
        # 1. form all the four lines that the mission is made of.
        # 2. intersect the four lines with the input line
        # 3. Return the intersection point or None.
        # Also Returns whether this was a horizontal or vertical intersection.

        lines = []
        end = Point(self.topRight.getX(), self.bottomLeft.getY())
        bottomHorizontalLine = Line(self.bottomLeft, end)
        lines.append(bottomHorizontalLine)

        start = Point(self.bottomLeft.getX(), self.topRight.getY())
        topHorizontalLine = Line(start, self.topRight)
        lines.append(topHorizontalLine)

        end = Point(self.bottomLeft.getX(), self.topRight.getY())
        leftVerticalLine = Line(self.bottomLeft, end)
        lines.append(leftVerticalLine)

        start = Point(self.topRight.getX(), self.bottomLeft.getY())
        rightVerticalLine = Line(start, self.topRight)
        lines.append(rightVerticalLine)

        minDistance = 10000000
        nearestIntersection = None
        horizontal = None
        counter = 1
        for line in lines:
            intersection = line.doesIntersect(robotLine)
            if (intersection != None):
                distance = intersection.distance(robotLine.getStart())
                if (distance < minDistance):
                    minDistance = distance
                    nearestIntersection = intersection

                    # This means that we have a horizontal intersection
                    # Since the first two lines in the list are 
                    # the horizontal lines
                    if (counter < 3):
                        horizontal = True
                    else:
                        horizontal = False

            counter = counter + 1

        return nearestIntersection, horizontal

class Point(object):
    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.X = x
        self.Y = y

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, point):
        return math.sqrt(math.pow((self.X - point.getX()), 2) + math.pow((self.Y - point.getY()), 2))

    def equal(self, otherpoint):
        if (self.getX() != otherpoint.getX()):
            return False
        if (self.getY() != otherpoint.getY()):
            return False
        return True

class Line(object):
    def __init__(self, start, end):
        '''Defines start and end points'''
        self.start = start
        self.end = end
        self.isVerticalLine = False
        if (self.end.getX() - self.start.getX()) != 0:
            self.slope = (self.end.getY() - self.start.getY()) / (self.end.getX() - self.start.getX())
            self.yintercept = end.getY() - self.slope * end.getX()
        else:
            self.isVerticalLine = True
            self.yintercept = None
            self.slope = None

    def getSlope(self):
        return self.slope

    def getYIntercept(self):
        return self.yintercept

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def isVertical(self):
        return self.isVerticalLine

    def isPointOnLine(self, point):
        '''Returns true if the point is on the line and between start and end points'''
        lowX = min(self.end.getX(), self.start.getX())
        highX = max(self.end.getX(), self.start.getX())

        lowY = min(self.end.getY(), self.start.getY())
        highY = max(self.end.getY(), self.start.getY())
        
        if point.getX() >= lowX and point.getX() <= highX and point.getY() >= lowY and point.getY() <= highY:
            return True
        else:
            return False
    
    def doesIntersect(self, anotherLine):
        ''' Returns the intersection point else returns None.
        '''
        intersectionX = None
        intersectionY = None

        # This line is vertical, need to deal with this specially
        if (self.isVerticalLine == True):
            if (anotherLine.isVertical() == True):
                # Both are vertical lines and so they dont intersect.
                return None
            else:
                # This line is vertical, but the other line is not vertical
                intersectionY = (anotherLine.getSlope() * self.getStart().getX()) + anotherLine.getYIntercept()
                intersectionX = self.getStart().getX()
        # The otherline is vertical, need to deal with this specially.
        elif (anotherLine.isVertical() == True):
            intersectionY = (self.slope * anotherLine.getStart().getX()) + self.yintercept
            intersectionX = anotherLine.getStart().getX()
        else:
            l2slope = anotherLine.getSlope()
            l2YIntercept = anotherLine.getYIntercept()
            
            # Parallel lines
            if (l2slope == self.slope):
                return None

            # Solve Both Equations
            intersectionX = (self.yintercept - l2YIntercept) / (l2slope - self.slope)
            intersectionY = (((self.slope * self.yintercept) - (self.slope * l2YIntercept)) / (l2slope - self.slope)) + self.yintercept

        intersectionPoint = Point(intersectionX, intersectionY)
        if self.isPointOnLine(intersectionPoint) == False:
            return None

        if anotherLine.isPointOnLine(intersectionPoint) == False:
            return None

        return intersectionPoint

class LineTest(object):
    def __init__(self):
        return

    def runTest(self, testCase):
        print("running testCase: " + str(testCase.__name__))
        try:
            testCase()  
        except AssertionError:
            print("Test Failed")
            return
        print("Passed")

    def Test45dLines(self):
        line1 = Line(Point(0,0), Point(10,10))
        line2 = Line(Point(10,0), Point(0,10))
        expectedIntersectionPoint = Point(5,5)
        intersectionPoint = line1.doesIntersect(line2)
        assert expectedIntersectionPoint.equal(intersectionPoint) == True

    def Test45dLineIntersectionWithVerticalLineMovingNE(self):
        line1 = Line(Point(0,0), Point(10,10))
        line2 = Line(Point(5,0), Point(5,20))
        expectedIntersectionPoint = Point(5,5)
        intersectionPoint = line1.doesIntersect(line2)
        assert expectedIntersectionPoint.equal(intersectionPoint) == True

    def Test45dLineIntersectionWithVerticalLineMovingSE(self):
        line1 = Line(Point(0,20), Point(20,0))
        line2 = Line(Point(5,0), Point(5,20))
        expectedIntersectionPoint = Point(5,15)
        intersectionPoint = line1.doesIntersect(line2)
        assert expectedIntersectionPoint.equal(intersectionPoint) == True

    def Test45dLineIntersectionWithVerticalLineMovingNW(self):
        line1 = Line(Point(20,0), Point(0,20))
        line2 = Line(Point(5,0), Point(5,20))
        expectedIntersectionPoint = Point(5,15)
        intersectionPoint = line1.doesIntersect(line2)
        assert expectedIntersectionPoint.equal(intersectionPoint) == True

    def Test45dLineIntersectionWithVerticalLineMovingSW(self):
        line1 = Line(Point(10,10), Point(0,0))
        line2 = Line(Point(5,0), Point(5,20))
        expectedIntersectionPoint = Point(5,5)
        intersectionPoint = line1.doesIntersect(line2)
        assert expectedIntersectionPoint.equal(intersectionPoint) == True

    def TestNoIntersection(self):
        line1 = Line(Point(10,10), Point(0,0))
        line2 = Line(Point(15,0), Point(15,0))
        expectedIntersectionPoint = None
        intersectionPoint = line1.doesIntersect(line2)
        assert intersectionPoint == None

    def TestNoIntersectionParallelLines(self):
        line1 = Line(Point(10,10), Point(0,0))
        line2 = Line(Point(10,20), Point(20,30))
        expectedIntersectionPoint = None
        intersectionPoint = line1.doesIntersect(line2)
        assert intersectionPoint == None

    def Test45dLineIntersectionWithHorizontalLine(self):
        line1 = Line(Point(20,20), Point(0,0))
        line2 = Line(Point(0,5), Point(10,5))
        expectedIntersectionPoint = Point(5,5)
        intersectionPoint = line1.doesIntersect(line2)
        assert expectedIntersectionPoint.equal(intersectionPoint) == True

    def runAllTests(self):
        self.runTest(self.Test45dLines)
        self.runTest(self.Test45dLineIntersectionWithVerticalLineMovingNE)
        self.runTest(self.Test45dLineIntersectionWithVerticalLineMovingSE)
        self.runTest(self.Test45dLineIntersectionWithVerticalLineMovingNW)
        self.runTest(self.Test45dLineIntersectionWithVerticalLineMovingSW)
        self.runTest(self.TestNoIntersection)
        self.runTest(self.TestNoIntersectionParallelLines)
        self.runTest(self.Test45dLineIntersectionWithHorizontalLine)
    
def findAngleToTurnAfterIntersection(mission, robotLine, intersectionPoint, horizontal):
    if (horizontal == True):
        if (intersectionPoint.getX() < robotLine.getEnd().getX()):
            return 0
        else:
            return -179
    else:
        if (intersectionPoint.getY() < robotLine.getEnd().getY()):
            return -90
        else:
            return 90

def findDistanceToTravelAfterIntersection(mission, robotLine, intersectionPoint, angle):
    # For now 30 works for all missions, we can optimize later.
    distance = 30
    offset = 20
    if angle == 90:
        distance = intersectionPoint.getY() - mission.getBottomLeft().getY() + offset
    if angle == -90:
        distance = mission.getTopRight().getY() - intersectionPoint.getY() + offset
    if angle == 0:
        distance = mission.getTopRight().getX() - intersectionPoint.getX() + offset
    if angle == 179 or angle == -179:
        distance = intersectionPoint.getX() - mission.getBottomLeft().getX() + offset
    return distance

def calculateNewStartPointAfterInstersection(intersectionPoint, distance, angle):
    if (angle == 0):
        x = intersectionPoint.getX() + distance
        return Point(x, intersectionPoint.getY())
    elif(angle == -179 or angle == 179):
        x = intersectionPoint.getX() - distance
        return Point(x, intersectionPoint.getY())
    elif(angle == 90):
        y = intersectionPoint.getY() - distance
        return Point(intersectionPoint.getX(), y)
    else:
        y = intersectionPoint.getY() + distance
        return Point(intersectionPoint.getX(), y)

def intersectLineWithAllMissions(missions, robotLine):
    # Intersects the robotline with all missions and returns the mission
    # and the intersection point that is closest to the start point of the
    # robot line.
    # The code also returns if the intersection with the mission is with
    # the horizontal line or the vertical line to aid in which way to turn.

    # select a large value.
    minDistance = 1000000
    nearestIntersection = None
    nearestIntersectionMission = None
    for row in missions:
        bottomLeft = Point(row[1], row[2])
        topRight = Point(row[3], row[4])

        # Form mission.    
        mission = Mission(row[0], bottomLeft, topRight)
        intersectionPoint,horizontal = mission.findClosestIntersectionPoint(robotLine)

        if intersectionPoint != None:
            # Calculate distance of the intersection point from the start point.
            distance = intersectionPoint.distance(robotLine.getStart())
            if (distance < minDistance):
                minDistance = distance
                nearestIntersection = intersectionPoint
                nearestIntersectionMission = mission
                nearestintersectionHorizontal = horizontal

    if nearestIntersection != None:
        return nearestIntersection, nearestIntersectionMission, nearestintersectionHorizontal
    else:
        return None, None, None
            
def readMissionFile():
    csvfile = open("./mission_coordinates.txt", newline='\n')
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    missions = []
    count = 0
    for row in reader:
        if count != 0:
            introw = []
            firstiteration = True
            for value in row:
                if firstiteration == False:
                    introw.append(int(value))
                else:
                    introw.append(value)
                firstiteration = False
            missions.append(introw)
            #print(introw)
        count = 1
    return missions

def addActions(speed, angle, distance, mission, actions):
    actions.append('')
    actions.append("# Code to get past mission: {}".format(mission.getName()))
    actions.append("turnToAngle(targetAngle={}, speed={})".format(angle, speed))
    actions.append("gyroStraight(distance={}, speed={}, backward={}, targetAngle={})".format(int(distance), speed, "False", angle))

def drawPath(coordinates, color, runName):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(90, 10)
    turtle.write(runName, font=("Arial", 26, "bold"))
    
    turtle.pencolor(color)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(coordinates[0].getX(),coordinates[0].getY())
    turtle.pendown()
    turtle.showturtle()
    for coordinate in range(len(coordinates)):
            #print(str(coordinates[coordinate].getX()) + ", " + str(coordinates[coordinate].getY()))
            turtle.goto(coordinates[coordinate].getX(), coordinates[coordinate].getY())
    os.system("cls")
def checkIfEndInMission(endX, endY, missions):
    for row in missions:
        if endX >= row[1] and endX <= row[3] and endY >= row[2] and endY <= row[4]:
            return True, Mission(row[0], Point(row[1], row[2]), Point(row[3], row[4]))
    return False, None

def findPath(start, end, missions, speed, actions, coordinates):
    if (start == end):
        return True

    robotLine = Line(start, end)
    intersectionPoint, mission, horizontal = intersectLineWithAllMissions(missions, robotLine)
    coordinates.append(Point(start.getX(), start.getY()))
    endInMission, endMission = checkIfEndInMission(end.getX(), end.getY(), missions)
    if (intersectionPoint == None):
        # Get to the end point.
        robot = Robot(start.getX(), start.getY())
        robot.goto(end.getX(), end.getY(), endAngle=0, speed=speed)
        actions.append('')
        actions.append("# Drive from ({},{}) to ({},{})".format(start.getX(), start.getY(), end.getX(), end.getY()))
        coordinates.append(Point(end.getX(),end.getY()))
        robot.addActions(speed=speed, robotActions=actions)
        return True

    if (endInMission == True and mission.getName() == endMission.getName()):
        coordinates.append(Point(end.getX(), end.getY()))

        # Get from the intersection point to the end.
        robot = Robot(start.getX(), start.getY())
        robot.goto(end.getX(), end.getY(), endAngle=0, speed=speed)
        actions.append('')
        actions.append("# Drive from ({},{}) to ({},{})".format(start.getX(), start.getY(), end.getX(), end.getY()))
        robot.addActions(speed=speed, robotActions=actions)

        return True
    else:
        # First get to the intersection point.
        robot = Robot(start.getX(), start.getY())
        robot.goto(intersectionPoint.getX(), intersectionPoint.getY(), endAngle=0, speed=speed)
        actions.append('')
        actions.append("# Drive from ({},{}) to mission:{} at ({:3.0f},{:3.0f})".format(start.getX(), start.getY(), mission.getName(),intersectionPoint.getX(), intersectionPoint.getY()))
        coordinates.append(intersectionPoint)
        robot.addActions(speed=speed, robotActions=actions)

        # Add the code to get past the obstacle
        angle = findAngleToTurnAfterIntersection(mission, robotLine, intersectionPoint, horizontal)
        distance = findDistanceToTravelAfterIntersection(mission, robotLine, intersectionPoint, angle)
        startPoint = calculateNewStartPointAfterInstersection(intersectionPoint, distance, angle)
        addActions(speed, angle, distance, mission, actions)
        coordinates.append(startPoint)
        if (findPath(startPoint, end, missions, speed, actions, coordinates) == True):
            return True

def findPaths(points, color="blue", runName="Run6"):
    missions = readMissionFile()
    actions = []
    coordinates = []
    counter = 0

    for point in points:
        if counter < len(points) - 1:
            actions.append('')
            #actions.append("# Driving from ({},{}) to ({},{})".format(points[counter].getX(), 
            #    points[counter].getY(), points[counter+1].getX(), points[counter+1].getY()))
            findPath(points[counter], points[counter + 1], missions, 50, actions, coordinates)

        counter = counter + 1

    # print the code.
    print("--------------------------------------------------------------------------------------")
    print("Producing Code for Run6. Copy code below to run the Robot.")
    print("--------------------------------------------------------------------------------------")

    print("from utilities import *")
    print("\n\n")
    print("def {}()".format(runName))
    print("    # Code automatically generated by PathFinder.")
    print("    # Download the code below to the Robot and run it.")
    for action in actions:        
        print("    " + action)

    # Draw the path that the robot will take using Turtle Graphics 
    drawPath(coordinates, color, runName)

def findAndShowAllPaths():
    home2 = Point(190, 20)
    TV = Point(185, 65)
    HybridCar = Point(142, 90)
    home2 = Point(190, 20)
    powerplant = Point(100, 20)
    home1 = Point(20,10)
    smartgrid = Point(97, 94)
    solarplant = Point(77, 96)
    oilplatform = Point(5, 64)
    energyStorage = Point(40, 96)
    waterReservoir = Point(80, 64)
    toyfactory = Point(127,65)
    powerToX = Point(98, 54)
    windTurbine = Point(175, 90)
    RechargeableBattery = Point(149, 70)
    hydroDam = Point(56, 49)

    missions = readMissionFile()
    actions = []
    coordinates = []
    run1 = [home2, TV, windTurbine, RechargeableBattery, home2]
    run2 = [home2, powerplant, home2]
    run3 = [home2, RechargeableBattery, HybridCar, waterReservoir, solarplant, home1]
    run4 = [home1, hydroDam, home1]
    run5 = [home1, energyStorage, home1]
    run6 = [home1, smartgrid, waterReservoir]
    justForFun = [home2, TV, windTurbine, HybridCar, RechargeableBattery, smartgrid, solarplant, waterReservoir, home1,
                powerplant, powerToX, toyfactory, home2]
    points = run3
    counter = 0

    runs = {
            "run1": (run1, "red", "Run1"), 
            "run2": (run2, "blue", "Run2"), 
            "run3": (run3, "green", "Run3"), 
            "run4": (run4, "brown", "Run4"),
            "run5": (run5, "pink", "Run5"),
            "run6": (run6, "blue", "Run6")
            }
    print("------------------------------")
    print("Printing code now, copy this code to edit and run robot.")
    print("------------------------------")

    run = runs.get("run6")
    findPaths(points=run[0], color=run[1], runName=run[2])
    '''
    for run in runs:
        findPaths(run[0], run[1], run[2])
        sleep(2)clear
    '''
initializeGraphics()

def repeatlyShowThePaths():
    while(True):
        findAndShowAllPaths()
        sleep(1)
        screen.reset()
        turtle.pen(fillcolor="black", pencolor="blue", pensize=5)

repeatlyShowThePaths()
#findAndShowAllPaths()
screen.mainloop()

# Inputs for Run6
#         (Home1)     (Smart Grid)   (Water Reservoir)
#run6 = [Point(20,10), Point(97, 94), Point(80, 64)]

# Call PathFinder to create run6 code.
#findPaths(run6)

#print("\n\n")



