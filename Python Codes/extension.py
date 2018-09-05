#program to identify the extension of a filename provided by user

filename = str(input("Enter a filename"))
file_ext = filename.split(".")
print("Extension for a file provided is = ." + file_ext[1])

