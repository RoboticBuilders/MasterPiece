#include <SoftwareSerial.h>

// https://www.instructables.com/AT-command-mode-of-HC-05-Bluetooth-module/
// press red button before powering arduino and see the slow blink
// important part is to change Newline in serial mopnitor to "Both BL & CR"
// https://www.instructables.com/Modify-The-HC-05-Bluetooth-Module-Defaults-Using-A/


SoftwareSerial BTSerial(10, 11); // RX | TX

void setup() {
  pinMode(9, OUTPUT);
  // this pin will pull the HC-05 pin 34 (key pin) HIGH to switch module to AT mode
  digitalWrite(9, HIGH);
  Serial.begin(9600);
  Serial.println("Enter AT commands:");
  BTSerial.begin(38400);
  // HC-05 default speed in AT command more
}

void loop() {
  // Keep reading from HC-05 and send to Arduino Serial Monitor
  if (BTSerial.available())
    Serial.write(BTSerial.read());

  // Keep reading from Arduino Serial Monitor and send to HC-05
  if (Serial.available())
    BTSerial.write(Serial.read());
}