"""
-------------
DRY-EYE TIMER
-------------

Program for nerds to run who have dry-eyes because we spend too much
time staring at gam... I mean code

"""

# Imports

import os
import sys

import pygame
import time

from inputimeout import inputimeout, TimeoutOccurred

pygame.init()
pygame.mixer.init()

# Constants
TXT = "preferences/pref.txt"
TIME = "preferences/time.txt"

# Initializing sound and timer_time to 0
sound = 0
timer_time = 1200


# -------FUNCTIONS-------
# Function to read the saved sound preference file
def reader():
    global sound  # *allowing local var to access global variable
    file1 = open(TXT, "r")  # reads pref.txt
    sound_read = file1.read()  # Store value from pref.txt as str because pref.txt is a text file
    sound = int(sound_read)


# Function to save a file with the sound preference
def saver():
    global sound  # *
    check = input("Would you like to save this preference to run it in the future(yes/no): ").lower()
    if check == 'yes':
        file1 = open(TXT, "w")  # Here, creates new file to write the preference
        str_sound = repr(sound)
        file1.write(str_sound)
        file1.close()  # Always have this line when opening files
    if check == 'no':
        print("Not saving your preference...")


def testprint():  # Laziness.
    print("Preferred Sound Test")


def sleep():
    if sound == 4:
        time.sleep(5)
    # May make vars for sleep timer for custom sounds


def time_reader():
    global timer_time  # *allowing local var to access global variable
    file1 = open(TIME, "r")  # reads time.txt
    time_read = file1.read()  # Store value from time.txt as str because time.txt is a text file
    timer_time = int(time_read)


def time_saver():
    global timer_time  # *
    check = input("Would you like to save this TIME preference to run in the future(yes/no): ").lower()
    if check == 'yes':
        file1 = open(TIME, "w")  # Here, creates new file to write the preference
        str_time = repr(timer_time)
        file1.write(str_time)
        file1.close()  # Always have this line when opening files
    if check == 'no':
        print("Not saving your preference...")


# Convoluted Try-Except block for sound preference
try:
    open(TXT, "r")  # Throws FileNotFoundError if pref.txt does not exist to bypass
    # try-except TimeoutOccurred block
    try:
        print("Running from a previously existing preference...")
        time.sleep(1)
        print("You have 5 seconds to answer")

        # Using inputimeout to set a timer on the key_press input
        key_press = inputimeout("Press 'S' to break to delete SOUND preference: ",
                                timeout=5).lower()
        if key_press == "s":
            os.remove(TXT)  # Removes pref.txt from the working directory
    except TimeoutOccurred:
        reader()  # If TimeoutOccurred, then calls reader() function
except FileNotFoundError:
    sound = int(input("""
Enter Sound Effect
0 = quit
1 = notification
2 = gangsta's paradise
3 = ar
4 = EEEEEEEEEEE
    
Enter number:
"""))

    saver()  # Calls saver() func incase user wants to save the sound preference

# Try-except block to avoid the program running cus if this weren't here, the program would not
# play any sound even when the timer is running
try:
    open(TXT, "r")
except FileNotFoundError:
    check = input("""
Would you like to run the timer with the default sound preference? Timer will quit if 
the answer is no (don't know how to bring the preference selector back, may fix later): 
""").lower()
    if check == 'yes':
        print("Default sound preference is 1")
        sound = 1
    else:
        print("Bye")
        sys.exit(1)
try:  # Try-except block for timer duration
    open(TIME, "r")  # Opens time.txt
    try:
        print("Running from previously existing TIME preference...")
        time.sleep(1)
        print("You have 5 seconds to answer...")
        # Using inputimeout to set a timer on the key_press input
        key_press = inputimeout("Press 'T' to break to delete TIME preference: ",
                                timeout=5).lower()
        if key_press == "t":
            os.remove(TIME)  # Removes time.txt
        else:
            print("Should've left it empty...")
            sys.exit(1)  # May not work on Windows. Pls check Windows' users (pls tell if that
            # is the wrong punctuation mark)
    except TimeoutOccurred:
        time_reader()
        print("\n")
        print("Timer duration is", timer_time, "seconds =", timer_time / 60, "minutes")
except FileNotFoundError:
    timer_time = int(input("""
---------------------    
Timer duration setter
1200 seconds = 20 min 

20 minutes is default to avoid issues like audio clipping/the same audio file layering on top of itself

Enter timer duration(seconds):
"""))

    time_saver()  # Calls time_saver() func incase user wants to save the sound preference
    print("\n")
    print("Timer duration is", timer_time, "seconds =", timer_time / 60, "minutes")

# Copy-paste the below block of code and just add a number - like 5 - to
# add a new sound effect below these comments
# btw, do the same thing in the timer itself
# This one is just for testing the sound when the timer starts

if sound == 4:
    testprint()
    sounda = pygame.mixer.Sound("funtimes.mp3")
    sounda.play()
elif sound == 3:  # fixed elif thing
    testprint()
    sounda = pygame.mixer.Sound("ara-ara.mp3")
    sounda.play()
elif sound == 2:
    testprint()
    sounda = pygame.mixer.Sound("gangsta's paradise.mp3")
    sounda.play()
elif sound == 1:
    testprint()
    sounda = pygame.mixer.Sound("notification.mp3")
    sounda.play()

while sound != 0:
    t = timer_time

    # Copy-Pasted from a code learning Website
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

        if sound == 4:
            sound4 = pygame.mixer.Sound("funtimes.mp3")
            sound4.play()
        if sound == 3:
            sound4 = pygame.mixer.Sound("ara-ara.mp3")
            sound4.play()
        elif sound == 2:
            sound2 = pygame.mixer.Sound("gangsta's paradise.mp3")
            sound2.play()
        elif sound == 1:
            sound1 = pygame.mixer.Sound("notification.mp3")
            sound1.play()


    countdown(int(t))
