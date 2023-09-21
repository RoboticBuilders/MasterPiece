
/*
 * This code is used to Run motors using a L298N motor driver
 * that can control two DC motors.
 * 
 * The L298N is connected to a SN74HC595N shift register.
 * The shift register is used to increase the Arduion pins.
 * 
 * This code writes out the appropriate bits to the shift register
 * so as to turn on the motor in the appropriate direction.
 * 
 * The idea here is to use the correct bit pattern to turn on the motor.
 * The L298N needs the bit pattern of 01 on pins N1,N2 to turn forward
 * and pattern 10 on the same pins for backward. 00 and 11 turn the motor off.
 * 
 * We connect the shift register outputs Q0-Q7 to the motor drivers.
 * Q0 -> M2
 * Q1 -> M1
 * Q2 -> M4
 * Q3 -> M3
 * (Same shift register, but on a second L298N)
 * Q4 -> M2
 * Q5 -> M1
 * Q6 -> M3
 * Q7 -> M2
 * 
 * This means the bit pattern: 10101010 (170) will turn all motors forward.
 * and the bit pattern 01010101(85) will turn all the motors backward.
  */

//Pin connected to ST_CP of 74HC595
int latchPin = 8;
//Pin connected to SH_CP of 74HC595
int clockPin = 12;
////Pin connected to DS of 74HC595
int dataPin = 11;

void setup() {
  // put your setup code here, to run once:

  //set pins to output because they are addressed in the main loop
  pinMode(latchPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  for (int j = 1; j < 8; j++) {
   //ground latchPin and hold low for as long as you are transmitting
    digitalWrite(latchPin, 0);

    Serial.print("\nWriting out : ");
    Serial.print(j);

    // Move out the bits. We are moving out the same bit pattern to both
    // registers.
    shiftOut(dataPin, clockPin, j);
    shiftOut(dataPin, clockPin, j);

    //return the latch pin high to signal chip that it
    //no longer needs to listen for information
    digitalWrite(latchPin, 1);

    delay(5000);
  }
}

void shiftOut(int myDataPin, int myClockPin, byte myDataOut) {

  // This shifts 8 bits out MSB first,
  //on the rising edge of the clock,
  //clock idles low
  //internal function setup

  int i=0;
  int pinState;

  pinMode(myClockPin, OUTPUT);
  pinMode(myDataPin, OUTPUT);

  //clear everything out just in case to
  //prepare shift register for bit shifting
  digitalWrite(myDataPin, 0);
  digitalWrite(myClockPin, 0);

  //for each bit in the byte myDataOut&#xFFFD;
  //NOTICE THAT WE ARE COUNTING DOWN in our for loop
  //This means that %00000001 or "1" will go through such
  //that it will be pin Q0 that lights.

  for (i=7; i>=0; i--)  {
    digitalWrite(myClockPin, 0);

    //if the value passed to myDataOut and a bitmask result
    // true then... so if we are at i=6 and our value is
    // %11010100 it would the code compares it to %01000000
    // and proceeds to set pinState to 1.

    if ( myDataOut & (1<<i) ) {
      pinState= 1;
    }
    else {
      pinState= 0;
    }

    //Sets the pin to HIGH or LOW depending on pinState
    digitalWrite(myDataPin, pinState);

    //register shifts bits on upstroke of clock pin
    digitalWrite(myClockPin, 1);

    //zero the data pin after shift to prevent bleed through
    digitalWrite(myDataPin, 0);
  }

  //stop shifting

  digitalWrite(myClockPin, 0);
}
