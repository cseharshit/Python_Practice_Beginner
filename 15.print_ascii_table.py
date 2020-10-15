import itertools as it
print("ASCII TABLE")
print("\nNO.\tChar")
#itertools has chain function to allow us to iterate over multiple ranges in one loop
for i in it.chain(range(32,127), range(161,256)):
        print(i,"\t", chr(i))
