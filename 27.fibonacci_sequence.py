#Generate fibonacci sequence of n numbers

range_of_seq=abs(int(input("Enter the range of sequence (O excluded): ")))
f1=f2=1

print(0,f1,f2,end=" ")
for i in range(range_of_seq-2):
    print(f1+f2,end=" ")
    f1,f2 = f2, f1+f2