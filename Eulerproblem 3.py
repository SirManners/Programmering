import math

__author__ = 'ab53995'


def f():
    x = 600851475142
    z = 1
    while x > 2:
        # while x > z:
        # x % Tal != 0
        # prime = x % z > 0
        if 600851475143 % x == 0:
            # and x == prime
            print(x)

        x -= 1
f()
