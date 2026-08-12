import random

print(random.random()) # creates random between 0.0 and 1.0
print(random.randint(1, 6)) # range mai 1 and 6 dono inclusive hoge, generate a random integer in the given range
print(random.choice(["a", "b", "c"])) # chooses randomly from the given list or sequence, can be string too
my_list = ["a", "b", "c", "d"]
random.shuffle(my_list) # list ko shuffle karna, doesn't returns something
print(my_list)