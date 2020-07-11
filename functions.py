import os
import time
from time import sleep



from numerals import numbers

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t**********************************************")
    print("\t***          It's Timer time!              ***")
    print("\t**********************************************")
    




for key in numbers:
    display_title_bar()

    print("\n\n\a")

   
    print(numbers[key])
    print("\nSeconds")
    
    # Pause for 1 second between batches.
    sleep(1)




