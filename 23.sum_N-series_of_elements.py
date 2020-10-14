# 1,-0.5,0.25,-0.125.....

num=int(input("Insert number of elements in the series: "))
x = 1
y=0
sum=0

while y < num:
    sum += x
    x = x/-2
    y += 1
    
print(sum)