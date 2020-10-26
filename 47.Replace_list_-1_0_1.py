mylist = [8,4,7,6,2,3,5,-2,-1,0,1,-6,-8,5,0,-9]
print(mylist)

for i in range(len(mylist)):
    if mylist[i]>0:
        mylist[i]=1
    elif mylist[i]<0:
        mylist[i]=-1
    else: mylist[i]=0

print(mylist)