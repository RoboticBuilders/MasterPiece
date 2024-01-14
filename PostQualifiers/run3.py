from Utilities import *

def goHome():
    # Go home with curve
    drive_base.settings(1000, 1000, 1000, 1000)
    drive_base.curve(radius = -160, angle = -45, then=Stop.COAST)
    #Radius was -650 and angle was -50
    drive_base.curve(radius = -740, angle = -50)
    
    # Raise the arm
    right_med_motor.run_angle(speed=2000, rotation_angle = 800, wait = False)

def goToScenceChangeFromHomeFaster():
    # Drive towards the scene change, catch the line.
    angle = 11
    gyroStraightWithDriveWithAccurateDistance(distance=35, speed=500, targetAngle=angle, gradualAcceleration = False,
                                              backward=False, stop=Stop.COAST, slowDown = False)

    # Drive till the black line. Notice the tillBlackLine = True.                                              
    if(gyroStraightWithDriveWithAccurateDistance(distance=25, speed=500, targetAngle=angle,
                                              backward=False, tillBlackLine=True, stop=Stop.COAST) == False):
        print("Missed black line catch infront of the scene change.")
    
    # Go forward a litle more
    gyroStraightWithDrive(distanceInCm=3, targetAngle=angle, speed=300)

    # Turn towards the scene change. 
    angle = -45
    turnToAngle(targetAngle=angle, speed=500)
    
def _doSceneChange():
    
    # Start bringing down the bucket when we move forward to push the scene.
    angle = -45
    right_med_motor.run_angle(speed=2000, rotation_angle = -800, wait = False)
    gyroStraightWithDrive(distanceInCm=8, targetAngle=angle, speed=300)
    
    # wait for the bucket to come down.
    while (right_med_motor.done() == False):
        continue

def run3():
    resetRobot()
    goToScenceChangeFromHomeFaster()
    _doSceneChange()
    goHome()

# runWithTiming(run3,"SceneChange")