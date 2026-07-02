# Checking frequency..
n = [5, 3, 2, 2, 1, 5, 5, 7, 5 ,10]
m = [10, 111, 1, 9, 5, 67, 2]

hash_map = {}

# for i in range (0, len(n)):
#     hash_map[n[i]] = hash_map.get(n[i], 0) + 1
for i in n: # directly element ko dekha jayga
    hash_map[i] = hash_map.get(i, 0) + 1
print(hash_map)
for i in m:
    if i in hash_map:
        print (f"frequency of {i}:- ",hash_map[i])
    else:
        print(f"frequency of {i}:- ", 0)