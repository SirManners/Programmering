
'''
for i in range(0, 10):
    for j in range(10-i):
        print(j, end = " ")
    print()

for row in range(10):
    for space in range(row):
        print(" ", end = " ")
    for column in range(10-row):
        print(column, end = " ")
    print()

for row in range (9):
    for column in range(9):
        if (row+1)*(column+1)<10:
            print(end = " ")
        print((row+1)*(column+1), end = " " )
    print()

'''

for row in range(9):
    for column in range(row+1):
        print(column+1, end=" ")

    for row2 in range(1, 9, 2):
        print(row, end=" ")

    print()