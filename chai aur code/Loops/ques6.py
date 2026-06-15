# Factorial Calculator
# Compute the factorial of a number using a while loop.

number = int(input("Enter a number: "))
factorial = 1
while number> 0:
    factorial = factorial * number
    number -= 1
print(factorial)

number = int(input("Enter num: "))
factorial = 1 # multiply mai 1 ho jayga, kyuki vrna sab kuch 0 rh jayga
# using for loop
for i in range(1, number +1):
    factorial = factorial * i

print(factorial)