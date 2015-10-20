import math

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

__author__ = 'ab53995'


def f():
    x = 1
    z = 1
    while x < 600851475143:
        # while x > z:
        # x % Tal != 0
        # prime = x % z > 0
        if 600851475143 % x == 0:
            # and x == prime
            z *= x
            if z == 600851475143:
                print(x)
                break
        x += 2

f()