import random
import time
import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.GP18

# The number of NeoPixels
num_pixels = 50

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER)

GREEN = (255, 0, 0, 0)
RED = (0, 255, 0, 0)
BLUE = (0, 0, 255, 0)
FAKEWHITE = (255, 255, 255, 0)
WHITE = (0, 0, 0, 255)
ALLON = (255, 255, 255, 255)
OFF = (0, 0, 0, 0)
# green, red, blue, white

pixels.fill(GREEN)
pixels.show()
time.sleep(1)

pixels.fill(RED)
pixels.show()
time.sleep(1)

pixels.fill(BLUE)
pixels.show()
time.sleep(1)

pixels.fill(WHITE)
pixels.show()
time.sleep(1)

pixels.fill(FAKEWHITE)
pixels.show()
time.sleep(1)

pixels.fill(ALLON)
pixels.show()
time.sleep(1)

pixels.fill(OFF)
pixels.show()
time.sleep(1)

while True:
    for i in range(num_pixels):
        color = fancy.CHSV(random.randint(0, 255),255,255)
        color2 = fancy.CRGB(color)
        color3 = int(color2[0]*255), int(color2[1]*255), int(color2[2]*255), 0
        pixels[i] = color3
    pixels.show()
    time.sleep(2)

