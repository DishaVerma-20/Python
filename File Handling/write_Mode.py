# with open("new.txt", "w") as f:
#     # f.write("Hello World!")
#     f.write("Good bye")

lines = ["abcd\n", "line2\n", "nsbhjvadkhs\n"]
with open ("new.txt", "w") as f:
    f.writelines(lines)