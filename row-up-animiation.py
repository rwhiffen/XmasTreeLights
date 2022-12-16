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
import json


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 350
DELAY=0.2

TREE_DICT_FILE="home-tree.json"

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
pixel_yellow = (255, 100, 0)
pixel_orange = (255, 50, 0)
pixel_red = (0, 255, 0)
pixel_blue = (0, 0, 255)
pixel_green = (255, 0, 0)
pixel_off = (0, 0, 0)


with open(TREE_DICT_FILE, 'r') as handle:
    tree_dict = json.loads(handle.read())

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

is_finished = False

def turn_off():
    pixels.fill((0, 0, 0))
    pixels.show()

while not is_finished:
    for row in tree_dict:
        start_led=tree_dict[row][0]
        end_led=tree_dict[row][1]
        for i in range(start_led,end_led):  #I may have a logic issue and be off by one here...
            pixels[i] = pixel_blue
        pixels.show()
        time.sleep(DELAY)
    turn_off()
