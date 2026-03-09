chai_types = {} # use dict keyword or use curly braces
d = dict(name = "Disha", age = 20, city = "Ghaziabad")
print(chai_types)
print(d)

# to get a value from dictionary, enter key
print(d["name"])
# dusra method 
print(d.get("name"))
print("There is none",d.get("namy")) # namy name ki koi key nahi hai toh yeh kuch nahi return karega

# print(d["namy"]) 
# iss uppr vale syntax mai error aa jayga

# if i want to change the Value
d["name"] = "Naina Verma"
print(d)

# using for loop in dictionary
for a in d:
    print(a) # srf key print ho jaygi, lekin list mai toh esa nahi hota tha, vha toh srf value he print hoti thi, not index

# key value dono print krne ke liye
for a in d:
    print("Key: value = ",a, d[a])
