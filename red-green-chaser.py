# Rich Whiffen - 11/21/2022 - lots of lifted code here
#
# Mostly taken from the Adafruit learn guides.
# https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
#
# alternating red and green colors and then have
# a "brightness train" run around the tree.
#

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 350
DELAY=0.05

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
pixel_yellow = (255, 100, 0)
pixel_orange = (255, 50, 0)
pixel_red = (0, 255, 0)
pixel_blue = (0, 0, 255)
pixel_green = (255, 0, 0)
pixel_off = (0, 0, 0)

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

# set the inital red/green pattern.
for i in range(num_pixels):
    if i % 2:
        pixels[i] = pixel_red
    else:
        pixels[i] = pixel_green

pixels.show()

while True:

    for i in range(num_pixels):  #I may have a logic issue and be off by one here...
        if i < num_pixels - 4 and i > 4:  #the normal case
            if i % 2:
                restore_color = pixel_red
            else:
                restore_color = pixel_green
            pixels[i-1] = restore_color #reset the trailing pixel
            pixels[i] = pixel_blue
            pixels[i+1] = pixel_blue
            pixels[i+2] = pixel_blue
            pixels[i+3] = pixel_blue
            pixels[i+4] = pixel_blue
        elif i < num_pixels - 3 and i > 4: #end of the line detected
            pixels[i-1] = restore_color #reset the trailing pixel
            pixels[i] = pixel_blue
            pixels[i+1] = pixel_blue
            pixels[i+2] = pixel_blue
            pixels[i+3] = pixel_blue
            pixels[i+4-num_pixels] = pixel_blue  #wrap around
        elif i < num_pixels - 2 and i > 4: #end of the line detected
            pixels[i-1] = restore_color #reset the trailing pixel
            pixels[i] = pixel_blue
            pixels[i+1] = pixel_blue
            pixels[i+2] = pixel_blue
            pixels[i+3-num_pixels] = pixel_blue
            pixels[i+4-num_pixels] = pixel_blue  #wrap around
        elif i < num_pixels - 1 and i > 4: #end of the line detected
            pixels[i-1] = restore_color #reset the trailing pixel
            pixels[i] = pixel_blue
            pixels[i+1] = pixel_blue
            pixels[i+2-num_pixels] = pixel_blue
            pixels[i+3-num_pixels] = pixel_blue
            pixels[i+4-num_pixels] = pixel_blue #wrap around
        elif i < num_pixels  and i > 4: #end of the line detected
            pixels[i-1] = restore_color #reset the trailing pixel
            pixels[i] = pixel_blue
            pixels[i+1-num_pixels] = pixel_blue
            pixels[i+2-num_pixels] = pixel_blue
            pixels[i+3-num_pixels] = pixel_blue
            pixels[i+4-num_pixels] = pixel_blue #wrap around

        pixels.show()
