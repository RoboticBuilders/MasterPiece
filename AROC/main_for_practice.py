from Utilities import *
from run0 import *
from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *
import run6_new_path
import run6
from run7 import *
from run8 import *

## Use this file on the PRACTICE TABLE
## On counter 9, the old run6 is loaded. In case you need this. then just run that.

def _maindriver():
    counter = 0
    sw = StopWatch()

    while True:
        if (counter > 0):
            startAttachmentChangeTime = sw.time()
        hub.display.number(counter)
        if counter == 10: 
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
            runWithTiming(run6_new_path.run6, "run6")
        if counter == 7:
            runWithTiming(run7, "run7")
        if counter == 8:
            runWithTiming(run8, "run8")
        if counter == 9:
            runWithTiming(run6.run6, "run6")

        counter = counter + 1
        drive_base.straight(distance=0, then=Stop.BRAKE)

    endTotalTime = sw.time()
    sw.pause()
    print("total time = " + str(endTotalTime - startTotalTime))

initializeAndWaitForRobotReady()
_maindriver()
