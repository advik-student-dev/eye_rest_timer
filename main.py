"""
-------------
DRY-EYE TIMER
-------------

Program for nerds to run who have dry-eyes because we spend too much
time staring at gam... I mean code

"""

# Imports

import os
import pygame
import time

from inputimeout import inputimeout, TimeoutOccurred

pygame.init()
pygame.mixer.init()

# Initializing sound to 0
sound = 0


# Function to read the saved file
def reader():
    global sound  # *allowing local var to access global variable
    file1 = open("pref.txt", "r")  # reads pref.txt
    sound_read = file1.read()  # Store value from pref.txt as str because pref.txt is a text file
    sound = int(sound_read)


# Function to save a file with the preference
def saver():
    global sound  # *
    check = input("Would you like to save this preference to run it in the future(yes/no):  ").lower()
    if check == 'yes':
        file1 = open("pref.txt", "w")  # Here, creates new file to write the preference
        str_sound = repr(sound)
        file1.write(str_sound)
        file1.close()  # Always have this line when opening files
    if check == 'no':
        print("Not saving your preference...")


def testprint():  # Laziness.
    # Prolly slows down program. My fault. Wanted to be fancy
    print("Sound Preference Test")


try:
    open("pref.txt", "r")  # Throws FileNotFoundError if pref.txt does not exist to bypass
    # try-except TimeoutOccurred block
    try:
        print("Running from a previously existing preference...")
        time.sleep(1)
        print("You have 5 seconds to answer")

        # Using inputimeout to set a timer on the key_press input
        key_press = inputimeout("Press 'k' to break to delete this preference and see the sound "
                                "selection prompt again: ",
                                timeout=5).lower()
        if key_press == "k":
            os.remove("pref.txt")  # Removes pref.txt from the working directory
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

if sound == 4:
    testprint()
    sounda = pygame.mixer.Sound("funtimes.mp3")
    sounda.play()
if sound == 3:
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
    t = 1198

    # Copy-Pasted from a code learning Website
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

        if sound == 4:
            sounda = pygame.mixer.Sound("funtimes.mp3")
            sounda.play()
        if sound == 3:
            sounda = pygame.mixer.Sound("ara-ara.mp3")
            sounda.play()
        elif sound == 2:
            sounda = pygame.mixer.Sound("gangsta's paradise.mp3")
            sounda.play()
        elif sound == 1:
            sounda = pygame.mixer.Sound("notification.mp3")
            sounda.play()


    countdown(int(t))
