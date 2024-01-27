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


def _doexpertdropoff():
    angle = 30
    turnToAngle(targetAngle=angle, speed=500)
    gyroStraightWithDrive(distanceInCm=5, targetAngle=angle, speed=500)
    right_med_motor.run_angle(speed=2000, rotation_angle = 800)

def _doSceneChange():
    angle = 25
    # Backup after expert dropoff
    #gyroStraightWithDriveWithAccurateDistance(distance=5, speed=500, targetAngle=angle,backward=True)
    #was -70 changed to -100 due to making wait true for bucket raising after experts dropoff
    #Changed 1/26/2024 - increased baclup from 9 to 10
    drive_base.straight(distance=-100)


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
    drive_base.curve(radius = -720, angle = -55)

    # Raise the arm
    right_med_motor.run_angle(speed=2000, rotation_angle = 800, wait = False)

def run3():
    resetRobot()
    goToExpertDropOffFromHomeFaster()
    #_doexpertdropoff()
    _doSceneChange()
    goHome()

# First bring bucket down:
#resetRobot()
#right_med_motor.run_angle(speed=2000, rotation_angle = -800, wait = True)

#runWithTiming(run3,"SceneChange")
#waitForButtonPress()