# eye_rest_timer

Written on 08/04/2022

Dry eye timer for people with dry eyes. Won't get rid of it, but at least will prevent it.

Project Stuff
  Pre-reqs (in the directory of the project ofc):-
    1. pygame
    2. inputimeout
    3. python 3.10 (recommended, anything above python 2 should be good)

  Run the following to install:-

  pip3 install pygame
  pip3 install inputimeout

  You need to have python installed and I am assuming you already know very basic python. The code is already commented, apart from the timer
  cus I couldn't care to learn the time and pygame module 

  Gave it sound preference saving functionality to waste my time and lose my sanity

  Yes indeed, you can save your preference when you run it for the first time. 
  But it isn't smart enough to detect time of day to nail your preference**
  It's just to skip the prompt of selecting the sounds to play every 20 mins

  If you want to, you can save the sound effect you like. 
  The sound effect preference can be changed by following the prompt and starting the program again.

  To add sound effects, add the .mp3 file sound effect to the directory of the project and modify main.py

  Instructions to add the effects are in main.py
  Line 82-85 (just broke up the sentences into multiple lines to make it slightly readable)


Made in Pycharm community edition
I recommend that you use pycharm for this project and to make tweeks to it on your own.
VS Code is fine. I am not too sure if the env of pycharm may create problems, but I am 95% sure that it won't cause problems.

Only run on a *nix system (macos specifically, intel) (architecture on mac shouldn't matter cause this ain't in a binary form)
up to this point. Never tried on any other platform. As long as you have the pre-reqs mentioned, you shouldn't have a problem (no guarantees).

If there is a problem on windows, it may be the os.remove part of the code that may be incompatible (Line 65).
I recommend that you find a windows equivalent command of os.remove in python.

** May try to add this functionality. May be able to do it in the next few days because the changes are just adding more
preference files and using another library to get the date and time from the user's computer (don't @ me. idk if those changes are enough).


If this somehow gains any traction, I'll clone this repo. The clone repo can have any person's additions. I'll merge stuff there instead of this
repo to maintain a stable version which always works and doens't break. If the additions are stable, I'll add the additions from the clone repo
to here. But that's if this gains any traction (if even 1 person become interested in this).

If you want that to happpen, just comment or do something. Like maybe raising a random issue or something to get my attention. I am a bit careless, so yeah.

Hope this gets some attention. But I imagine it won't cus this mini-essay is at the bottom of the readme.md.
Anyways, if anyone sees this... Ur cool

******* install.sh NOT TESTED ********

