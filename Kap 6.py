
"""
for i in range(0, 10):
    for j in range(10-i):
        print(j, end = " ")
    print()
"""

for row in range(0, 10):
    for space in range(0, row):
        print(end = "  ")
    for column in range(0, 10-row):
        print(column, end = " ")
    print()



