from math import *

# define the function
def count_digits(num):
    return int(log10(num) + 1)

print(count_digits(87654))