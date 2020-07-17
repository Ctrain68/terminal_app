import os
import time
from time import sleep



from numerals import numbers

def display_title_bar(stage):
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t**********************************************")
    print(f"\t***             {stage}                    ***")
    print("\t**********************************************")



# def round_rest():
#     for numb in numbers:
#         display_title_bar("Break....")

#         print("\n\n\a")
#         print(numbers[sets])
#         print("\nSet")
    
#         print(numbers[numb])
#         print("\nSeconds")
#         sleep(1)


def rest(activity,time):
    numbs = 1
    while numbs <= time :
        
            display_title_bar(activity)

            print("\n\n\a")
        
            print(numbers[numbs])
            print("\nSeconds")
        
            # Pause for 1 second between batches.
            sleep(1)
            numbs +=1


def double_digit(tis):

    numbstring = tis
    
    lstkey = []

    # if len(tis) > 1:
    for s in tis:
        lstkey.append(int(s))

    lst1 = []
    for numb in lstkey:

        lst1.append(numbers[numb])



    strings_by_column = [s.split('\n') for s in lst1]

    # Group the split strings by line
    # In this example, all strings are the same, so for each line we
    # will have three copies of the same string.
    strings_by_line = zip(*strings_by_column)

    # Work out how much space we will need for the longest line of
    # each multiline string
    max_length_by_column = [
        max([len(s) for s in col_strings])
        for col_strings in strings_by_column
    ]

    for parts in strings_by_line:
        # Pad strings in each column so they are the same length
        padded_strings = [
            parts[i].ljust(max_length_by_column[i])
            for i in range(len(parts))
        ]
        print(''.join(padded_strings))
    


def train(activity,time):
    numbs = 1
    while numbs <= time :
            
            display_title_bar(activity)

            print("\n\n\a")
            print(numbers[sets])
            print("\nSet")
            
            double_digit(str(numbs))
            print("\nSeconds")
            
                # Pause for 1 second between batches.
            sleep(1)
            numbs +=1




# for rounds in range(1,i+1):
#     display_title_bar(f"Round {rounds}!")
i = int(input("Enter how many rounds?"))
for rounds in range(1,i+1):
    display_title_bar(f"Round {rounds}")
    sleep (4)   
    for sets in range(1,3):
        
        train("Train!",30)

        train("Rest...",4)
    rest("Rest Between Rounds",10)



