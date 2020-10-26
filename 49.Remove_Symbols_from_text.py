input_str=input("Enter some string including symbols:\n ")
symbols=['.' , ',' , '?' , ';' , '!' , '(',')' ,"'", ':',]

for i in symbols:
    input_str=input_str.replace(i,'')

print("Clean String: ",input_str)