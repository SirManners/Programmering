__author__ = 'ab53995'


def f():
    x = 0
    summa = 0
    while x < 1000:
        if x % 3 == 0:
            summa += x
        elif x % 5 == 0:
            summa += x

        x += 1
    print(summa)

f()

