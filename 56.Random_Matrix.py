from random import randint

rows=int(input('Enter number of rows: '))
cols=int(input('Enter number of columns: '))
matrix=[]

for i in range(rows):
    y=[]
    for j in range(cols):
        y.append(randint(1,100))
    matrix.append(y)

for row in matrix:
    for item in row:
        print ("%3d"%item, end="")
    print()