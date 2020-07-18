#!/usr/sbin/python


import os
import time
from time import sleep
from numerals import numbers
from functions import tabata
from functions import double_digit
from functions import train
from functions import rest
from functions import display_title_bar
from functions import custom
import sys

if "--help" in sys.argv:
    sys.exit("""    # Please ensure round numbers only are entered as inputs
    # Time is in seconds only
    # Have fun""")
elif "--instruct" in sys.argv:
    sys.exit("""    There are two options for use:
    Option 1: Tabata timing, 20 seconds work, 10 seconds rest, 8 sets.
    If you choose to enter multiple rounds a break of 60 seconds shall be used inbetween eaech round
    Option 2: Fully customizable timer, be creative! Select, work time, rest time, number of sets, number of rounds
    and rest time between rounds.
    Be Creative and have fun!"""



option = " "
while option == " ":
    while option != "1" and option != "2":
        print("Please enter 1 or 2:")
        option = input("""Please select from the following options:
        Enter 1 for Tabata timer:
        Enter 2 for Custom timer:
        """)


if option == "1":
    tabata()
elif option == "2":
    custom()







