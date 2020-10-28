fp = open('./data/Program81.txt')
fp.write("Hello World 1 \n")
fp.write("Hello world 2 \n")

fp.writelines("Hello World 3 \n")
text = ["Hello World 4 \n","Hello World 5 \n", "Hello World 6"]

fp.close()