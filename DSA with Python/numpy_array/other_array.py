# np.arange() aur np.linspace() dono NumPy array hi return karte hain.
from numpy import *

# arange() me tum step size batate ho (kitna gap chahiye)
# linspace() me tum total numbers batate ho (kitne points chahiye)

arr = linspace(10, 20, 11)
for x in arr:
    print(x, end = ' ')
# start and end dono include rhte haii

print('\n')

# start included hoga, end nahii
arr = arange(10, 0, -1)
for x in arr:
    print(x, end = ' ')


print('\n')
# np.logspace() logarithmic scale par equally spaced values generate karta hai.
# Values 10^start se 10^stop ke beech hoti hain.
# 'num' batata hai ki total kitne elements generate karne hain.
# Return type: NumPy Array (ndarray)
# Syntax: np.logspace(start, stop, num)
# start and end dono include rhte haii
arr = logspace(1, 9, 8)
for x in arr:
    print(x, end = ' ')

print('\n')
# zero element ka array
z = zeros(10)
print(z)

print('\n')
# one element ka array
z = ones(10)
print(z)

print('\n')
# kisi bhi element ka array
z = full(10, 5) # size and element
print(z)