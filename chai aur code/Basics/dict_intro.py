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


# key + value = item
for key, value in d.items():
    print(key, value)

# if we want to check particular key exist kar rahi hai in dictionary or not
# conditional
if "name" in d:
    print("My name is Disha Verma.")

# to find the length of a dictionary
print(len(d))

chai_types = {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Mint': 'Mild', 'Green': 'Mild'}

# to add a n item in a dict that is key-value pair
chai_types["Earl Grey"] = "Citrus"
print("New list is ", chai_types)

# to remove an element from the dictionary using pop
chai_types.pop("Mint")
print(chai_types)

# to remove the last entered element
print(chai_types.popitem())

# for deleting the element from the memory reference
del chai_types["Green"]

print(chai_types) # 2 he bachega yaha par according to above

# agar hum copy = chai_types kare toh same memory reference
# but agar hum niche diye gaye method se kare toh dusri copy bana di jaati hai new reference par 
chai_types_copy = chai_types.copy()


# dictionary ke andar dictionary use karte haii, toh hame andar vali dict ka ref dena hoga kyuki vo index se nahi aa payga

tea_shop = {
    "chai": {"Ginger": "Zesty", "Mint": "Mild"},
    "tea" : {"Masala": "Spicy", "Green":"Mild"}
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])


# dict mai loop use karna in one line 
squared_num = {x:x**2 for x in range(7)}
print(squared_num)

# to remove squared no ke andar vala part
# squared_num.clear() , toh hame mili ek empty dictionary

keys = ["chai", "masala", "mint", "ginger"]
default_value = "Delicious"
new_dic = dict.fromkeys(keys, default_value)
newdic1 = dict.fromkeys(keys, keys)

print(new_dic)
print(newdic1)