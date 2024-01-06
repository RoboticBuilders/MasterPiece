#include <AccelStepper.h>
#include <MultiStepper.h>
#include <Wire.h>
#include <EEPROM.h>

#define STEPPER_ENABLE_PIN 8 

// Define the stepper motor and the pins that is connected to
AccelStepper stepper1(1, 2, 5); // X (Typeof driver: with 2 pins, STEP, DIR)
AccelStepper stepper2(1, 3, 6); // Y
AccelStepper stepper3(1, 4, 7); // Z
AccelStepper stepper4(1, 12, 13); // A

AccelStepper steppersArray[] = {stepper1, stepper2, stepper3, stepper4};

  // Create instance of MultiStepper to control Motors
MultiStepper steppersControl;

// I2C wire address for this unit. Make sure you set this to the right address before deploying. Valid addresses are {8, 9, 10, 11} from top to bottom row.
int i2cWireAddress = 51;

// An array to store the target positions for each stepper motor
long goToPositions[4];
bool pinPositionsReceived = false;
bool testExecuted = false;

void setup() {
  Serial.begin(9600);

  // read EEPROM for i2cWireAddress
  int wireAddress = readWireAddress();
  i2cWireAddress = wireAddress;
  Serial.print("Wire address "); Serial.println(wireAddress);

  // join I2C bus with the address for this sub Arduino
  Wire.begin(i2cWireAddress);     

  // Register a handler for data receive
  Wire.onReceive(receiveEvent);  

  initializeMotors();
  disableMotorOutputs();
  resetPositionsArray();

  Serial.println("Setup completed");   
}

void loop() {

  if (testExecuted == true) {
    return;
  }

  TestMotors();
  testExecuted = true;

  if (pinPositionsReceived == false) {
    delay(300);
    return;
  }

  Serial.println("Pin positions received ...");
  enableMotorOutputs();
  steppersControl.moveTo(goToPositions); // Calculates the required speed for all motors
  steppersControl.runSpeedToPosition(); // Blocks until all steppers are in position
  delay(1000);

  stopMotors();
  delay(2000);

  // bring motors back to zero positions
  resetPositionsArray();
  steppersControl.moveTo(goToPositions);
  disableMotorOutputs();

  pinPositionsReceived = false;

  delay(1000);

}

// initalize motors and setup the accelerator
void initializeMotors() {
  for (int i = 0; i < 4; i++) {
    // set max speed value for the steppers
    AccelStepper stepper = steppersArray[i];
    stepper.setMaxSpeed(100);
    stepper.setCurrentPosition(0);
    steppersControl.addStepper(stepper);
  }
}

void stopMotors() {
    for (int i = 0; i < 4; i++) {
    steppersArray[i].stop();
  }
}
void disableMotorOutputs() {
  for (int i = 0; i < 4; i++) {
    steppersArray[i].disableOutputs();
  }
}

void enableMotorOutputs() {
  for (int i = 0; i < 4; i++) {
    // set max speed value for the steppers
    AccelStepper stepper = steppersArray[i];
    stepper.enableOutputs();
  }
}

void resetPositionsArray() {
   for (int i = 0; i < 4; i++) {
    goToPositions[i] = 0;
   }
}
// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  Serial.print("received event: "); Serial.println(howMany);

  while (1 < Wire.available()) {  // loop through all but the last
    char c = Wire.read();         // receive byte as a character
    Serial.print(c);              // print the character
  }

  int x = Wire.read();           // receive byte as an integer
  Serial.print("Sub reads: ");   // print the integer
  Serial.println(x);             // print the integer

  if (x == -1)
    return;

  // Get height data from the received byte. Each pin uses 2 of the 8 bits in the data stream. The bit operations below extracts these values and adds them to an array.
  int arr[] = { x & 3, x >> 2 & 3, x >> 4 & 3, x >> 6 & 3 };

  // Print for debug purposes
  for (int i = 0; i < 4; i++) {
    Serial.print(arr[i]);
  }
  Serial.println();

  // Set motor state for each motor that has a height >=1. The control loop uses this info to run the pin to the right height.
  // Currently, this state is a boolean corresponding to UP or DOWN, but we could change it to a int with 4 levels of height with the 2 bits we have
  // We can also redo the code here to accept 4 bytes instead of 1 to give each motor 1/256 units of motion - overkill for our motor setup.
  for (int i = 0; i < 4; i++) {
    goToPositions[i] = 0;
    if (arr[i] > 0) {
      goToPositions[i] = 50;
      pinPositionsReceived = true;
    }
  }
}

int readWireAddress() {
  // We store wireAddress at the start of EEPROM
  int wireAddress = EEPROM.read(0);
  if (wireAddress != 255) {
    return wireAddress;
  }
  else {
    return i2cWireAddress;
  }
}

void TestMotors()
{
  goToPositions[0] = 20;
  goToPositions[1] = 30;
  goToPositions[3] = 40;
  goToPositions[4] = 50;
  pinPositionsReceived = true;
}

