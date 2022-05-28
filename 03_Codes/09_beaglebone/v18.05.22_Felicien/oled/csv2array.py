
# This example shows using two SSD1306_I2C attached to TCA9548A channels 0 and 1.
# Use with other I2C sensors would be similar.
import time
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import adafruit_tca9548a

# Create I2C bus as normal
i2c = board.I2C()
time.sleep(1)

# Create the TCA9548A object
# give it the I2C bus and the address of the multiplexer (from 0x70 to 0x77)
tca = adafruit_tca9548a.TCA9548A(i2c, address=0x70)
#tca1 = adafruit_tca9548a.TCA9548A(i2c, address=0x71)
#tca2 = adafruit_tca9548a.TCA9548A(i2c, address=0x72)
#tca3 = adafruit_tca9548a.TCA9548A(i2c, address=0x73)



# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 1
var = 35

# Create an array for the displays that represent the physical grid of oleds
disp = 0

displays = [
    [[0, disp], [0, disp], [0, disp], [0, disp]] #(0, 4), (0, 5), (0, 6), (0, 7)),
    #((1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)),
    #((2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)),
    #((3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)),
]

# For each oled display, create it using the TCA9548A channel instead of the I2C object and assign it to i$
##BE CAREFUL WITH ADDRESSING: tca[0] is SC0/SD0 on the TCA9548A!

#tca_count = -1
for row in displays:
    print(row)
    count = 0
    #tca_count = tca_count + 1
    for d in row: 
        if d[0] == 0:
            d[1] = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[count])
        elif tca_count == 1:
            d[1] = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca1[count])
        elif tca_count == 2:
            d[1] = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca2[count])
        elif tca_count == 3:
            d[1] = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca3[count])
        #print(count)
        print(d[1])
        count = count+1

########### DRAWING ON OLED1 ############
# Clear display.

for row in displays:
    for d in row:
        d[1].fill(0)
        d[1].show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (d[1].width, d[1].height))
        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Load font.
        font = ImageFont.load_default()
        
        # Draw Some Text
        text = "Hello!"
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (d[1].width // 2 - font_width // 2, d[1].height // 2 - font_height // 2),
            text,
            font=font,
            fill=255,
        ) 

        # Display image
        d[1].image(image)
        d[1].show()
