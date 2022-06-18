# pip install inputs maybe???
# pip3 install pynput
# https://pypi.org/project/pynput/
from pynput import keyboard
import board
import digitalio
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
import time
import random

# set up button
from gpiozero import Button

button = Button(21)

# set up oled
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
oled_reset = digitalio.DigitalInOut(board.D4)
retro_screen = sh1106(
    serial_interface=0,
    width=128,
    height=64,
    rotate=0,
    reset=oled_reset,
)
WIDTH = 132
HEIGHT = 64  # Change to 32 depending on your screen resolution

num_lines = 7
line_length = 20
line_vert_spacing = 9

global lines
lines = ["" for i in range(num_lines)]


def get_char(key):
    try:
        return key.char
    except AttributeError:
        return " "


# handle keypresses
def on_press(key):
    global lines

    char = get_char(key)

    if char == " ":
        print("space pressed")
    else:
        print("alphanumeric key {0} pressed".format(char))
        # print(f"alphanumeric key {char} pressed")

    # change this line to 'update_lines_scroll' for scrolling behavior
    lines = update_lines(char, lines)

    draw_lines(lines)


def update_lines(char, lines):
    for i in range(len(lines)):
        if len(lines[i]) < line_length:
            lines[i] = lines[i] + char

            print("line {0}".format(i), lines[i])
            # print(f"line {i}", lines[i])

            return lines

    print("FULL")
    return lines


def update_lines_scroll(char, lines):
    for i in range(len(lines)):
        if len(lines[i]) < line_length:
            lines[i] = lines[i] + char

            print("line {0}".format(i), lines[i])
            # print(f"line {i}", lines[i])

            return lines

    # add new line at bottom, containing only the newly typed character
    lines.append([char])

    # make sure we don't have too many lines. This SHOULD only run once
    while len(lines) > num_lines:
        del lines[0]  # delete top line

    return lines


def draw_lines(lines):
    with canvas(device) as draw:
        for i in range(len(lines)):
            draw.text((0, i * line_vert_spacing), lines[i], fill="white")


def on_release(key):
    # print('{0} released'.format(key))
    # print ({0}.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
        """ADD SOMETHING THAT SAYS GOOD BYE"""


### listen for key press
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
