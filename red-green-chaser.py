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
num_pixels = 1000
DELAY=0.1

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

while true:

    for i in range(num_pixels):  #I may have a logic issue and be off by one here...
        if i < num_pixels - 4 && i > 4:  #the normal case
            pixels[i-1].brightness=0.2 #reset the trailing pixel
            pixels[i].brightness=0.4
            pixels[i+1].brightness=0.4
            pixels[i+2].brightness=0.4
            pixels[i+3].brightness=0.4
            pixels[i+4].brightness=0.4
        elif i < num_pixels - 3 && i > 4: #end of the line detected
            pixels[i-1].brightness=0.2 #reset the trailing pixel
            pixels[i].brightness=0.4
            pixels[i+1].brightness=0.4
            pixels[i+2].brightness=0.4
            pixels[i+3].brightness=0.4
            pixels[i+4-num_pixels].brightness=0.4  #wrap around
        elif i < num_pixels - 2 && i > 4: #end of the line detected
            pixels[i-1].brightness=0.2 #reset the trailing pixel
            pixels[i].brightness=0.4
            pixels[i+1].brightness=0.4
            pixels[i+2].brightness=0.4
            pixels[i+3-num_pixels].brightness=0.4
            pixels[i+4-num_pixels].brightness=0.4  #wrap around
        elif i < num_pixels - 1 && i > 4: #end of the line detected
            pixels[i-1].brightness=0.2 #reset the trailing pixel
            pixels[i].brightness=0.4
            pixels[i+1].brightness=0.4
            pixels[i+2-num_pixels].brightness=0.4
            pixels[i+3-num_pixels].brightness=0.4
            pixels[i+4-num_pixels].brightness=0.4  #wrap around
        elif i < num_pixels  && i > 4: #end of the line detected
            pixels[i-1].brightness=0.2 #reset the trailing pixel
            pixels[i].brightness=0.4
            pixels[i+1-num_pixels].brightness=0.4
            pixels[i+2-num_pixels].brightness=0.4
            pixels[i+3-num_pixels].brightness=0.4
            pixels[i+4-num_pixels].brightness=0.4  #wrap around

        pixels.show()
