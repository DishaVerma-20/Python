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