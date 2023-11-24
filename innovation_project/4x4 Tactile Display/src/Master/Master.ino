#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>
#include <stdlib.h>

int images[6][4][4] = 
                  { 
                    {
                      { 0, 0, 0, 0},
                      { 0, 0, 0, 0},
                      { 0, 0, 0, 0},
                      { 0, 0, 0, 0}
                    },
                    {
                      { 0, 0, 0, 0},
                      { 3, 3, 3, 3},
                      { 3, 3, 3, 3},
                      { 0, 0, 0, 0}
                    },                   
                    {
                      { 0, 3, 3, 0},
                      { 3, 0, 0, 3},
                      { 3, 0, 0, 3},
                      { 0, 3, 3, 0}
                    },
                    {
                      {3, 0, 3, 0},
                      {3, 0, 3, 0},
                      {3, 3, 3, 3},
                      {0, 0, 3, 0}
                
                    }
                  };

int imageIndex = -1;

// Index of the image to display
String input = String("");
String lastInput = String("");
SoftwareSerial BTSerial(10, 11); // RX | TX

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup()
{
	// initialize the LCD and turn on backlight
	lcd.begin();
	lcd.backlight();
  
  WriteLcdAndWait("Reset pins", 2);

  Serial.begin(9600);
  BTSerial.begin(19200);
  Serial.println("Setup");
}

void WriteLcdAndWait(String text, int waitTimeSeconds) {

    for(int i = waitTimeSeconds; i > 0; i--) {
      lcd.clear();
      lcd.print(text);
      lcd.setCursor(0, 1);
      lcd.print("Waiting... " + String(i));
      delay(1000);
  }
}

void loop() {  
  
  // for now we just render one image
  if (BTSerial.available()) {
    input = BTSerial.readString();
    Serial.print("input = ");
    Serial.println(input);

    if (input.equals("0"))
    {
      imageIndex = 1;
      Serial.println("rectangle");
    }
    else if (input.equals("1"))
    {
      imageIndex = 2;
      Serial.println("circle");
    }
    else
    {
     // Image data to reset pins
      imageIndex = 0;
      Serial.println(input);
      Serial.println("Reset pins - clear");
    }

    delay(1000);
  }

  if ((lastInput.equals("") && input.equals("")) || (lastInput.equals(input)))
  {
    //Serial.println(F("no input"));
    return;
  }

  lastInput = input;
  
   if (imageIndex == -1)
    return;

  // Send height instructions to each sub unit
  WriteToWire(0, 20);
  WriteToWire(1, 21);
  WriteToWire(2, 22);
  WriteToWire(3, 23);
  
  // Wait for the next cycle
  //WriteLcdAndWait("Sent image: " + String(imageIndex), 20);

  delay(300);
}

void WriteToWire(int row, int wireAddress) {
  Serial.println("Sending data to " + String(wireAddress) + " for imageIndex " + String(imageIndex));
  delay(1000);
  Wire.beginTransmission(wireAddress); // transmit to device #8
  byte data = images[imageIndex][row][0] | images[imageIndex][row][1] << 2 | images[imageIndex][row][2] << 4 | images[imageIndex][row][3] << 6;
  Wire.write(data);              // sends one byte
  Wire.endTransmission();    // stop transmitting
}