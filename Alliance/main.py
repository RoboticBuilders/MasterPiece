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
    
    while True:
        hub.display.number(counter)
        if counter == 9: 
            break

        # Beep that we are ready for button press.
        hub.speaker.beep()
        button = waitForButtonPress()
        resetRobot()

        if button == Button.LEFT:
            counter = counter + 1
            continue

        if counter == 0:
            run0()
        if counter == 1:
            run1()
        if counter == 2:
            run2()
            counter = 6
        if counter == 6:
            run6()
        if counter == 7:
            run7()
        if counter == 8:
            run8()
        
        counter = counter + 1
        drive_base.straight(distance=0, then=Stop.BRAKE)

initializeAndWaitForRobotReady()
_maindriver()
