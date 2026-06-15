# List Uniqueness Checker

# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

n = int(input("Enter no. of integers: "))
list_num = list(map(int, input().split()))

for i in list_num:
    if list_num.count(i) != 1:
        print(i)
        break



# other acha vala method
items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set() # duplicate add nhi hote, naturally, faster

for item in items:
    if item in unique_item:
        print("Duplicate item")
        break
    unique_item.add(item)