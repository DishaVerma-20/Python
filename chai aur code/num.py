x = 234
y = 3
z = 4
print(x + y)
print(x ** 3)
print(x - z)
print(x + (y * z)) #industry standards - parenthesis use karo
print(42 + 2.23) # higher precision liya jayga, yeh bhi prefer nahi kara jaata hai
print(float(40))

# Operator Overloading : Ek operator ko multiple behavior dena depending on the operands.

print(x+1, y*6) # parenthesis mai result aayga
print(2 ** 1000) # number handle nahi hota most of languages mai e ya l show hota hai number ke saath


# 2 ** 1000 → Python exact integer print karta hai

# Python integers unlimited size ke ho sakte hain

# Dusri languages me overflow ya scientific notation aata hai

# Float numbers me Python bhi e notation use karta hai

print(1==2<3)
# 1==2 and 2<3

import math
print(math.floor(3.5))
print(math.floor(-3.5)) # nearest bottom whole number return karta hai
print(math.trunc(2.8))
print(math.trunc(-2.8)) # ye return karega towards zero nearest value

# 0o20 -> 0o ki yeh octal number hai, 0-7, base 8

x = 89

print(0o20)
print(0x45) # this shows hexa-decimal, base 16, 1-9, a-f
print(0b0101)
print(0xFF)

# but if we want to convert decimal to hex, octal or binary then we need to denote it
print(hex(x))
print(oct(x))
print(bin(x))

# given base se decimal mai jaane ke liye hai yeh method

print(int('10101010',2))
print(int('89',16)) # this method can also be used for conversion

# Bitwise Operations
print("Bitwise And:- & , returns 1 when both 1 ")
print("Bitwise Or:- | , returns 1 when any one bit is 1 ")
print("Bitwise Xor:- ^ , returns 1 when both are different ")
print("Bitwise Nor:- ~ , reverse the bits ")
print("Left Shift:- << , bits ko left side shift karta hai ")
print("Right Shift:- >> , bits ko right side shift karta hai ")


# from decimal import Decimal
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# >>> Decimal('0.3')
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# >>> Decimal('0.0')
# Decimal context manager

# from fractions import Fraction


# Sets
setone = {1,2,3,4}
print(setone & {1,3}) # intersection nikaal raha hai
print( setone | {1,7}) # union nikaal raha hai
# - sign is for difference
# empty set denote karte hai - set()
# {} ye dictionary ko represent karta haiii

print(setone -{1,2,3,4})


# Boolean Data Type
# True ko internally 1 ki trh treat kara jaata hai
print(True + 4) # answer will be 5
print(False + 2) # answer will be 2
print(True is 1) # False aayga kyuki memory reference alag haii
print(True == 1) # true aayga because value same haiii









