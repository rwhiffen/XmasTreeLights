# Rich Whiffen - 12/17/2022 - lots of lifted code here
#
# Mostly taken from the Adafruit learn guides.
# https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
#
# test manually entered GRB color numbers.
#

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 350
DELAY=0.2

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
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

is_finished = False

def turn_off():
    pixels.fill((0, 0, 0))
    pixels.show()

while not is_finished:

    green_val = int(input("Green value (0-255): "))
    red_val = int(input("Red value (0-255): "))
    blue_val = int(input("Blue value (0-255): "))
   
    pixels.fill((green_val, red_val, blue_val))

    pixels.show()
    should_turn_off = input("Y/N/Q - turn all off? ")
    if should_turn_off.lower() == "y":
        turn_off()
    if should_turn_off.lower() == "q":
        is_finished = True