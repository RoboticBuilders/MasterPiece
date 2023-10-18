#include <AccelStepper.h>
#include <MultiStepper.h>

#define STEPPER_ENABLE_PIN 8 

// Define the stepper motor and the pins that is connected to
AccelStepper stepper1(1, 2, 5); // X (Typeof driver: with 2 pins, STEP, DIR)
// AccelStepper stepper2(1, 3, 6); // Y
// AccelStepper stepper3(1, 4, 7); // Z
// AccelStepper stepper4(1, 12, 13); // A

AccelStepper steppersArr[] = {stepper1};//, stepper2, stepper3, stepper4};


MultiStepper steppersControl;  // Create instance of MultiStepper

long gotoposition[1]; // An array to store the target positions for each stepper motor

void setup() {

  Serial.begin(9600);
  // // set up the CNC Shield I/O
  // digitalWrite(STEPPER_ENABLE_PIN, HIGH); // initialize drivers in disabled state
  // pinMode(STEPPER_ENABLE_PIN, OUTPUT);

  stepper1.setMaxSpeed(100); // Set maximum speed value for the stepper
  // stepper2.setMaxSpeed(100);
  // stepper3.setMaxSpeed(100);
  // stepper4.setMaxSpeed(100);

  stepper1.setCurrentPosition(0); // Set maximum speed value for the stepper
  // stepper2.setCurrentPosition(0);
  // stepper3.setCurrentPosition(0);
  // stepper4.setCurrentPosition(0);


  // Adding the 3 steppers to the steppersControl instance for multi stepper control
  steppersControl.addStepper(stepper1);
  // steppersControl.addStepper(stepper2);
  // steppersControl.addStepper(stepper3);
  // steppersControl.addStepper(stepper4);


  
  stepper1.disableOutputs();
  // stepper2.disableOutputs();
  // stepper3.disableOutputs();
  // stepper4.disableOutputs();
  // // enable the drivers, the motors will remain constantly energized
  // digitalWrite(STEPPER_ENABLE_PIN, LOW);

}

void loop() {

  stepper1.enableOutputs();
  // stepper2.enableOutputs();
  // stepper3.enableOutputs();
  // stepper4.enableOutputs();
  
  // Store the target positions in the "gotopostion" array
  gotoposition[0] = 100;  // 800 steps - full rotation with quater-step resolution
  // gotoposition[1] = 100;
  // gotoposition[2] = 80;
  // gotoposition[3] = 80;

  Serial.println("Starting ...");
  steppersControl.moveTo(gotoposition); // Calculates the required speed for all motors
  steppersControl.runSpeedToPosition(); // Blocks until all steppers are in position

  delay(1000);

  gotoposition[0] = 0;
  // gotoposition[1] = 0;
  // gotoposition[2] = 0;
  // gotoposition[3] = 0;

  steppersControl.moveTo(gotoposition);
  steppersControl.runSpeedToPosition();

  // stepper1.stop(); //stop motor
  // stepper1.disableOutputs(); //disable power
  stepper1.stop();
  // stepper2.stop();
  // stepper3.stop();
  // stepper4.stop();
  stepper1.disableOutputs();
  // stepper2.disableOutputs();
  // stepper3.disableOutputs();
  // stepper4.disableOutputs();
  delay(5000);
}
