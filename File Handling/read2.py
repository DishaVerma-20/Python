# f = open("hello.txt")
# content = f.read(10)
# print(content)
# content2 = f.read(10) # next 10 char
# print(content2)
# content3 = f.read(10)
# print(content3)

# f.close()
# content = f.read(10) 
# error aa jayga badme

# but isme error aayga toh file close nahi ho paygi kyuki program ka execution toh vhii rukk gaya nh
with open("hello.txt") as f:
    content = f.read(10)
    print(content)
    content = f.read(10)
    print(content)
    # new line bhi 1 char he hai