#pip install inputs maybe???
#pip3 install pynput
#https://pypi.org/project/pynput/
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
retro_screen = sh1106(serial_interface=0, width=128, height=64, rotate=0, reset=oled_reset)
WIDTH = 132
HEIGHT = 64 # Change to 32 depending on your screen resolution


global line_one
global line_two
global line_three
global line_four
global line_five
global line_six
global line_seven

line_one = ("")
line_two = ""
line_three = ("")
line_four = ("")
line_five = ("")
line_six = ("")
line_seven = ("")

# Enter a letter

def on_press(key):
    global line_one
    global line_two
    global line_three
    global line_four
    global line_five
    global line_six
    global line_seven

  # check to see if line is full
    line_length_1 = len(line_one)
    line_length_2 = len(line_two)
    line_length_3 = len(line_three)
    line_length_4 = len(line_four)
    line_length_5 = len(line_five)
    line_length_6 = len(line_six)
    line_length_7 = len(line_seven)  
    
      
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        letter = (key.char) # single letter
        print (letter)
        
       
        #print (line_length_2)

        if line_length_7 > 20:
            print ("FULL")
            #CLEAR ALL TEXT?

        elif line_length_6 > 20:
            line_seven = line_seven + letter
            print ("line seven", line_seven)

        elif line_length_5 > 20:
            line_six = line_six + letter
            print ("line six", line_six)    
        
        elif line_length_4 > 20:
            line_five = line_five + letter
            print ("line five", line_five)

        elif line_length_3 > 20:
            line_four = line_four + letter
            print ("line four", line_four)    

        elif line_length_2 > 20:
            line_three = line_three + letter
            print ("line three", line_three)

        elif line_length_1 > 20:
            line_two = line_two + letter
            print ("line two", line_two)

        else:
            line_one = line_one + letter
            print ("line one", line_one)
            

        
            
        with canvas(device) as draw:
            draw.text((0, 0), line_one, fill="white")
            draw.text((0, 9), line_two, fill="white")
            draw.text((0, 18), line_three, fill="white")
            draw.text((0, 27), line_four, fill="white")
            draw.text((0, 36), line_five, fill="white")
            draw.text((0, 45), line_six, fill="white")
            draw.text((0, 54), line_seven, fill="white")

    except AttributeError:

        letter = " " # Check for SPACE BAR Press
        
        with canvas(device) as draw:

            # adds space to letter list

            if line_length_7 > 20:
                print ("FULL")
                #CLEAR ALL TEXT?

            elif line_length_6 > 20:
                line_seven = line_seven + letter
                print ("line seven", line_seven)

            elif line_length_5 > 20:
                line_six = line_six + letter
                print ("line six", line_six)    
            
            elif line_length_4 > 20:
                line_five = line_five + letter
                print ("line five", line_five)

            elif line_length_3 > 20:
                line_four = line_four + letter
                print ("line four", line_four)    

            elif line_length_2 > 20:
                line_three = line_three + letter
                print ("line three", line_three)

            elif line_length_1 > 20:
                line_two = line_two + letter
                print ("line two", line_two)

            else:
                line_one = line_one + letter
                print ("line one", line_one)

           ### draw the letters:
                
            draw.text((0, 0), line_one, fill="white")
            draw.text((0, 9), line_two, fill="white")
            draw.text((0, 18), line_three, fill="white")
            draw.text((0, 27), line_four, fill="white")
            draw.text((0, 36), line_five, fill="white")
            draw.text((0, 45), line_six, fill="white")
            draw.text((0, 54), line_seven, fill="white")

def on_release(key):
    #print('{0} released'.format(key))
    #print ({0}.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
        '''ADD SOMETING THAT SAYS GOOD BYE'''

                      
### listen for key press
                      
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()                       





