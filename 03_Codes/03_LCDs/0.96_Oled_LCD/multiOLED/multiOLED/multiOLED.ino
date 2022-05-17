   #include <SPI.h>
   #include <Wire.h>
   #include <Adafruit_GFX.h>
   #include <Adafruit_SSD1306.h>

  #include <Multi_BitBang.h>
  #include <Multi_OLED.h>
  
  
  #define NUM_DISPLAYS 3
  #define NUM_BUSES 3
  // I2C bus info
  uint8_t scl_list[NUM_BUSES] = {0x15,0x15, 0x15}; //{9,9,9,9};
  uint8_t sda_list[NUM_BUSES] = {0x0F, 0x10, 0x11}; //{5,6,7,8};
  int32_t speed_list[NUM_BUSES] = {400000L, 400000L, 400000L};
  // OLED display info
  uint8_t bus_list[NUM_DISPLAYS] = {0,1,2}; // can be multiple displays per bus
  uint8_t addr_list[NUM_DISPLAYS] = {0x3c, 0x3c, 0x3c};
  uint8_t type_list[NUM_DISPLAYS] = {OLED_128x64, OLED_128x64, OLED_128x64};
  uint8_t flip_list[NUM_DISPLAYS] = {0,0,0};
  uint8_t invert_list[NUM_DISPLAYS] = {0,0,0};


void setup() {
  Serial.begin(9600);
 
  
  // put your setup code here, to run once:
  Multi_I2CInit(sda_list, scl_list, speed_list, NUM_BUSES);
  Multi_OLEDInit(bus_list, addr_list, type_list, flip_list, invert_list, NUM_DISPLAYS);
  Multi_OLEDFill(0, 0);
  Multi_OLEDSetContrast(0, 255);
  Multi_OLEDFill(1, 0);
  Multi_OLEDSetContrast(1, 255);
  Multi_OLEDFill(2, 0);
  Multi_OLEDSetContrast(2, 255);
  
} // setup

void loop() {
  // put your main code here, to run repeatedly:
  Multi_OLEDFill(0, 0); 
  Multi_OLEDFill(1, 0);
  Multi_OLEDFill(2, 0);

  
  Multi_OLEDWriteString(0, 0, 0, (char *)"proof", 2, 0); 
  delay(500);  
  Multi_OLEDWriteString(1, 0, 0, (char *)"of", 2, 0);
  delay(500);  
  Multi_OLEDWriteString(2, 0, 0, (char *)"faith", 2, 0);  
  delay(5000);
  Multi_OLEDFill(0, 0); 
  Multi_OLEDFill(1, 0);
  Multi_OLEDFill(2, 0);  
  delay(1000);
  Multi_OLEDWriteString(0, 0, 0, (char *)"Blockchain and crypto is so exciting. I think it will revolutionsise the world in the way the internet has. ", 2, 0);
  delay(500);   
  Multi_OLEDWriteString(1, 0, 0, (char *)"No groundbreaking idea from the blockchain will come from a college campus", 2, 0);
  delay(500);  
  Multi_OLEDWriteString(2, 0, 0, (char *)"Forgot to mention... We don&#39;t need bitcoin. It&#39;s worthless and will burst making a lot of people cry one day.", 2, 0);  
  delay(600);   
} // loop
