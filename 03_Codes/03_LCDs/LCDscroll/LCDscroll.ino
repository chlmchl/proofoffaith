#include <LiquidCrystal.h>
#include <LCD_I2C.h>
float counter;


LCD_I2C lcd(0x27);

void setup() {

  Serial.begin(9600);
  // put your setup code here, to run once:
  lcd.begin(); 
  lcd.backlight();
  lcd.print("Blockchain should be used to replace a lot of centralized data");

}

void loop() {
  // put your main code here, to run repeatedly:
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Blockchain should be used to replace a lot of centralized data");
  //lcd.setCursor(0, 1);
  //lcd.print("replace a lot of centralized data");
  for(counter = 0; counter <24; counter++)
   {
    lcd.setCursor(0,0);
    lcd.scrollDisplayLeft();
    delay(1000);
    }
}
