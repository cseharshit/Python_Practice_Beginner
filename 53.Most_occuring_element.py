from random import random

x=[int(random()*15) for i in range(20)]
print(x)

my_set=set(x)

most_occuring_value=None
most_occuring_frequency=0

for item in my_set:
    frequent=x.count(item)
    if frequent>most_occuring_frequency:
        most_occuring_frequency=frequent
        most_occuring_value=item


print("Most occuring element = ", most_occuring_value, " Occuring {} times".format(most_occuring_frequency))