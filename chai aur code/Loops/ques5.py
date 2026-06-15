# Find the First Non-Repeated Character
# Given a string, find the first non-repeated character.

str = input()
for i in str:
    if str.count(i) == 1:
        print(i)
        break
