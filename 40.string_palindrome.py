str = input("Insert a string: ")
len_str = len(str)

# for i in range(len_str//2):
#     if str[i] != str[-1-i]:
#         print("This is Not a palindrome!")
#         quit()
if (str == str[::-1]):
    print("{} is a palindrome!".format(str))
else:
    print("{} is not a palindrome".format(str))
