from Utilities import *


def goToScenceChangeFromHomeFaster():
    # First bring bucket down:
    right_med_motor.run_angle(speed=2000, rotation_angle = -800, wait = True)
    # Drive towards the scene change, catch the line.
    angle = 15
    gyroStraightWithDriveWithAccurateDistance(distance=35, speed=500, targetAngle=angle, gradualAcceleration = False,
                                              backward=False, stop=Stop.COAST, slowDown = False)

    # Drive till the black line. Notice the tillBlackLine = True.                                              
    if(gyroStraightWithDriveWithAccurateDistance(distance=25, speed=500, targetAngle=angle,
                                              backward=False, tillBlackLine=True, stop=Stop.COAST) == False):
        print("Missed black line catch infront of the scene change.")
    
    # Go forward a litle more
    gyroStraightWithDrive(distanceInCm=3, targetAngle=angle, speed=300)


def _doexpertdropoff():
    angle = 30
    turnToAngle(targetAngle=angle, speed=500)
    gyroStraightWithDrive(distanceInCm=5, targetAngle=angle, speed=500)
    right_med_motor.run_angle(speed=2000, rotation_angle = 800)
    
def _doSceneChange():
    angle = 30
    # Backup after expert dropoff
    gyroStraightWithDriveWithAccurateDistance(distance=8, speed=500, targetAngle=angle,backward=True)
    # Start bringing down the bucket when we move forward to push the scene.
    angle = -45
    turnToAngle(targetAngle=angle, speed=500)
    right_med_motor.run_angle(speed=2000, rotation_angle = -800, wait = False)
    gyroStraightWithDrive(distanceInCm=8, targetAngle=angle, speed=300)
    
    # wait for the bucket to come down.
    while (right_med_motor.done() == False):
        continue

def goHome():
    # Go home with curve
    drive_base.settings(1000, 1000, 1000, 1000)
    drive_base.curve(radius = -155, angle = -45, then=Stop.COAST)
    #Radius was -650 and angle was -50
    drive_base.curve(radius = -740, angle = -50)
    
    # Raise the arm
    right_med_motor.run_angle(speed=2000, rotation_angle = 800, wait = False)

def run3():
    resetRobot()
    goToScenceChangeFromHomeFaster()
    _doexpertdropoff()
    _doSceneChange()
    goHome()
waitForButtonPress()
runWithTiming(run3,"SceneChange")