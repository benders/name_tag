# SPDX-FileCopyrightText: 2020 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# SpaceX Launch Display, by Anne Barela November 2020
# MIT License - for Adafruit Industries LLC
# See https://github.com/r-spacex/SpaceX-API for API info

import time
import terminalio
from adafruit_magtag.magtag import MagTag

magtag = MagTag()
#    url=DATA_SOURCE,
#    json_path=(NAME_LOCATION, DATE_LOCATION, DETAIL_LOCATION)
#)

magtag.add_text(
    text_font="/fonts/Kanit-Black-24.bdf",
    text_position=(50, ((magtag.graphics.display.height - 36) // 2) - 1),
    text_scale=2,
    is_data=False,
)

magtag.add_text(
    text_font="/fonts/Lato-Bold-ltd-25.bdf",
    text_position=(50, ((magtag.graphics.display.height - 36) // 2) - 1),
    text_scale=2,
    is_data=False,
)

magtag.add_text(
    text_font="/fonts/Kanit-Medium-20.bdf",
    text_position=(25, ((magtag.graphics.display.height - 36) // 2) - 1),
    text_scale=2,
    is_data=False,
)

# Display heading text below with formatting above
#magtag.set_text("TEDDY",0)
magtag.set_text("WALTER",1)
#magtag.set_text("GARRETT",2)

import board
from rainbowio import colorwheel
import neopixel

num_pixels = 4
pixels = magtag.peripherals.neopixels
pixels.brightness = 0.05

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    pixels[0] = RED
    pixels[1] = GREEN
    pixels[2] = RED
    pixels[3] = GREEN
    pixels.show()
    time.sleep(1)

    pixels[0] = GREEN
    pixels[1] = RED
    pixels[2] = GREEN
    pixels[3] = RED
    pixels.show()
    time.sleep(1)
   
#    pixels.fill(RED)
#    pixels.show()
#    # Increase or decrease to change the speed of the solid color change.
#    time.sleep(1)
#    pixels.fill(GREEN)
#    pixels.show()
#    time.sleep(1)
#    pixels.fill(BLUE)
#    pixels.show()
#    time.sleep(1)

#    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
#    color_chase(YELLOW, 0.1)
#    color_chase(GREEN, 0.1)
#    color_chase(CYAN, 0.1)
#    color_chase(BLUE, 0.1)
#    color_chase(PURPLE, 0.1)

#    rainbow_cycle(0.1)  # Increase the number to slow down the rainbow


## wait 2 seconds for display to complete
#time.sleep(2)
#magtag.exit_and_deep_sleep(TIME_BETWEEN_REFRESHES)
