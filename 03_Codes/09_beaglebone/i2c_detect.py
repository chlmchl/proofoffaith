# This example shows using two TSL2491 light sensors attached to TCA9548A channels 0 and 1.
# Use with other I2C sensors would be similar.
import time
import board
import busio
import adafruit_tca9548a
import adafruit_ssd1306

# Create I2C bus as normal
i2c = busio.I2C(board.SCL, board.SDA)
time.sleep(1)
print(board.SDA)

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)
time.sleep(1)
print(tca)
print(i2c)

# For each sensor, create it using the TCA9548A channel instead of the I2C object
display1 = adafruit_ssd1306.SSD1306_I2C(128, 64, tca[0])

# Loop and profit!
while True:
    #display1.fill(0)
    time.sleep(0.1)