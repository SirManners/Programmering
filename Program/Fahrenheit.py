__author__ = 'ab53995'
import math

print("Detta är en Celsius till Fahrenheit omvandlare")
answer = input("A. C->F B. F->C").lower()
if answer == "a":
    value1 = int(input("Antal grader Celsius:"))
    value1 = (value1*1.8)+32
    print(value1, " grader Fahrenheit")
if answer == "b":
    value2 = int(input("Antal grader Fahrenheit:"))
    value2 = (value2 - 32)/1.8
    print(value2, " grader Celsius", )