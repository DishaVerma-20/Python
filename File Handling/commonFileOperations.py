from pathlib import Path
import os

# for creation of a new folder
# os.mkdir("new_folder")
# Path("new_fol").mkdir()

# os.remove("neww.txt") # recycle bin mai bhi nahi jaata hai
# used to remove files
# Path("new.txt").unlink()

# now, i am going to rename the file
# os.rename("hello.txt", "hello_new.txt")
# Path("pathlibs.py").rename("modern_pathlibs.py")

# to list all the files in the particular space 
# for f in os.listdir("."):
#     print(f)

# . this shows current

# print("\n")
# print("\n")

# for f in Path(".").iterdir():
#     print(f)

for f in Path("C:\\").iterdir():
    # C drive ke andar jitni bhi files haii, folder hai sb return karega yeh
    print(f)
