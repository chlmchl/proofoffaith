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

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 1

# For each oled display, create it using the TCA9548A channel instead of the I2C object
##BE CAREFUL WITH ADDRESSING: tca[0] is SC0/SD0 on the TCA9548A!
oled1 = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[0])
oled2 = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, tca[1])


############ DRAWING ON OLED1 ############
# Clear display.
oled1.fill(0)
oled1.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled1.width, oled1.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled1.width, oled1.height), outline=255, fill=255)

# Draw a smaller inner rectangle
draw.rectangle(
    (BORDER, BORDER, oled1.width - BORDER - 1, oled1.height - BORDER - 1),
    outline=0,
    fill=0,
)

# Load default font.
font = ImageFont.load_default()

# Draw Some Text
text = "Hello!"
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled1.width // 2 - font_width // 2, oled1.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)

# Display image
oled1.image(image)
oled1.show()


############DRAWING ON OLED2 ############
# Clear display.
oled2.fill(0)
oled2.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled2.width, oled2.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled2.width, oled2.height), outline=255, fill=255)

# Draw a smaller inner rectangle
draw.rectangle(
    (BORDER, BORDER, oled2.width - BORDER - 1, oled2.height - BORDER - 1),
    outline=0,
    fill=0,
)

# Load default font.
font = ImageFont.load_default()

# Draw Some Text
text = "Goodbye!"
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled2.width // 2 - font_width // 2, oled2.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)

# Display image
oled2.image(image)
oled2.show()
