#include <Stepper.h>
#include <Wire.h> 
#include <SoftwareSerial.h>


// gantry motor initialization
const int STEPS_PER_REV = 240;
const int numberOfMotorStepsForOneGantryStep = 960;

const int motorSpeed = 70;
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

//#define HOUSE2
//#define GREATWAVE
#ifdef GREATWAVE
int images[1][16][16] =
{
   // Great Wave Array from Anya
  {
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0},
    {0, 0, 3, 3, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 3, 3, 3, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 3, 0},
    {0, 0, 0, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0},
    {0, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0},
    {0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0},
    {0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 0}
  }
};
#elif HOUSE2
int images[1][16][16] =
{
   // House Array from Anya
  {
    {0, 3,  3,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0},
    {0, 0,  0,  0,  3,  3,  0,  0,  0,  0,  0,  3,  0,  0,  0, 0},
    {0, 0,  0,  0,  3,  3,  3,  3,  3,  3,  3,  3,  3,  0,  0, 0},
    {0, 0,  0,  3,  3,  3,  3,  0,  0,  0,  0,  0,  0,  3,  0, 0},
    {0, 0,  3,  3,  3,  3,  3,  3,  0,  0,  0,  0,  0,  0,  0, 0},
    {0, 0,  3,  0,  3,  3,  0,  3,  0,  0,  0,  0,  0,  0,  0, 0},
    {0, 3,  3,  0,  0,  0,  0,  3,  3,  0,  0,  0,  0,  0,  3, 0},
    {0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  3,  3,  3,  3, 0},
    {0, 0,  0,  3,  3,  3,  3,  0,  0,  0,  3,  3,  3,  3,  0, 0},
    {0, 0,  0,  3,  0,  0,  3,  0,  0,  0,  3,  0,  0,  3,  0, 0},
    {0, 0,  0,  3,  3,  3,  3,  0,  3,  0,  3,  0,  0,  3,  0, 0},
    {0, 0,  0,  3,  3,  3,  3,  0,  0,  0,  3,  3,  3,  0,  0, 0},
    {0, 0,  3,  3,  0,  0,  0,  0,  0,  0,  0,  3,  3,  3,  3, 0},
    {0, 3,  3,  0,  3,  0,  3,  3,  3,  3,  3,  3,  3,  3,  3, 0}
  }
};

#else
int images[1][16][16] =
{
  //  0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
  {
    { 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0},  // 0
    { 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0},  // 1
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 2
    { 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0},  // 3
    { 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0},  // 4
    { 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0},  // 5
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 6
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 7
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 8
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 9
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 0
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 1
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 2
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 3
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0},  // 4
    { 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0}   // 5
  }
};
#endif

// Index of the image to display
int imageIndex = -1;
int imageIndexForResettingPins = 100;

String input = String("");
String lastInput = String("");
SoftwareSerial BTSerial(10, 11); // RX | TX

int secondaryStartWireAddress = 51;

void setup() {
  Wire.begin();
  Serial.begin(9600);
  BTSerial.begin(19200);
 
  Serial.println(F("Primary Setup completed"));
}

void loop() {
  // for now we just render one image
  // for now we just render one image
  if (BTSerial.available()) {
    input = BTSerial.readString();
    Serial.print("input = ");
    Serial.println(input);

    if (input.equals("0"))
    {
      imageIndex = -1;
      Serial.println("rectangle");
    }
    else if (input.equals("1"))
    {
      imageIndex = -1;
      Serial.println("circle");
    }
    else if (input.equals("2"))
    {
      imageIndex = 0;
      Serial.println("house");
    }
    else
    {
     // Image data to reset pins
      imageIndex = imageIndexForResettingPins;
      Serial.println(input);
      Serial.println("Reset pins - clear");
    }

    delay(300);
  }
  else
  {
    //imageIndex = 0;
    //input = "0";
  }

  if ((lastInput.equals("") && input.equals("")) || (lastInput.equals(input)))
  {
    return;
  }

  lastInput = input;

  if (imageIndex == -1)
    return;

  Serial.println("image index = " + String(imageIndex));
  
  for (int i = 5; i >= 0; i--)
  {
    // one row in 5 frames
    WriteToWire(imageIndex, i, secondaryStartWireAddress, 0, 3);
    WriteToWire(imageIndex, i, secondaryStartWireAddress + 1, 4, 7);
    WriteToWire(imageIndex, i, secondaryStartWireAddress + 2, 8, 11);
    WriteToWire(imageIndex, i, secondaryStartWireAddress + 3, 12, 15);
 
    // Wait for all motor arrays to render the row
    delay(3000);
    moveBewelScrewInSteps(1, GantryDirection::TowardsMotor, 0);
  }

  moveBewelScrewInSteps(6, GantryDirection::AwayFromMotor, 0);

  delay(1000);       
}

// this method rotates motor to move gantry in steps
void moveBewelScrewInSteps(int numberOfGantrySteps, GantryDirection direction, int delayBetweenSteps)
{
    stepper.setSpeed(motorSpeed);
    int directionMultiplier = direction == GantryDirection::AwayFromMotor ? -1 : 1;
    for(int i = 0; i < numberOfGantrySteps; i++) {
      stepper.step(directionMultiplier * numberOfMotorStepsForOneGantryStep);
      delay(delayBetweenSteps);
    }
}

void WriteToWire(int imageNumber, int row, int wireAddress, int startIndex, int endIndex) {
  Serial.println("Sending data to " + String(wireAddress) + " for imageNumber " + String(imageNumber));
  Wire.beginTransmission(wireAddress); // transmit to device #8
  
  byte data = 0; // data for resetting pins

  if (imageNumber != imageIndexForResettingPins)
  {
    data = images[imageNumber][row][startIndex] | images[imageNumber][row][startIndex + 1] << 2 | images[imageNumber][row][startIndex + 2] << 4 | images[imageNumber][row][startIndex + 3] << 6;
  }
  Serial.print(F("data = "));
  Serial.println(data);
  Wire.write(data);          // sends one byte
  Wire.endTransmission();    // stop transmitting
}

