# Function Returning Multiple Values

# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math
def circle(r):
    area = math.pi * r * r
    circ = 2 * math.pi * r
    return area, circ
print(circle(7))
a, c = circle(7) # multiple assignment ya phir unpacking, vese tuple mai value return ho rhi thi
print(a)
print(c)

# 👉 “Unpacking me ek iterable (tuple/list) ki values ko alag-alag variables me assign kar dete hain”