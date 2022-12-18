# Rich Whiffen - 12/17/2022 - lots of lifted code here
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

pixel_aqua = (250, 50, 250)
pixel_magena = (0, 250, 20)
pixel_yellow = (225, 250, 30)
pixel_amber = (100, 250, 0)
pixel_orange = (50, 250, 0)
pixel_red = (0, 250, 0)
pixel_blue = (0, 0, 250)
pixel_green = (250, 0, 0)
pixel_pink = (90, 242, 255)
pixel_purple = (0, 180, 250)
pixel_white = (250, 250, 250)
pixel_jade = (240, 0, 40)
pixel_off = (0, 0, 0)

is_finished = False

def turn_off():
    pixels.fill((0, 0, 0))
    pixels.show()

def pick_color():
    colors = [pixel_jade, pixel_aqua, pixel_magena, pixel_amber, pixel_pink, pixel_yellow, pixel_orange, pixel_red, pixel_blue, pixel_green, pixel_purple, pixel_white, pixel_off]
    color = random.choice(colors)
    return color


pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

#start out white
pixels.fill(pixel_white)
pixels.show()

while not is_finished:
    pixel_num = random.randint(0,num_pixels-1)
    pixels[pixel_num] = pick_color()
    pixels.show()
