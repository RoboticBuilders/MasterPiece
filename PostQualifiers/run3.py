from Utilities import *

def goHome():
    #Go home with curve
    drive_base.settings(1000, 1000, 1000, 1000)
    drive_base.curve(radius = -160, angle = -45, then=Stop.COAST)
    drive_base.curve(radius = -650, angle = -55)
    
    # Raise the arm
    right_med_motor.run_angle(speed=2000, rotation_angle = 800)

def goToScenceChangeFromHomeFaster():
    stopwatch = StopWatch()
    # This start time is going to get overridden in the main loop.
    t1 = stopwatch.time()

    # Drive towards the scene change, catch the line.
    angle = 10
    gyroStraightWithDriveWithAccurateDistance(distance=35, speed=2000, targetAngle=angle, gradualAcceleration = False,
                                              backward=False, stop=Stop.COAST, slowDown = False)

    t2 = stopwatch.time()
    print("first straight: " + str(t2-t1))
    gyroStraightWithDriveWithAccurateDistance(distance=25, speed=500, targetAngle=angle,
                                              backward=False, tillBlackLine=True, stop=Stop.COAST)
    t3 = stopwatch.time()
    print("black straight: " + str(t3-t2))
    
    # Go forward a litle more
    gyroStraightWithDrive(distanceInCm=3, targetAngle=angle, speed=300)
    t4 = stopwatch.time()
    print("more straight: " + str(t4-t3))

    angle = -45
    turnToAngle(targetAngle=angle, speed=500)
    t5 = stopwatch.time()
    print("after turn: " + str(t5-t4))
    #Raise the bucket This is wrong line of code. delete after testing
    #right_med_motor.run_angle(speed=2000, rotation_angle = 800,wait=False)
    stopwatch.time()

def _doSceneChange():
    stopwatch = StopWatch()
    # This start time is going to get overridden in the main loop.
    t1 = stopwatch.time()

    # Start bringing down the bucket when we move forward.
    angle = -45
    right_med_motor.run_angle(speed=2000, rotation_angle = -800, wait = False)
    gyroStraightWithDrive(distanceInCm=8, targetAngle=angle, speed=300)
    t2 = stopwatch.time()
    print("8cm straight: " + str(t2-t1))
    
    # wait for the bucket to come down.
    while (right_med_motor.done() == False):
        continue

    t3 = stopwatch.time()
    print("Bucket down: " + str(t3-t2))

    

def run3():
    resetRobot()
    #right_med_motor.run_angle(speed=2000, rotation_angle = 800)
    #goToScenceChangeFromHome()
    goToScenceChangeFromHomeFaster()
    _doSceneChange()
    goHome()

# runWithTiming(run3,"SceneChange")