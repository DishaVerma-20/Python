# Tuple is immutable
# Jab list itna acha chal rha tha, phrr iske jrurat kyu aai, kyuki list mutable haii, vha append vgera sab kuch kar sakte hai 
# parenthesis is used for tuples

tea_types = ("Black", "Green", "Oolong")
print(tea_types)
print(tea_types[0]) # indexing bhi kar skte hai, index se access
print(tea_types[-1]) # negative indexing bhi hoti hai
print(tea_types[:]) #this will give the whole tuple


# ye variable assign ho jayga tea_types ke har ek element ko
(black, green, oolong) = tea_types
print(black) # black ki value print ho jaygi
print(green)

# we can concatenate
more_tea = ("Herbal", "Mint")
all_tea = more_tea + tea_types
print(all_tea)
# jis order mai concatenate kara hai vhi order aa jayga

type(tea_types)
len(tea_types)
# same list jese funcx. haii also dict

# loop we can use
if "Green" in all_tea:
    print("haha")