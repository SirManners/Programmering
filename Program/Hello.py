#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ab53995
#
# Created:     28-08-2015
# Copyright:   (c) ab53995 2015
# Licence:     <your licence>
# Import the math library

#-------------------------------------------------------------------------------

from math import *

print("Welcome")
print()
score = 0
questions = 0
answer_0 = input("Hello. Do you want to play a game?")
if answer_0.lower() == "yes":
    print("Excellent")
else:
    print("This is not a democracy")
print()
questions = questions + 1
answer_1 = int(input("Question one: How much is 2^64?"))
if answer_1 == 18446744073709551616:
    print("Congratulations, you know how to use a calculator")
    score = score + 1
else:
    print("You are not doing too well are you")
print()

questions = questions + 1
answer_2 = input("Question two: What are my middle names?")
if answer_2.lower() == "martin joel":
    print("Correct! You know me too well")
    score = score + 1
else:
    print("You should have come prepared")
print()

questions = questions + 1
answer_3 = input("This is the last question")
if answer_3.lower() == "yes":
    print("Clever boy")
    score = score + 1
else:
    print("You suck balls")
    score = score - 500

print()

score_procent = score / questions * 100
print("You have scored" , score , "points," , score_procent , "% of the total.")


