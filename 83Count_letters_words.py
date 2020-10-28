lines=0
words=0
letters=0

file="./data/Program83.txt"
for line in open(file):
    lines += 1
    letters += len(line)
    words += len(line.split(' '))

print("Lines = {}, Words = {}, Letters = {}".format(lines,words,letters))