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


void setup() {
    Serial.begin(9600);
    moveBewelScrewInSteps(9, GantryDirection::AwayFromMotor, 1000);
}

void loop() {
  if (gantryHasRun == false) {
    moveBewelScrewInSteps(33, GantryDirection::TowardsMotor, 1000);
    gantryHasRun = true;
  }
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

