# LEGO type:standard slot:0
# This is now the version of Round1 that we are committed to.
# region initialize
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait
from pybricks.parameters import Button
from pybricks.hubs import PrimeHub

hub = PrimeHub()

# Which Marvin is this.
# Amogh: A
# Rishabh-Nami: RN
# Anya:Arisha: AA
ROBOT = "A" 

pressed = []
while not any(pressed):
    pressed = hub.buttons.pressed()
    wait(10)

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)

left_med_motor = Motor(Port.B)
right_med_motor = Motor(Port.F)

left_color = ColorSensor(Port.C)
right_color = ColorSensor(Port.D)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = GyroDriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

def driverWithFewerArms():
    counter = 1
    arm_change_end_time = 0
    arm_change_start_time = 0
    while True:
        
        if counter == 7: 
            break
        # Skip printing for the first time the loop runs.
        if (counter != 1):
            arm_change_start_time = time.ticks_ms()
            logMessage("Waiting for arm change", level=0)

        primeHub.speaker.beep(90, 1)
        primeHub.right_button.wait_until_pressed()
        if (counter != 1):
            arm_change_end_time = time.ticks_ms()      
            logMessage("Time for arm change time(ms): {}".format(str(time.ticks_diff(arm_change_end_time, arm_change_start_time))), level=0)

        if counter == 1:
            doRunWithTiming(_run1)
        if counter == 2:
            doRunWithTiming(_run2)
        if counter == 3:
            doRunWithTiming(_run3)
        if counter == 4:
            doRunWithTiming(_run4)
        if counter == 5:
            doRunWithTiming(_run5)
        if counter == 6:
            doRunWithTiming(_run7)
        counter = counter + 1
#endregion

# region Rishabh
def craftCreatorAndVirtualRealityArtist():
    drive_base.straight(90)
    drive_base.turn(-45)
    drive_base.straight(240)
    #drive_base.straight(-3)
    left_med_motor.run_angle(1000, 2000)
    drive_base.straight(5, wait=False, straight_speed= 1000)
    drive_base.settings(straight_speed = 1050)
    drive_base.straight(-250)
    

def rollingCamera():
    drive_base.settings(straight_speed = 525)
    drive_base.straight(25)
    drive_base.turn(525, -2)
    drive_base.straight(30)
    drive_base.settings(straight_speed = 250)
    drive_base.straight(20)
    drive_base.settings(straight_speed = 1050)
    drive_base.straight(75)

def rightSide():
    craftCreatorAndVirtualRealityArtist()
    while True:
        if Button.RIGHT in pressed:
            break
        wait(10)
    rollingCamera()

def test():
    left_med_motor.run_angle(1000, 3600)
    right_med_motor.run_angle(1000, 3600)

def virtualrealityspinny():
    drive_base.straight(130)
    drive_base.turn(-90)
    drive_base.straight(40)
    drive_base.turn(45)
    drive_base.straight(135)
    drive_base.settings(turn_rate = 50)
    drive_base.turn(20)
    left_med_motor.run_angle(speed = 400, rotation_angle = 100)
    
#endregion

# region calls 
#rightSide()
virtualrealityspinny()
#craftCreatorAndVirtualRealityArtist()
#left_med_motor.run_angle(1000, 20000)
#test()
#endregion