// OneBitDisplay library multi-display demo
// Demonstrates how to initialize and use multiple displays

#include <OneBitDisplay.h>
#include <SoftwareSerial.h>
#include <SerialTransfer.h>

// Use -1 for the Wire library default pins
// or specify the pin numbers to use with the Wire library or bit banging on any GPIO pins
// These are reversed because I did straight-through wiring for my SSD1306
// and it has the 4-pin header as GND,VCC,SCL,SDA, but the GROVE connector is
// GND,VCC,SDA,SCL
#define LCD1_SDA_PIN 15
#define LCD1_SCL_PIN 14

#define LCD2_SDA_PIN 17
#define LCD2_SCL_PIN 16

#define LCD3_SDA_PIN 19
#define LCD3_SCL_PIN 18

#define LCD4_SDA_PIN 20
#define LCD4_SCL_PIN 21
// Set this to -1 to disable or the GPIO pin number connected to the reset
// line of your display if it requires an external reset
#define RESET_PIN -1
// let ss_oled figure out the display address
#define OLED_ADDR -1
// don't rotate the display
#define FLIP180 0
// don't invert the display
#define INVERT 0
// Bit-Bang the I2C bus
#define USE_HW_I2C 1

// Change these if you're using different OLED displays
#define MY_OLED1 OLED_128x64
#define MY_OLED2 OLED_128x64
#define MY_OLED3 OLED_128x64
#define MY_OLED4 OLED_128x64

// 2 copies of the SSOLED structure. Each structure is about 56 bytes
// There is no limit to the number of simultaneous displays which can be controlled by ss_oled 
OBDISP obd[4];

#define TX_PIN 6 // Arduino transmit  YELLOW WIRE  labeled RX on printer
#define RX_PIN 5 // Arduino receive   GREEN WIRE   labeled TX on printer

String strAr[30];
bool hasRun = false;

void setup() 
{
  Serial.begin(38400);
  Serial.println("Ready");
  //getData();
}

void sendToDisplay(const char* ch, const char* ch2, const char* ch3, const char* ch4) {
  int rc;
  int rc2;
  int rc3;
  int rc4;
  // The I2C SDA/SCL pins set to -1 means to use the default Wire library
  // If pins were specified, they would be bit-banged in software
  // This isn't inferior to hw I2C and in fact allows you to go faster on certain CPUs
  // The reset pin is optional and I've only seen it needed on larger OLEDs (2.4")
  //    that can be configured as either SPI or I2C
  //
  // obdI2CInit(OBDISP *, type, oled_addr, rotate180, invert, bWire, SDA_PIN, SCL_PIN, RESET_PIN, speed)
  
  rc = obdI2CInit(&obd[0], MY_OLED1, OLED_ADDR, FLIP180, INVERT, 0, LCD1_SDA_PIN, LCD1_SCL_PIN, RESET_PIN, 400000L); // use standard I2C bus at 400Khz
    if (rc != OLED_NOT_FOUND)
    {
      obdFill(&obd[0], 0, 1);
      obdSetTextWrap(&obd[0], 1);
      obdWriteString(&obd[0], 0,0,0, (char*)ch, FONT_6x8, 0, 1);
    }
  rc2 = obdI2CInit(&obd[1], MY_OLED2, OLED_ADDR, FLIP180, INVERT, 0, LCD2_SDA_PIN, LCD2_SCL_PIN, RESET_PIN, 400000L); // use standard I2C bus at 400Khz
    if (rc2 != OLED_NOT_FOUND)
    {
      obdFill(&obd[1], 0, 1);
      obdSetTextWrap(&obd[1], 1);
      obdWriteString(&obd[1], 0,0,0, (char*)ch2, FONT_6x8, 0, 1);
    }
  
  rc3 = obdI2CInit(&obd[2], MY_OLED3, OLED_ADDR, FLIP180, INVERT, 0, LCD3_SDA_PIN, LCD3_SCL_PIN, RESET_PIN, 400000L); // use standard I2C bus at 400Khz
    if (rc3 != OLED_NOT_FOUND)
    {
      obdFill(&obd[2], 0, 1);
      obdSetTextWrap(&obd[2], 1);
      obdWriteString(&obd[2], 0,0,0,(char*)ch3, FONT_6x8, 0, 1);
    }
  rc4 = obdI2CInit(&obd[3], MY_OLED4, OLED_ADDR, FLIP180, INVERT, 0, LCD4_SDA_PIN, LCD4_SCL_PIN, RESET_PIN, 400000L); // use standard I2C bus at 400Khz
    if (rc4 != OLED_NOT_FOUND)
    {
      obdFill(&obd[3], 0, 1);
      obdSetTextWrap(&obd[3], 1);
      obdWriteString(&obd[3], 0,0,0, (char*)ch4, FONT_6x8, 0, 1);
    }
  
} /* setup() */

void getData() {
  
}

void loop() 
{ 
  const char* input_data = " ";

  if(!hasRun){
    if(Serial.available()){ 
        for(int i=0; i < 40; i++) {
          strAr[i] = Serial.readString();   // receive string from python
          Serial.println("str:" +strAr[i]);
        }
        hasRun = true;
    }
  }
  
  
  const char *ch = strAr[random(0, 30)].c_str();       // convert string to const char
  const char *ch2 = strAr[random(0, 30)].c_str();
  const char *ch3 = strAr[random(0, 30)].c_str();
  const char *ch4 = strAr[random(0, 30)].c_str();
      
  delay(4000);                        // somehow it's better to be sure the whole string was received
  sendToDisplay(ch, ch2, ch3, ch4);                  // send the converted string to displays
  
  //delay(100); 
} /* loop() */
