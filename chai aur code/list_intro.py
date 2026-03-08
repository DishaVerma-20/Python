# list[i] = value, value single element
# list[i:j] = iterable, slice assignment, iterable ke elements insert honge

tea_varities = ['Lemon', 'Ginger', 'Mint', 'Masala']
# >>> tea_varities
# ['Lemon', 'Ginger', 'Mint', 'Masala']
# >>> tea_varities[2] = "Oolong"
# >>> tea_varities
# ['Lemon', 'Ginger', 'Oolong', 'Masala']
# >>> tea_varities[1:2] = 'Mint'
# >>> tea_varities
# ['Lemon', 'M', 'i', 'n', 't', 'Oolong', 'Masala']
print(tea_varities[1:1])
tea_varities[1:1] = ['test', 'test']
print(tea_varities)


# if i want to add element, there is also another method
tea_varities.append("Oolong")
print(tea_varities)

tea_varities.pop()
print(tea_varities)
# it is used to remove the last element
tea_varities.remove("test")
# to remove the particular element from the list
print(tea_varities)

