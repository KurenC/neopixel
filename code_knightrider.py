# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.GP18

# The number of NeoPixels
num_pixels = 5


# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)
pixels.fill((0,0,0,0))
pixels.show()
time.sleep(1)


reddot = 0
reverse = False;
while True:
    for i in range(num_pixels):
        if reddot == i:
            pixels[i] = (255, 0, 0, 0)
        else:
            pixels[i] = (63, 0, 0, 0)

    pixels.show()
    time.sleep(0.1)

    if reddot >= num_pixels-1:
        reverse = True
    if reddot == 0:
        reverse = False
    if reverse:
        reddot = reddot - 1
    else:
        reddot = reddot + 1


