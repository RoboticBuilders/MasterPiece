from Utilities import *
from run1 import *
from run2 import *
from run3 import *
from run4 import *
from run5 import *

def _maindriver():
    counter = 1
    arm_change_start_time = 0
    arm_change_end_time = 0
    stopwatch = StopWatch()
    counter = 1

    while True:
        hub.display.number(counter)
        if counter == 6: 
            break
        # Skip printing for the first time the loop runs.
        if (counter != 1):
            arm_change_start_time = stopwatch.time()
            print("Waiting for arm change")

        hub.speaker.beep()
        resetRobot()
        print("Waiting for right button press...")
        button = waitForButtonPress()
        print(button)

        # display counter
        # if the left button is pressed 
        # counter=counter+1
        # if right button is pressed
        # run counter "continue counter from there"

        if button==Button.LEFT:
            counter=counter+1
            continue

# the next few lines are the else loop here it is also the case if the right button is pressed.
        if (counter != 1):
            arm_change_end_time = stopwatch.time()    
            print("Time for arm change time(ms): {}".format(str(arm_change_end_time- arm_change_start_time)))

        if counter == 1:
            runWithTiming(run1,"run1")
        if counter == 2:
            runWithTiming(run2,"run2")
        if counter == 3:
            runWithTiming(run3,"run3")
        if counter == 4:
            runWithTiming(run4,"run4")
        if counter == 5:
            runWithTiming(run45,"run45")
        if counter == 6:
            runWithTiming(run5,"run5")
        
        counter = counter + 1
        drive_base.straight(distance=0, then=Stop.BRAKE)

stopwatch = StopWatch()
start_time = stopwatch.time()
initializeAndWaitForRobotReady()
_maindriver()

#run4()
end_time = stopwatch.time()
print("Total Time: " + str((end_time-start_time)/1000) + " seconds")
















