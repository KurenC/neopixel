import time
import board
import neopixel
pixel_pin = board.GP18

num_pixels = 150

ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

counter = 0
firstColor = (0,0,255,0)
secondColor = (255,0,0,0)

while True:
    for index in range(num_pixels):
        counter = counter + 1
        if counter<=5:
            pixels[index] = firstColor
        else:
            pixels[index] = secondColor
        if counter>=10:
            counter=0
    pixels.show()
    tempColor = firstColor
    firstColor = secondColor
    secondColor = tempColor
    time.sleep(0.3)
