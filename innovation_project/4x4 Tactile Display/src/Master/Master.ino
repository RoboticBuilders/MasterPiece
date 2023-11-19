#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <stdlib.h>

int images[5][4][4] = 
                  {                    
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

int imageCount = 3;

// Index of the image to display
int imageIndex = 0;

// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup()
{
	// initialize the LCD and turn on backlight
	//lcd.begin();
	//lcd.backlight();
  
  WriteLcdAndWait("Reset pins", 12);
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
  // Send height instructions to each sub unit
  WriteToWire(0, 8);
  WriteToWire(1, 9);
  WriteToWire(2, 10);
  WriteToWire(3, 11);

  // Wait for the next cycle
  WriteLcdAndWait("Sent image: " + String(imageIndex), 20);

  // Increment image index, and reset to zero if needed.
  imageIndex++;
  if (imageIndex == imageCount) 
    imageIndex = 0; 

}

void WriteToWire(int row, int wireAddress) {
  Wire.beginTransmission(wireAddress); // transmit to device #8
  byte data = images[imageIndex][row][0] | images[imageIndex][row][1] << 2 | images[imageIndex][row][2] << 4 | images[imageIndex][row][3] << 6;
  Wire.write(data);              // sends one byte
  Wire.endTransmission();    // stop transmitting
}