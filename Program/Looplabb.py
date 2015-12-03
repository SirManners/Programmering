__author__ = 'ab53995'


x = 10
for row in range(9):
    for column in range(row+1):
        print(x+column, end=" ")
    print("")
    x += column + 1

