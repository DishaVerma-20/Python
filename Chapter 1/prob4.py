import os

# specify the path of the directory
directory_path = "/"

# get the list of files and folders
contents = os.listdir(directory_path)

# print the contents
print("Contents of directory:", directory_path)
for item in contents:
    print(item)
