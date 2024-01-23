from Utilities import *
from run0 import *
from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *
from run6 import *
from run7 import *
from run8 import *

# ************** IMPORTANT ********************************
# The right bucket design should be such that it is 4.5 centimeters outside from the bucket wall.

def _maindriver():
    counter = 0
    arm_change_start_time = 0
    arm_change_end_time = 0
    stopwatch = StopWatch()
    # This start time is going to get overridden in the main loop.
    start_time = stopwatch.time()

    while True:
        hub.display.number(counter)
        if counter == 9: 
            break

        # Beep that we are ready for button press.
        hub.speaker.beep()

        # Skip printing for the first time the loop runs.
        if (counter != 0):
            arm_change_start_time = stopwatch.time()
        
        button = waitForButtonPress()
        resetRobot()

        if button == Button.LEFT:
            counter = counter + 1
            continue

        # The next few lines are the else loop here it is also the case if the right button is pressed.
        if (counter != 0):
            arm_change_end_time = stopwatch.time()    
            print("Time for arm change time(ms): {}".format(str(arm_change_end_time- arm_change_start_time)))

        if counter == 0:
            start_time = stopwatch.time()
            runWithTiming(run0, "CraftCreator+Chicken")
        if counter == 1:
            runWithTiming(run1, "Home1ToHome2")
        if counter == 2:
            runWithTiming(run2,"lever")
        if counter == 3:
            runWithTiming(run3,"SceneChange")
        if counter == 4:
            runWithTiming(run4, "3d cinema")
        if counter == 5:
            runWithTiming(run5, "Sound mixer")
        if counter == 6:
            runWithTiming(run6, "LightShow+Immersive")
        if counter == 7:
            runWithTiming(run7, "Rolling Camera")
        if counter == 8:
            runWithTiming(run8, "Music Concert")
        
        
        counter = counter + 1
        drive_base.straight(distance=0, then=Stop.BRAKE)
    
    end_time = stopwatch.time()
    print("Total Time: " + str((end_time-start_time)/1000) + " seconds")


initializeAndWaitForRobotReady()
_maindriver()

#testHsv()