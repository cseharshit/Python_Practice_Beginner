file_path=input("Enter complete file path: ")
try:
    file=open(file_path)

except FileNotFoundError:
    print("\nFile does not exist.")

else:
    print(file.read())