
#include <AFMotor.h>
#include <Wire.h>
#include <EEPROM.h>

AF_DCMotor motor1(2);
AF_DCMotor motor2(3);
AF_DCMotor motor3(4);
AF_DCMotor motor4(1);

// I2C wire address for this unit. Make sure you set this to the right address before deploying. Valid addresses are {8, 9, 10, 11} from top to bottom row.
int i2cWireAddress = 8;

// State variable for each motor
volatile bool motor1_running = false;
volatile bool motor2_running = false;
volatile bool motor3_running = false;
volatile bool motor4_running = false;

void setup() {
  // Set motor speeds
  motor1.setSpeed(500);
  motor2.setSpeed(500);
  motor3.setSpeed(500);
  motor4.setSpeed(500);

  ReleaseAllMotors();

  // start serial for output
  Serial.begin(9600);  
  Serial.println("Reseting pins");

  // Reset all pins to lowest point
  ResetPins();
  
  Serial.println("Pins are reset");

  // read EEPROM for i2cWireAddress
  int wireAddress = readWireAddress();
  i2cWireAddress = wireAddress;
  Serial.print("Wire address ");
  Serial.println(wireAddress);

  // join I2C bus with the address for this sub Arduino
  Wire.begin(i2cWireAddress);     

  // Register a handler for data receive
  Wire.onReceive(receiveEvent);  
  Serial.println("Setup completed");   
}

void ResetPins() {
  // FORWARD | BACKWARD
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);

  delay(9000);

  ReleaseAllMotors();
}

void loop() {
  if (motor1_running | motor2_running | motor3_running | motor4_running) {
    // At least one motor should be running. Enter control loop.
    // Run the corresponding motor. Release the other ones.

    ResetPins();

    if (motor1_running) {
      Serial.print("Forward | ");
      motor1.run(FORWARD);
    } else {
      Serial.print("Released | ");
      motor1.run(RELEASE);
    }

    if (motor2_running) {
      Serial.print("Forward | ");
      motor2.run(FORWARD);
    } else {
      Serial.print("Released | ");
      motor2.run(RELEASE);
    }

    if (motor3_running) {
      Serial.print("Forward | ");
      motor3.run(FORWARD);
    } else {
      Serial.print("Released | ");
      motor3.run(RELEASE);
    }

    if (motor4_running) {
      Serial.print("Forward | ");
      motor4.run(FORWARD);
    } else {
      Serial.print("Released");
      motor4.run(RELEASE);
    }

      Serial.println("Loop");

    // Run motors for specified time
    delay(7000);

    // Reset motor state now that time has elapsed
    motor1_running = false;
    motor2_running = false;
    motor3_running = false;
    motor4_running = false;

    ReleaseAllMotors();

    // Wait for some time to allow users to feel/see the display
    //delay(6000);

    // Now reset it back to original state
    // ResetPins();
  }
  else {
    //Serial.println("Nothing to do");
  }

  // Delay for the control loop
  delay(5000);
}

void ReleaseAllMotors() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  Serial.print("receive event");
  Serial.println(howMany);
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

  // if the command is to reset Pins (all 0s then we can call ResetPins)
  if (x == 0) {
    Serial.println("Command to reset pins");
    ResetPins();
  }

  // Print for debug purposes
  for (int i = 0; i < 4; i++) {
    Serial.print(arr[i]);
  }
  Serial.println();

  // Set motor state for each motor that has a height >=1. The control loop uses this info to run the pin to the right height.
  // Currently, this state is a boolean corresponding to UP or DOWN, but we could change it to a int with 4 levels of height with the 2 bits we have
  // We can also redo the code here to accept 4 bytes instead of 1 to give each motor 1/256 units of motion - overkill for our motor setup.
  if (arr[0] > 0)
    motor1_running = true;

  if (arr[1] > 0)
    motor2_running = true;

  if (arr[2] > 0)
    motor3_running = true;

  if (arr[3] > 0)
    motor4_running = true;
}

int readWireAddress()
{
  // We store wireAddress at the start of EEPROM
  int wireAddress = EEPROM.read(0);
  if (wireAddress != 255)
  {
    return wireAddress;
  }
  else
  {
    return i2cWireAddress;
  }
}

void TestMotors()
{
  Serial.println(F("Testing motor1..."));
  TestMotor(motor1);
  delay(5000);
  Serial.println(F("Testing motor2..."));
  TestMotor(motor2);
  delay(5000);
  Serial.println(F("Testing motor3..."));
  TestMotor(motor3);
  delay(5000);
  Serial.println(F("Testing motor4..."));
  TestMotor(motor4);
}

void TestMotor(AF_DCMotor motor)
{
  motor.run(FORWARD);
  delay(7000);
  motor.run(BACKWARD);
  delay(7000);
  ReleaseAllMotors();
}
