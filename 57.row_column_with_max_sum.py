from random import randint
matrix=[]

rows=int(input('Enter number of rows: '))
cols=int(input('Enter number of columns: '))
matrix=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(randint(1,100))
    matrix.append(row)

for row in matrix:
    print(row)

row_max=0
row_no=0

i=0

for row in matrix:
    if sum(row)>row_max:
        row_max=sum(row)
        row_no=i
    i+=1

print("Max_Sum = ",row_max, " for {}th row ".format(row_no+1))

col_max=0
col_no=0

i=0

for i in range(cols):
    sumcol=0
    for j in range(rows):
        sumcol+=matrix[j][i]
        if sumcol>col_max:
            col_max=sumcol
            col_no=i

print("Max_Sum = ",col_max, " for {}th col".format(col_no+1))
