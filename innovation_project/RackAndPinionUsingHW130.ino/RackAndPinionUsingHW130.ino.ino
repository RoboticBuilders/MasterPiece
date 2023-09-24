#include <AFMotor.h>
#include <assert.h>

const int SPEED = 50;

typedef struct FourMotorBlock {
  AF_DCMotor motors[4] = {
    AF_DCMotor(1),
    AF_DCMotor(2),
    AF_DCMotor(3),
    AF_DCMotor(4)
  };

  int upTimeMs[4] = {
    333,
    640,
    428,
    385
  };

  int downTimeMs[4] = {
    315,
    650,
    390,
    385
  };
  
  const int NUM_MOTORS = 4;
} MotorBlock;

MotorBlock motorBlock1;

void initializeMotorBlock(MotorBlock* motorBlock) {
  for (int i = 0; i < motorBlock->NUM_MOTORS; ++i) {
    motorBlock->motors[i].setSpeed(SPEED);
    motorBlock->motors[i].run(RELEASE);
  }
}

// Motors are numbered from one in a motor block.
void turnOnMotorForTime(MotorBlock* motorBlock, uint8_t motor_number, uint8_t direction) {
  assert(motor_number >=1 && motor_number <= 4);
  motor_number = motor_number - 1;
  
  AF_DCMotor* motors = motorBlock->motors;
  Serial.print("Turning on motor : ");
  Serial.print(motor_number);
  motors[motor_number].run(direction);
  motors[motor_number].setSpeed(SPEED); 

  // wait for the specified amount of time.
  if (direction == FORWARD) {
    delay(motorBlock->upTimeMs[motor_number]);
  } else {
    delay(motorBlock->downTimeMs[motor_number]);
  }

  motors[motor_number].setSpeed(0); 
  motors[motor_number].run(RELEASE);
  Serial.print("   Turning off motor\n");
}

void turnOffAllMotors(MotorBlock* motorBlock) {
  AF_DCMotor* motors = motorBlock->motors;
  // Turn off all motors. Do it in the same 
  // order in which we started so any slight 
  // delays in the start are also accounted for.
  for (int i = 0; i < motorBlock->NUM_MOTORS; ++i) {
    motors[i].setSpeed(0); 
    motors[i].run(RELEASE);
  }
}

void setup() 
{
  Serial.begin(9600);
  initializeMotorBlock(&motorBlock1);
  turnOffAllMotors(&motorBlock1);
}

void loop()
{
  turnOffAllMotors(&motorBlock1);
  delay(15000);
  
  /*
  for (int i = 1; i <=4; ++i) {
    turnOnMotorForTime(&motorBlock1, i, FORWARD);  
    delay(1000);
  }
  delay(5000);
  for (int i = 1; i <=4; ++i) {
    turnOnMotorForTime(&motorBlock1, i, BACKWARD);  
    delay(1000);
  }
  */
}
