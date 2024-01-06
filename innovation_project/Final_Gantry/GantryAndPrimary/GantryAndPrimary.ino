#include <Stepper.h>

// gantry motor initialization
const int STEPS_PER_REV = 240;
const int numberOfMotorStepsForOneGantryStep = 120;

const int motorSpeed = 20;
const int TotalNumberOfGantryStepsForFullSpan = 30;

const int motorIn1 = 2;
const int motorIn2 = 3;
const int motorIn3 = 4;
const int motorIn4 = 5;

enum GantryDirection
{
  TowardsMotor,
  AwayFromMotor
};

Stepper stepper(STEPS_PER_REV, motorIn1, motorIn2, motorIn3, motorIn4);

// control variables
bool gantryHasRun = true;

// Index of the image to display
int imageIndex = -1;
int imageIndexForResettingPins = 100;

String btInput = String("");
String lastBTInput = String("");
SoftwareSerial BTSerial(10, 11); // RX | TX

int secondaryStartWireAddress = 51;

void setup() {
  Wire.begin();
  Serial.begin(9600);
  BTSerial.begin(19200);
 
  Serial.println("Primary Setup completed");
}

void loop() {
  / for now we just render one image
  if (BTSerial.available()) {
    btInput = BTSerial.readString();
    Serial.print("input = ");
    Serial.println(btInput);

    if (btInput.equals("0"))
    {
      imageIndex = 0;
      Serial.println("rectangle");
    }
    else
    {
     // Image data to reset pins
      imageIndex = imageIndexForResettingPins;
      Serial.println(btInput);
      Serial.println("Reset pins - clear");
    }

    delay(1000);
  }

  if ((lastBTInput.equals("") && btInput.equals("")) || (lastBTInput.equals(btInput)))
  {
    return;
  }

  lastBTInput = btInput;

  if (imageIndex == -1)
    return;

  for (int i = 0; i < 20; i++)
  {
    // one row in 5 frames
    WriteToWire(imageIndex, i, secondaryStartWireAddress, 0, 3);
    WriteToWire(imageIndex, i, secondaryStartWireAddress + 1, 4, 7);
    WriteToWire(imageIndex, i, secondaryStartWireAddress + 2, 8, 11);
    WriteToWire(imageIndex, i, secondaryStartWireAddress + 3, 12, 15);
    WriteToWire(imageIndex, i, secondaryStartWireAddress + 4, 16, 19);
  }

    // Wait for all motor arrays to render the row
  delay(10000);
  moveBewelScrewInSteps (1, GantryDirection::AwayFromMotor, 0);
  delay(1000);
       
}

// this method rotates motor to move gantry in steps
void moveBewelScrewInSteps(int numberOfGantrySteps, GantryDirection direction, int delayBetweenSteps)
{
    stepper.setSpeed(motorSpeed);
    int directionMultiplier = direction == GantryDirection::AwayFromMotor ? 1 : -1;
    for(int i = 0; i < numberOfGantrySteps; i++) {
      stepper.step(directionMultiplier * numberOfMotorStepsForOneGantryStep);
      delay(delayBetweenSteps);
    }
}

int images[6][20][20] =
{
  {
    { 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3},
    { 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
    { 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3},
    { 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3},
    { 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3},
    { 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3},
    { 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3},
    { 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3},
    { 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3},
    { 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3},
    { 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
    { 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3},
    { 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3},
    { 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3},
    { 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3},
    { 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3},
  },
}; 

