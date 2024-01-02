from Utilities import *

DRIVE_SPEED = 400
TURN_SPEED = 500


def goHome():
    #Go home with curve
    drive_base.settings(1000, 1000, 1000, 1000)
    drive_base.curve(radius = -160,angle = -45,then=Stop.COAST)
    drive_base.curve(radius = -460,angle = -70)
    '''
    angle = -45
    # backup from movie set
    gyroStraightWithDrive(distanceInCm = 10, speed = 1000, targetAngle = angle, backward = True)
    # Now turn a little and backup all the way between 3d cinema and sound mixer
    angle = 15
    turnToAngle(targetAngle = angle, speed = TURN_SPEED)
    gyroStraightWithDrive(distanceInCm = 40, speed = 1000, targetAngle = angle, backward = True)
    '''
    # Raise the arm
    right_med_motor.run_angle(speed=2000, rotation_angle = 800)
    


def goToScenceChangeFromHome():
    # Go straight
    angle = 0
    gyroStraightWithDrive(distanceInCm=26, targetAngle=angle, speed=1000)
    # Turn towards sound mixer and drive straight
    angle = 55
    turnToAngle(targetAngle=angle,speed=TURN_SPEED)
    gyroStraightWithDrive(distanceInCm=10, targetAngle=angle, speed=1000)
    #Catch the black line between 3d cinema and sound mixer
    driveTillLine(speed=200, doCorrection=False, sensor=right_color, blackOrWhite="Black")
    # Now move towards the movie set
    angle = 0
    turnToAngle(targetAngle=angle,speed=TURN_SPEED)
    gyroStraightWithDrive(distanceInCm=10, targetAngle=angle, speed=800)
    #Catch the black line in front of movie set
    driveTillLine(speed=200, doCorrection=False, sensor=right_color, blackOrWhite="Black")
    gyroStraightWithDrive(distanceInCm=2, targetAngle=angle, speed=300)
    # Now turn towards movie set
    angle = -45
    turnToAngle(targetAngle=angle,speed=TURN_SPEED)

def goToScenceChangeFromHomeFaster():
    angle = 7
    gyroStraightWithDrive(distanceInCm=35, targetAngle=angle, speed=1000)
    driveTillLine(speed=400, doCorrection=False, sensor=right_color, blackOrWhite="Black")
    gyroStraightWithDrive(distanceInCm=3, targetAngle=angle, speed=300)
    angle = -45
    turnToAngle(targetAngle=angle,speed=TURN_SPEED)
    #Raise the bucket
    right_med_motor.run_angle(speed=2000, rotation_angle = 800,wait=False)
    


def _doSceneChange():
    angle = -45
    gyroStraightWithDrive(distanceInCm=8, targetAngle=angle, speed=300)
    right_med_motor.run_angle(speed=2000, rotation_angle = -800)

def run3():
    resetRobot()
    #right_med_motor.run_angle(speed=2000, rotation_angle = 800)
    #goToScenceChangeFromHome()
    goToScenceChangeFromHomeFaster()
    _doSceneChange()
    goHome()

# runWithTiming(run3,"SceneChange")