#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ab53995
#
# Created:     04-09-2015
# Copyright:   (c) ab53995 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import *
import random

#pyCharm

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.\nThe natives want their camel back and are chasing you down! \nSurvive your desert trek and outrun the natives.")

#i = avståndet du har gått
drinks = 3
fatigue = 0
i = 5
j = 0
# Natives avstånd till dig
# Behöver en till while loop?
while i < random.randrange(40, 51) or j >= i :
    input("A. Drink from your canteen.\nB. Ahead moderate speed. \nC. Ahead full speed. \nD. Stop and rest. \nE. Status check. \nQ. Quit. \nYour choice? ")
        if "A".lower():
            fatigue -= 5
            j += random.randrange(2, 8)
            drinks -= 1
        if "B".lower():
            i += random.randrange(4, 8)
            fatigue += 1
            j += random.randrange(2, 8)
        if "C".lower():
            i += random.randrange(10, 15) - fatigue
            fatigue += 5
            j += random.randrange(2, 8)
        if "D":
            fatigue -= 10
            j += random.randrange(2, 8)
        if "E":
            print("Miles traveled:" , i , "\nDrinks in the canteen" , drinks , "\nThe natives are" , i-j , "miles behind you.")