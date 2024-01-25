from Utilities import *

class stall_detect:
    # stalls based on load
    def load(max_load = 100, debug = False):
        while drive_base.done() == False: # while either motor is still moving
            if int((abs(left_motor.load()) + abs(right_motor.load())) / 2) > max_load: # if there is extra load
                # calculate load
                left_load = abs(left_motor.load())
                right_load = abs(right_motor.load())
                load = int((left_load + right_load) / 2)

                if debug == True:
                    print("Stopping stall detection with " + str(load) + " load.") # print debug messages

                # stop the motors
                left_motor.stop()
                right_motor.stop()

                # exit the loop
                break

            else: # if there is no extra load
                # calculate load
                left_load = left_motor.load()
                right_load = right_motor.load()
                load = int((left_load + right_load) / 2)

                if debug == True:
                    print("Continuing stall detection with " + str(load) + " load.") # print debug messages

                continue # keep running the loop

    # stalls based on angle change
    def angle_change(max_iterations = 5, deadzone = 10, debug = False):
        # define reading arrays
        right_readings = []
        left_readings = []

        while drive_base.done() == False: # while either motor is still moving
            if int((len(right_readings) + len(left_readings)) / 2) > 5: # if there are more than 5 readings
                # append new readings
                right_readings.append(right_motor.angle())
                left_readings.append(left_motor.angle())

                # calculate the motor speed for proportional calculations
                right_speed = right_motor.speed()
                left_speed = left_motor.speed()
                speed = int((right_speed + left_speed) / 2)

                # calculate the reading diff
                right_reading_diff = right_readings[-1] - right_readings[-1 * max_iterations]
                left_reading_diff = left_readings[-1] - left_readings[-1 * max_iterations]
                reading_diff = int((right_reading_diff + left_reading_diff) / 2)

                if reading_diff < int((deadzone * speed) / 100): # if the readings haven't changed enough
                    # stop the motors
                    right_motor.stop()
                    left_motor.stop()
                    
                    if debug == True:
                        print("Stopping stall detection with angle change of " + str(reading_diff) + " degrees.") # print debug messages

                    # exit the loop
                    break

                else:
                    print("Continuing stall detection with angle change of " + str(reading_diff) + " degrees.")

            else: # if there are less than 5 readings
                # append new readings
                right_readings.append(right_motor.angle())
                left_readings.append(left_motor.angle())

drive_base.straight(distance = -5000, wait = False)
stall_detect.load(max_load = 150, debug = True)