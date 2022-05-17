
#include <gfxfont.h>
#include <Adafruit_GFX.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <Fonts/Org_01.h>


#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
// The pins for I2C are defined by the Wire-library. 
// On an arduino UNO:       A4(SDA), A5(SCL)
// On an arduino MEGA 2560: 20(SDA), 21(SCL)
// On an arduino LEONARDO:   2(SDA),  3(SCL), ...
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  //testdrawrect();
  //delay(2000); // Pause for 2 seconds

  // Clear the buffer
  display.clearDisplay();

  testdrawchar();
}

void loop() {
  // put your main code here, to run repeatedly:

}

void testdrawrect(void) {
  display.clearDisplay();

  for(int16_t i=0; i<display.height()/2; i+=2) {
    display.drawRect(i, i, display.width()-2*i, display.height()-2*i, SSD1306_WHITE);
    display.display(); // Update screen with each newly-drawn rectangle
    delay(1);
  }

  delay(2000);
}

void testdrawchar(void) {
  display.clearDisplay();
  display.setTextSize(1);      // Normal 1:1 pixel scale
  display.setFont(&Org_01);
  display.setTextWrap(true);
  display.setTextColor(SSD1306_WHITE); // Draw white text
  display.setCursor(0, 5);     // Start at top-left corner
  display.println(F("Blockchain should be used to replace a lot of centralized data. So like social security and identity info.  You could have a registry blockchain for individual owner blockchains to join.  This would record all individual owners...  Replacing the social security system for id and all it is used for.  As an individual chain owner, you would be an oracle over certain property types of information (like gender, location, age, whatever is personal), and locked down for the impersonal items.  Those are the only properties to your id blockchain that the registry cares about (or should).  Then you could have various registry blockchains to register your individual chain to.  Allowing you to share whatever specific items from your chain with the new registry.  These registries can be the various markets/areas of interest a company could be.  Like advertising companies.  Or youtube.  Or anything where personal information is used.  However, this would enable individuals control and potentially contractual activity for data from their chain.  Like assigning royalty payouts to say, location data.  This way if a registry wants your location data, the registry has to give you something in return."));         // Use full 256 char 'Code Page 437' font

  // Not all the characters will fit on the display. This is normal.
  // Library will draw what it can and the rest will be clipped.
  /*for(int16_t i=0; i<256; i++) {
    if(i == '\n') display.write(' ');
    else          display.write(i);
  }*/

  display.display();
  delay(2000);

  // scroll
  //display.startscrollleft(0x00, 0x0F);
  //delay(2000);
}
