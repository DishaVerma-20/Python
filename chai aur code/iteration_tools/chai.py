import time
print("chai is here")
username = "Disha"
print(username)


# to read a file
# open the file
f = open('chai.py')
print(f.readline()) # 1 by 1 line aati jaygi jitni baar ye statement use kari jaygi


# using for loop
for line in open('chai.py'):
    print(line, end = ' ')

# while loop
f = open('chai.py')
while True:
    line = f.readline()
    if not line: break
    print(line, end = '')

test = ""
if not test: #agar variable empty hai toh print krao
    print("Chai")

test = "Disha"
if not test:
    print("Chai")
# is baar test ke andar value hai toh yha par kuch bhi nahi print kra jayga


# # for i in [1, 2, 3, 4]:
#     # print(i)

# python internally ye karta haii 
#it = iter([1, 2, 3, 4])

# while True:
#     try:
#         i = next(it)
#         print(i)
#     except StopIteration:
#         break


# Internally python mai jo next element aata hai, vo kuch ese aa jata hai
I = [1, 2, 3, 4]
In = I.__next__()
print(In)
# aur jab list samapt ho jaati hai toh error raise ho jata hai, StopIteration


# agar hum file ko variable ke andar store krte hai toh vo ek iterable object default ban jata hai, but esa list ke case mai nahi hota haii, list mai vo srf uske actual object ka reference haii

f = open('chai.py')
print(iter(f) is f) # true aayga
print(iter(f) is f.__iter__()) # True
my = [1, 2, 3]
print(iter(my) is my) # false aayga, kyuki ye ek memory reference haii


