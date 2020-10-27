from random import randint

rows = int(input("Enter number of rows = "))
cols = int(input("Enter number of columns = "))
matrix=[]

sum_of_rows=[0]*rows
sum_of_cols=[0]*cols

for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(randint(1,100))
    matrix.append(row)
 
for i in range (rows):
    for j in range(cols):
        sum_of_rows[i] += matrix[i][j]
        sum_of_cols[j] += matrix[i][j]

for i in range(rows):
    print(matrix[i], "|", sum_of_rows[i])


print("_"*cols*4)
print(sum_of_cols)