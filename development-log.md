# Colin Forster Development Log

## 11/7/2020

Started looking at my project, I had a change of what I wanted to do and went from wanting to do a adapation of my fitness regime app to one that was focused more on timers. The idea involves using Ascii art to display numbers. Spoke to Garret about the idea and how to implement it. Ran into an issue with being able to print multi-line strings such as the ascii art is. Decided on using a dictionary for the numbers with numerals as a key. The plan was first to make a timer that can count to 10. Then expand on this for rest time, sets, and rounds and rest after rounds. Managed to DRY up some of the timer loops into simple functions making it easier to use and manipulate. Still have issues with multi line strings printing side by side. At this point deciding on whether it is worthwhile. Git also was initilised and commits done. 

## 17/7/2020

Due to work commitments I have not been able to put in as much of an effort as I wanted with this project and have now scaled back what I wanted to achieve.  Ideally now what I shall make is two timers, one static for tabata with only the only variable that can be changed being the rounds of of the tabata set. The other timer shall be completely customizable. However the first issue that must be over come is to be able to print the multi line strings next eachother. Investigated this online and found a process that I was able to implement in my code that utlisies the \n that is created when multiline strings are put into a list. I was able to replace my counters and print functions with this adapated code to print out the multi line string. Had to add a tab to the Ascii art so they were seperated. Managed to get counter working to 30, and should potentially count however many places is needed

## 18/7/2020

Changed the function used to implement the multiple loop timers to its own function. Found an issue where a funciton won't search another function for a variable but this was fixed relatively easily. Created a menu to select from the two options and imported my functions into main.py. Added some error checking to the functionality of the project. Would ideally have liked to do a lot more but will continue to work on the app after submission.

