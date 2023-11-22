#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
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
                      { 3, 0, 0, 0},
                      { 3, 0, 3, 0},
                      { 3, 3, 3, 3},
                      { 0, 0, 3, 0}
                    },
                    {
                      { 3, 3, 0, 0},
                      { 0, 0, 3, 0},
                      { 0, 3, 0, 0},
                      { 3, 3, 3, 3}
                    },
                    {
                      { 3, 0, 0, 3},
                      { 3, 0, 0, 3},
                      { 3, 3, 3, 3},
                      { 0, 3, 3, 0}
                    }
                  };

int imageIndex = 0;

// Index of the image to display
int lastInput = -1;

bool imageRendered = false;

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup()
{
	// initialize the LCD and turn on backlight
	lcd.begin();
	lcd.backlight();
  
  WriteLcdAndWait("Reset pins", 12);

  Serial.begin(9600);
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
 
  // code for bluetooth
  int data = Serial.read();
  Serial.println(String(data));

  if (lastInput == data)
  {
    // entry for rendering the same image as before
    return;
  }

  lastInput = data;

  if (data == 0)
  {
    imageIndex = 1;
    Serial.println("rectangle");
  }
  else if (data == 1)
  {
    imageIndex = 2;
    Serial.println("circle");
  }
  else
  {
    // Image data to reset pins
    imageIndex = 0;
    Serial.println("Reset pins - clear");
  }

  // Send height instructions to each sub unit
  WriteToWire(0, 20);
  WriteToWire(1, 21);
  WriteToWire(2, 22);
  WriteToWire(3, 23);

  // Wait for the next cycle
  WriteLcdAndWait("Sent image: " + String(imageIndex), 20);

  delay(1000);
}

void WriteToWire(int row, int wireAddress) {
  Wire.beginTransmission(wireAddress); // transmit to device #8
  byte data = images[imageIndex][row][0] | images[imageIndex][row][1] << 2 | images[imageIndex][row][2] << 4 | images[imageIndex][row][3] << 6;
  Wire.write(data);              // sends one byte
  Wire.endTransmission();    // stop transmitting
}