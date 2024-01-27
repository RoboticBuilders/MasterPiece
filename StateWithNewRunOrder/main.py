from Utilities import *
from run0 import *
from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *
from run6 import *
from run7 import *
from run8_without_slider import *

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
            message = "Run" + str(counter - 1) + "To" + str(counter) + "AttachmentChange"
            print("AttachmentChange: " + message + ":" + str(arm_change_end_time- arm_change_start_time))

        if counter == 0:
            start_time = stopwatch.time()
            runWithTiming(run0, "run0")
        if counter == 1:
            runWithTiming(run1, "run1")
        if counter == 2:
            runWithTiming(run2, "run2")
        if counter == 3:
            runWithTiming(run3, "run3")
        if counter == 4:
            runWithTiming(run4, "run4")
        if counter == 5:
            runWithTiming(run5, "run5")
        if counter == 6:
            runWithTiming(run6, "run6")
        if counter == 7:
            runWithTiming(run7, "run7")
        if counter == 8:
            runWithTiming(mainRun8, "run8")
        
        
        counter = counter + 1
        drive_base.straight(distance=0, then=Stop.BRAKE)
    
    end_time = stopwatch.time()
    print("Total Time: " + str((end_time-start_time)/1000) + " seconds")


initializeAndWaitForRobotReady()
_maindriver()

#testHsv()