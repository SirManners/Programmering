__author__ = 'ab53995'


def f():
    z = 0
    x = 1
    summa = 0
    while z < 4000000:
        z += x
        if z % 2 == 0:
            summa += z
        x = z - x
    print(summa)

f()
