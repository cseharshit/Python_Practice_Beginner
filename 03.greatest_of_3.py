l,m,n = map(int,input().split())
if (l >= m) and (l >= n):
   largest = l
elif (m >= l) and (m >= n):
   largest = m
else:
   largest = n

print(largest, "is the maximum of the three numbers")