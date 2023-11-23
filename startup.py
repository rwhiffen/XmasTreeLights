# xmas 2023 version
# going to try and make a web interface to pick the tree animation
#
# 11/13/23 - Rich Whiffen 
# https://github.com/rwhiffen/XmasTreeLights

#
# Over all idea is to run a flask server that lets me pick the animations
# I've already built.  
#
# because this only runs inside my house I'm ok running flask in default 
# mode
#



import time
import board
import neopixel

from flask import Flask

app = Flask(__name__)