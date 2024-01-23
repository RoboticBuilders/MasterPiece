from Utilities import *
from goRightHometoLeftHome import *
from run0 import *
from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *
from run6 import *
from run7 import *

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
            # Craft creator & Virtual reality run
            start_time = stopwatch.time()
            runWithTiming(run6, "run6")
        if counter == 1:
            # Go from right home to left home
            runWithTiming(dohome2home, "dohome2home")
        if counter == 2:
            # lever
            runWithTiming(run2,"lever")
        if counter == 3:
            # Theater scene change run
            runWithTiming(run3,"SceneChange")
        if counter == 4:
            # Immersive experience run
            runWithTiming(run1,"3d cinema")
        if counter == 5:
            # sound mixer
            runWithTiming(run0, "Sound mixer")
        if counter == 6:
            # Craft creator & Virtual reality run
            runWithTiming(run4,"run4")
        if counter == 7:
            # Music concert run
            runWithTiming(run5,"run5")
        if counter == 8:
            # Music concert run
            runWithTiming(run7,"run7")
        
        
        counter = counter + 1
        drive_base.straight(distance=0, then=Stop.BRAKE)
    
    end_time = stopwatch.time()
    print("Total Time: " + str((end_time-start_time)/1000) + " seconds")


initializeAndWaitForRobotReady()
_maindriver()

#testHsv()