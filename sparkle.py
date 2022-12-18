# Rich Whiffen - 11/21/2022 - lots of lifted code here
#
# Mostly taken from the Adafruit learn guides.


import time
import board
import neopixel
import random


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 350
DELAY=0.05
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB


#predefine some colors

pixel_yellow = (255, 100, 0)
pixel_orange = (255, 50, 0)
pixel_red = (0, 255, 0)
pixel_blue = (0, 0, 255)
pixel_green = (255, 0, 0)
pixel_purple = (180, 0, 255)
pixel_off = (0, 0, 0)

is_finished = False

def turn_off():
    pixels.fill((0, 0, 0))
    pixels.show()

def pick_color():
    colors = [pixel_yellow, pixel_orange, pixel_red, pixel_blue, pixel_green, pixel_purple, pixel_off]
    color = random.choice(colors)
    return color


pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


while not is_finished:
    pixel_num = random.randint(0,num_pixels-1)
    pixels[pixel_num] = pick_color()
    pixels.show()
    