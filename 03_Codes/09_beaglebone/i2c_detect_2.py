import board
import busio
import time
import smbus
import adafruit_tca9548a
import adafruit_ssd1306

class multiplex:
    
    def __init__(self, bus):
        self.bus = smbus.SMBus(bus)

    def channel(self, address=0x70,channel=0):  # values 0-3 indictae the channel, anything else (eg -1) turns off all channels
        
        if   (channel==0): action = 0x04
        elif (channel==1): action = 0x05
        elif (channel==2): action = 0x06
        elif (channel==3): action = 0x07
        else : action = 0x00

        self.bus.write_byte_data(address,0x04,action)  #0x04 is the register for switching channels 


if __name__ == '__main__':
    
    bus=2       # 0 for rev1 boards etc.
    address=0x70
    
    plexer = multiplex(bus)
    plexer.channel(address,3)
    
   # display1 = adafruit_ssd1306.SSD1306_I2C(128, 64, bus, addr=address)
    print ("Now run i2cdetect")
    print(bus)

