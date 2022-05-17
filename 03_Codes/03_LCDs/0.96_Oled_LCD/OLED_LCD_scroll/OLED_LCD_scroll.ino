/* https://www.youtube.com/watch?v=sTYPuDMPva8
   Set the appropriate screen size in the Adafruit_SSD1306.h by uncommenting
   one of the two following lines.

   //#define SSD1306_128_64 ///< DEPRECTAED: old way to specify 128x64 screen
   //#define SSD1306_128_32 ///< DEPRECATED: old way to specify 128x32 screen
*/
   #include <SPI.h>
   #include <Wire.h>
   #include <Adafruit_GFX.h>
   #include <Adafruit_SSD1306.h>

   #define SCREEN_WIDTH 128 // OLED display width, in pixels
   #define SCREEN_HEIGHT 64 // OLED display height, in pixels
   #define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
   #define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
   Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

   char message[]="297M LstWyPt, 345M StPt, rec#89";
   int x, minX;

  void setup(){
  Serial.begin(9600);
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }
  
 
  x = display.width();
  minX = -12 * strlen(message);  // 12 = 6 pixels/character * text size 2
  testdrawchar();
  }

  void loop(){
  }

  void testdrawchar(void) {
       
   display.clearDisplay();
   display.setCursor(0,0);
   display.setTextSize(1);
   display.print("Sat:13  03:56:32  67%");// GPS # Satellites, Time, % Batt chg
   display.setTextSize(2);
   display.setCursor(x,10);
   display.print(message);
   display.setCursor(x,28);
   display.setTextSize(1);
   display.print("Press #1 New StPt, 2 RecWayPt, Cur 32.567, -102.456");
   display.setCursor(x,38);
   display.setTextSize(1);
   display.print("Press #1 New StPt, 2 RecWayPt, Cur 32.567, -102.456");
   display.setCursor(x,48);
   display.setTextSize(1);
   display.print("Press #1 New StPt, 2 RecWayPt, Cur 32.567, -102.456");
  }
