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
num_pixels = 100

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
pixel_yellow = (255, 100, 0)
pixel_orange = (255, 50, 0)
pixel_green = (0, 255, 0)
pixel_blue = (0, 0, 255)
pixel_red = (255, 0, 0)
pixel_off = (0, 0, 0)

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)





for i in range(num_pixels):
    pixels[i] = pixel_red
    pixels.show()
    print(f"Pixel number : {i}")
    time.sleep(1)
    pixels[i] = pixel_off
    pixels.show()
