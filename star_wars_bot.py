# Star Wars Bot
# Author: Aishani
# Date: Oct 16 2023

import time

# Creating a Star Wars Bot to let the user know if they are on the Dark Side

# Greet the user
print("Hello there.")
time.sleep(1)
print("I will be deciding if you are worthy for the Dark Side.")

# Ask questions 

red = input ("Is red your favourite colour? ")
cape = input("Do you like capes? ")

if red.lower().strip(",. ?!") == ("yes"): 
    print ("Dark side it is!")
elif cape.lower().strip(",. ?!") == ("yes") : 
        print ("Dark side it is!")
else: 
        print ("Light side, I see.")