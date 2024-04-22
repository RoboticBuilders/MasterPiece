from Utilities import *


def goToExpertDropOffFromHomeFaster():

    # First bring down the bucket.
    right_med_motor.run_angle(speed=2000, rotation_angle = -800, wait = True)
   
    # Drive towards the scene change, catch the line.
    angle = 23
    gyroStraightWithDriveWithAccurateDistance(distance=50, speed=500, targetAngle=angle, gradualAcceleration = False,
                                              backward=False)

    # Drive till the black line. Notice the tillBlackLine = True.                                              
    if(gyroStraightWithDriveWithAccurateDistance(distance=15, speed=500, targetAngle=angle,
                                              backward=False, tillBlackLine=True) == False):
        print("Missed black line catch infront of the scene change.")

    # Go forward a litle more
    gyroStraightWithDrive(distanceInCm=7, targetAngle=angle, speed=300)
    # Now dropoff experts...
    right_med_motor.run_angle(speed=2000, rotation_angle = 800,wait=True)

def _doSceneChange():
    angle = 25
    # Backup after expert dropoff
    drive_base.straight(distance=-80)

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
    #Change 1/24/2024: radius change from -155
    drive_base.curve(radius = -130, angle = -45, then=Stop.COAST)
    #Radius was -650 and angle was -50
    drive_base.curve(radius = -730, angle = -75)

    # Raise the arm
    right_med_motor.run_angle(speed=2000, rotation_angle = 800, wait = False)

def run3():
    resetRobot()
    goToExpertDropOffFromHomeFaster()
    _doSceneChange()
    goHome()

# First bring bucket down:
#waitForButtonPress()
#resetRobot()
#right_med_motor.run_angle(speed=2000, rotation_angle = -800, wait = True)

#runWithTiming(run3,"SceneChange")
#waitForButtonPress()