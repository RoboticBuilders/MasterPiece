from Utilities import *
from run0 import *
from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *
from run6_new_path import *
from run7 import *
from run8 import *

# ************** IMPORTANT ********************************
# The right bucket design should be such that it is 4.5 centimeters outside from the bucket wall.

def _maindriver():
    counter = 0
    sw = StopWatch()

    while True:
        if (counter > 0):
            startAttachmentChangeTime = sw.time()
        hub.display.number(counter)
        if counter == 9: 
            break

        # Beep that we are ready for button press.
        hub.speaker.beep()
        button = waitForButtonPress()
        if (counter == 0):
            sw.resume()
            startTotalTime = sw.time()
        resetRobot()

        if button == Button.LEFT:
            counter = counter + 1
            continue

        if (counter > 0):
            endAttachmentChangeTime = sw.time()
            print("Attachment change time = " + str(endAttachmentChangeTime - startAttachmentChangeTime))

        if counter == 0:
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
            runWithTiming(run8, "run8")
        
        counter = counter + 1
        drive_base.straight(distance=0, then=Stop.BRAKE)

    endTotalTime = sw.time()
    sw.pause()
    print("total time = " + str(endTotalTime - startTotalTime))

initializeAndWaitForRobotReady()
_maindriver()
