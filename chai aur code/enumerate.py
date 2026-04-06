x = ('Masala', 'Lemon', 'Ginger')
y = enumerate(x)

print(list(y))

# gives index + value
# more pythonic


list = [{'name':'Disha', 'time':'2 min'}, {'name':'Suhani', 'time':'3 min'}]
a = enumerate(list, start = 1)
for i, vid in a:
    print(f"{i}, {vid['name']}") # video mai bhi 2 elements haii