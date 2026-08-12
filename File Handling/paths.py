# C:\Users\HP\OneDrive\Desktop\Python\File Handling
#  this is the absolute path
# Yaani absolute = full address, relative = current location se address.
# script is instructions aur code vali file


# os path
import os

print(os.path.exists("hello.txt")) # check file or folder exists ya nahi, return true/false

print(os.path.isfile("new.txt")) # tells about the file
print(os.path.isdir("documents")) # tells whether the folder exists or not
print(os.path.getsize("hello.txt")) # return the size of the file

path = os.path.join("data", "app.log") # automatically observes windows system hai ya linux hai usi ke according path change kr dega

print(path)
