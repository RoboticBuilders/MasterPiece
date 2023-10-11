# 4x4 Tactile Display

This display prototype consists 16 tactile pins laid out in a 4x4 grid, and whose heights can be individually controlled by a dc motor. 

The display consists of 4 `pin frames`, each corresponding to a row in the display. Each frame has 4 simple DC motors with a lead screw actuator that moves the pins up/down. The frame and it's motors are controlled by an Arduino UNO and a HW-130 shield. 

The overall display is controlled by a `master` Arduino UNO which manages which image to display and when to show it. It does so by sending each frame instructions about it's pin heights at set intervals of time. In our demo, the master sends instructions to each frame to show it's part of the letters '4', '2' and 'W' at an interval of 20 seconds.

# Parts list for a 4x4

| Item        | Count       | Description |
| ----------- | ----------- | ----------- |
| Frames       | `4`           | The 3D printed frame for each row of the display. |
| Base       | `1`           | A 3D printed base on which the frames are placed. |
| Shoulders | 2 | A 3D printed structure that holds the tops of the frames together |
| DC motors + screw | `16` | Motors that power the actuator for the pins. 4 per frame |
| Hex spacers | `16` | Spacers that go over the screw and provide linear motion. |
| Pin Heads       | `16` | 3D printed pin heads to place on the hex spacers |
| Arduino (subs) |`4` | One for each frame to control the motors and communication |
| Arduino (master) | `1` | Controls communication and controls what image is showm |
| HW-130 shield | `4` | One for each frame to drive the motors |
| 9V Batteries | `4` | Provides power for the HW-130 and Arduino |
| 9V battery terminals | `4` | Connects the batteries to the HW-130 |
| Wires | `Many` | To connect the motors to the HW-130 and the master Arduino |
| LCD display | `1` | To let users know what is happening (mostly the wait countdown) |
| Arduino cables (subs) | `4` | To deploy programs to the sub Arduinos |
| Arduino cable (master) | `1` | To provide power and deploy program to the master |
| Breadboard (or prototype board) | `1` | To connect master/sub/LCD communication wires for I2C |