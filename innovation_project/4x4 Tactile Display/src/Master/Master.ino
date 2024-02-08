#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>
#include <stdlib.h>

//#define GANTRY_IMAGE 
//#define LCD_AVAILABLE


#ifdef  GANTRY_IMAGE
int images[6][12][20] =
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
  },
}; 
#else
int images[6][4][4] = 
                  { 
                    {
                      { 3, 3, 3, 3},
                      { 3, 0, 0, 3},
                      { 3, 0, 0, 3},
                      { 3, 3, 3, 3}
                    },                   
                    {
                      { 0, 3, 3, 0},
                      { 3, 0, 0, 3},
                      { 3, 0, 0, 3},
                      { 0, 3, 3, 0}
                    },
                    {
                      {0, 3, 3, 0},
                      {3, 3, 3, 3},
                      {0, 3, 3, 0},
                      {0, 3, 3, 0}
                
                    }
                  };
#endif

int imageIndex = -1;
int imageIndexForResettingPins = 100;

// Index of the image to display
String input = String("");
String lastInput = String("");
SoftwareSerial BTSerial(10, 11); // RX | TX

// smallest wire address for the 4x4 array
#ifdef  GANTRY_IMAGE
int subStartWireAddress = 8;
#else
int subStartWireAddress = 21;
#endif

#ifdef LCD_AVAILABLE
// Set the LCD address to 0x27 for a 16 chars and 2 line display
LiquidCrystal_I2C lcd(0x27, 16, 2);
#endif
void setup()
{
 #ifdef LCD_AVAILABLE 
	// initialize the LCD and turn on backlight
  lcd.begin();
	lcd.backlight();
   WriteLcdAndWait("Reset pins", 2);
 #endif
  Wire.begin();
  
  Serial.begin(9600);
  BTSerial.begin(19200);
  Serial.println("Primary Setup completed");
}

#ifdef LCD_AVAILABLE
void WriteLcdAndWait(String text, int waitTimeSeconds) {

    for(int i = waitTimeSeconds; i > 0; i--) {
      lcd.clear();
      lcd.print(text);
      lcd.setCursor(0, 1);
      lcd.print("Waiting... " + String(i));
      delay(1000);
  }
}
#endif

void loop() {  
  
  // for now we just render one image
  if (BTSerial.available()) {
    input = BTSerial.readString();
    Serial.print("input = ");
    Serial.println(input);

    if (input.equals("0"))
    {
      imageIndex = 0;
      Serial.println("rectangle");
    }
    else if (input.equals("1"))
    {
      imageIndex = 1;
      Serial.println("circle");
    }
    else if (input.equals("2"))
    {
      imageIndex = 2;
      Serial.println("house");
    }
    else if (input.equals("9"))
    {
     // Image data to reset pins
      imageIndex = imageIndexForResettingPins;
      Serial.println(input);
      Serial.println("Reset pins - clear");
    }
    else
    {
     // Image data to reset pins
      imageIndex = imageIndexForResettingPins;
      Serial.println(input);
      Serial.println("Reset pins - clear");
    }

    delay(1000);
  }

  if ((lastInput.equals("") && input.equals("")) || (lastInput.equals(input)))
  {
    return;
  }
 
  lastInput = input;
  
   if (imageIndex == -1)
    return;


#ifdef GANTRY_IMAGE

for (int i = 0; i < 12; i++)
{
  // one row in 5 frames
  WriteToWire(imageIndex, i, subStartWireAddress, 0, 3);
  WriteToWire(imageIndex, i, subStartWireAddress + 1, 4, 7);
  WriteToWire(imageIndex, i, subStartWireAddress + 2, 8, 11);
  WriteToWire(imageIndex, i, subStartWireAddress + 3, 12, 15);
  WriteToWire(imageIndex, i, subStartWireAddress + 4, 16, 19);
  delay (10000);
}
#else
  // Send height instructions to each sub unit
  WriteToWire(imageIndex, 0, subStartWireAddress, 0, 3);
  WriteToWire(imageIndex, 1, subStartWireAddress + 1, 0, 3);
  WriteToWire(imageIndex, 2, subStartWireAddress + 2, 0, 3);
  WriteToWire(imageIndex, 3, subStartWireAddress + 3, 0, 3);
#endif  
  // Wait for the next cycle
  //WriteLcdAndWait("Sent image: " + String(imageIndex), 20);
  Serial.println(F("All data sent"));
  delay(300);
}

void WriteToWire(int imageNumber, int row, int wireAddress, int startIndex, int endIndex) {
  Serial.println("Sending data to " + String(wireAddress) + " for imageNumber " + String(imageNumber));
  delay(1000);
  Wire.beginTransmission(wireAddress); // transmit to device #8
  
  byte data = 0; // data for resetting pins

  if (imageNumber != imageIndexForResettingPins)
  {
    data = images[imageNumber][row][startIndex] | images[imageNumber][row][startIndex + 1] << 2 | images[imageNumber][row][startIndex + 2] << 4 | images[imageNumber][row][startIndex + 3] << 6;
  }

  Wire.write(data);          // sends one byte
  Wire.endTransmission();    // stop transmitting
}
