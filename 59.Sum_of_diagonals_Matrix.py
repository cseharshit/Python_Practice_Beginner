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
    matrix.append(row)


for row in matrix:
    print(row)
   

for i in range(rows):
    sum_of_diagonal1+=matrix[i][i]
    sum_of_diagonal2+=matrix[i][rows-i-1]

print("Sum of diagonal 1 = {} and Sum of diagonal 2 = {}".format(sum_of_diagonal1,sum_of_diagonal2))
