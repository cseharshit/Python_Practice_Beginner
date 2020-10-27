extensions=['gif','png','jpeg','jpg','svg']

file_extension=input("Enter the filename with extension: ").split('.')
if (len(file_extension)>=2):
    extension=file_extension[-1].lower()
    if extension in extensions:
        print("File Extension exists")
    else: 
        print("File Extension does not exists")
else:
    print("File does not have extension")