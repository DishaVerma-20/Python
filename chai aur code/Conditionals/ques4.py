# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input()

if fruit == "Banana":
 color = input("Tell the color of fruit: ")
 if (color == "Green"):
    print("unripe")
 elif (color == "Yellow"):
    print("ripe")
 elif (color == "Brown"):
    print("overripe")

else:
   print("No information of other fruits.")