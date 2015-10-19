__author__ = 'ab53995'


def f():
    factors = []
    x = 3
    y = 0
    z = 1
    Tal = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    while x < 200283825047:
        # while x > z:
        # x % Tal != 0
        # prime = x % z > 0
        if 600851475143 % x == 0:
            # and x == prime
            number = x
            factors.append(number)
            print(x)
            y += 1
        x += 2
    print(factors[y])

f()
