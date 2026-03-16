# Reverse a String
# Reverse a string using a loop.

str = input()
reversed_str = ''
for char in str:
    reversed_str = char + reversed_str
print(reversed_str)

# there are many other ways too
# reversed function - built-in funxn
rev = ''.join(reversed(str))
print(rev)

# for loop - index method
rev = ""
length = len(str)
for i in range (length-1, -1, -1): # last index, stop before -1, step value
    rev += str[i]
print(rev)

# using while loop
rev = ""
i = len(str) -1
while i >= 0:
    rev += str[i]
    i -= 1
print(rev)
# agar hum len(s use kare srf, toh condition hmesha true rahegi agar hum minus nahi krege ya frr, agar ye kar lete hai toh len(s) exist nahi krta, len(S)-1 exist karta haii)

# using reverse 
# method matlab function jo kisi bhi object se attached ho jaat hai
# we need to convert first string to list, kyuki yeh list ka method haii
s = input("Enter string: ")
l = list(s)
l.reverse()
rev = "".join(l)
print(rev)