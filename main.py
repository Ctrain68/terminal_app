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
option = " "
while option == " ":
    while option != "1" and option != "2":
        option = input("""Please select from the following options:
        Enter 1 for Tabata timer:
        Enter 2 for Custom timer:
        """)


if option == "1":
    tabata()
elif option == "2":
    custom()







