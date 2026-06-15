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

# inserting elemnt at particular position
tea_varities.insert(1, "Turmeric")
# to copy the list with different memory reference
tea_varities_copy = tea_varities.copy()
print("this is copy", tea_varities_copy)

# List Comprehension in Python is a short and elegant way to create a list using a single line of code instead of writing a full for loop.
# [expression for item in iterable]

square_nums = [x**2 for x in range(10)]
print(square_nums)

cube_nums = [x**3 for x in range(7)]
print(cube_nums)
