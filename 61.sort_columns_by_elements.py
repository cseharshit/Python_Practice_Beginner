# Sort columns of elements by sorting the first row

from random import randint

column = 6
row = 6
matrix = []
for i in range(row):
    myrow=[]
    for j in range(column):
        myrow.append(randint(10,100))
    matrix.append(myrow)
    
for i in matrix:
    print(i)
print()
k = column - 1
while k != 0:
    x = 0 
    for j in range (1, k+1):
        if matrix[0][j] > matrix[0][x]:
            x = j
    for i in range(row):
        y = matrix[i][x]
        matrix[i][x] = matrix[i][k]
        matrix[i][k] = y
        
    k -= 1
    
for i in matrix:
    print(i)