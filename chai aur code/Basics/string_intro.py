# step ko hopping bhi bolte haii
# agar 2 hai toh step value, then current index + 2 hoga
str = "0123456789"
print(str[:]) # for printing full str
print(str[0:10]) # for printing full str
# last vala element included nahi hota haii

# some operations
tea = "   Masala Chai   "
print(tea.lower()) # lower all the characters
print(tea.upper()) # upper all the characters
print(tea.strip()) # removes all the spaces
print(tea.replace("Masala", "Lemon"))

list1 = "Masala, Ginger, Lemon, Mint"
print(list1.split(",")) # by default spaces se split karta haii
print(tea.find("Chai")) # agar nahi hoga toh -1 return kr dega, index se return karta haii
print(tea.count("Chai")) # returns the number of chai in the string


# performing another operation
# placeholders string mai use krna seekhna, yha hum variable insert kar sakte haii

chai_type = "masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))


chai_variety = ["Lemon", "Ginger", "Mint"]
print("".join(chai_variety)) # bina spaces ke saare elemnts ko join kar dega
print(" ".join(chai_variety)) # spaces ke saath string ke elements ko print krega
print(type(chai_variety))



# printing raw strings, path etc
name = "Disha\nVerma"
print(name)
print(r"name") # ye khud phirr ek raw strung ki trh treat kiya jayga

# to print as it is
name = r"Disha\nVerma"
print(name)

# raw string mai single backslash pr string nahi end hoga, usey vo lagega ki yeh escape char hai for inverted comma
# ya toh slash he hata do ya frr double slash ka use karo

path = r"c:\user\pwd\\"
path = r"c:\user\pwd"
print(path)

# >>> chai = "c:\\user\\pwd"
# >>> chai
# 'c:\\user\\pwd'
# >>> print(chai)
# c:\user\pwd


# Membership Operator
chai = "Masala chai"
print("Masala" in chai) # ask questions ki string ke andar hai ya nahi hai