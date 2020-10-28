from random import randint
n= int(input("Enter number of elements in list: "))
a,b = map(int, input("Enter range of numbers seperated by -(eg: 5-20) ").split('-'))

my_list=[randint(a,b) for i in range(n)]
print(my_list)