#include <LCD_I2C.h>

LCD_I2C lcd1(0x27);
LCD_I2C lcd2(0x26);
LCD_I2C lcd3(0x24);

void setup() {

  Serial.begin(9600);
  // put your setup code here, to run once:
  lcd1.begin();
  
  lcd1.backlight();
  lcd1.print("Blockchain should be used to replace a lot of centralized data");
  
  lcd2.begin();
  
  lcd2.backlight();
  lcd2.print("I'm 0x26");
  
 
  lcd3.begin();
  
  lcd3.backlight();
  
  lcd3.print("I'm 0x24");

}

void loop() {
  // put your main code here, to run repeatedly:
}
