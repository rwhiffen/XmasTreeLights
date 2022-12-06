# Rich Whiffen - 11/25/2022 - lots of lifted code here
#
# Mostly taken from the Adafruit learn guides.
# https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
#
# Flash alternating red and green colors
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


row_one = (0, 55)
row_two = (56, 102)
row_three = (103, 143)
row_four = (144, 180)
row_five = (181, 210)
row_six =  (211, 234)
row_seven = (235, 249)

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

is_finished = False

def turn_off():
    pixels.fill((0, 0, 0))
    pixels.show()

while not is_finished:

    start_led = int(input("starting LED: "))
    end_led = int(input("endinging LED: "))

    for i in range(start_led,end_led):  #I may have a logic issue and be off by one here...
        pixels[i] = pixel_blue
    pixels.show()
    should_turn_off = input("Y/N - turn all off? ")
    if should_turn_off.lower() == "y":
        turn_off()
