from random import randint

rows = int(input("Enter number of rows = "))
cols = rows #int(input("Enter number of columns = "))
matrix=[]

sum_of_diagonal1=0
sum_of_diagonal2=0

for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(randint(1,100))
        print("%4d"%row[j],end=' ')
    matrix.append(row)
    print()
print()

for i in range(rows):
    matrix[i][i], matrix[i][rows-1-i] = matrix[i][rows-1-i], matrix[i][i]


for i in matrix:
    for j in i:
        print("%4d" %j, end=" ")
    print()
