# Imports go at the top
from microbit import *
import random


# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        display.scroll('A')
        display.show(temperature())

    if button_b.was_pressed():
        display.scroll('B')
        display.show(Image.HAPPY)

    if accelerometer.was_gesture('shake'):
        display.show(random.randint(2, 12))