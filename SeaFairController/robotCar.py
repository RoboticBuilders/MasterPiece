from pybricks.hubs import ThisHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the hub for sending and receiving.
hub = ThisHub(broadcast_channel=2, observe_channels=[1])

# Initialize the drive base.
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)
drive_base = DriveBase(
    left_motor, right_motor, wheel_diameter=56, axle_track=112
)

# Initialize the distance sensor.
sensor = UltrasonicSensor(Port.D)

while True:
    # Receive tilt data.
    data = hub.ble.observe(1)

    if data is not None:
        #print(data)
        turn = data[0]
        forward = data[1]
        speedInput = data[2]

        speed = speedInput * 50
        
        if (turn < -50):
            turn = -50
        elif (turn > 50):
            turn = 50
        
        ###print(forward)
        if (forward < -10):
            speed = speed * -1
    
        drive_base.drive(speed, turn)
    #else:
        # If we lost the signal, stop.
        #drive_base.stop()

    # Send the distance data
    #hub.ble.broadcast(sensor.distance())

    # Wait some time.
    wait(10)

