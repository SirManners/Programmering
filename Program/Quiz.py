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

# -------------------------------------------------------------------------------
# förändring

yes = "ja", "yes", "jo", "y", "ye"
print("Welcome")
print()
score = 0
questions = 0
answer_0 = input("Hello. Do you want to play a quiz?")
if answer_0.lower() in yes:
    print("Excellent")
else:
    print("This is not a democracy")
print()
questions += 1
answer_1 = input("Question one: How much is 2^64? A) 16 B) 18446744073709551166 C) 18446744073709551616")
if answer_1.lower() == "c":
    print("Congratulations, you know how to use a calculator")
    score += 1
else:
    print("You are not doing too well are you")
print()

questions += 1
answer_2 = input("Question two: How fast is the speed of light? A) 300 000 000 m/s B) 300 000 km/h C) 300 000 m/s")
if answer_2.lower() == "a":
    print("Correct! You know me too well")
    score += 1
else:
    print("Not a man of science eh? No points for you")
print()

questions += 1
answer_4 = input("Question three: How many decimals does pi have? A) 912831298318 B) 314 C) 3.14")
if answer_4 == "a" or answer_4 == "b" or answer_4 == "c":
    print("Trick question! Pi has an infinite amount of decimals.")
else:
    print("Since none of the above were correct, and you didn't type one of them, you get a point")
    score += 1


questions += 1
answer_3 = input("Last question: Is the last question?")
if answer_3.lower() in yes:
    print("Clever boy")
    score += 1
else:
    print("Trick question you lose")
    score -= 500

print()

score_procent = score / questions * 100
print("You have scored", score, "points,", score_procent, "% of the total.")

if score_procent == 100:
    print("You are winner!")
elif score_procent > 70:
    print("Well done, but not good enough.")
elif score_procent > 20 and score_procent < 70:
    print("Mediocre.")
elif score_procent < 20:
    print("Did you even try?")

elif score_procent < 0:
    print("You are awful")
