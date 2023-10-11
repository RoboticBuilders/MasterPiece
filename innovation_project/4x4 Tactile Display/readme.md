# 4x4 Tactile Display

This display prototype consists 16 tactile pins laid out in a 4x4 grid, and whose heights can be individually controlled by a dc motor. 

The display consists of 4 `pin frames`, each corresponding to a row in the display. Each frame has 4 simple DC motors with a lead screw actuator that moves the pins up/down. The frame and it's motors are controlled by an Arduino UNO and a HW-130 shield. 

The overall display is controlled by a `master` Arduino UNO which manages which image to display and when to show it. It does so by sending each frame instructions about it's pin heights at set intervals of time. In our demo, the master sends instructions to each frame to show it's part of the letters '4', '2' and 'W' at an interval of 20 seconds.