# Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input().lower() # jo bhi input hoga lower case mai aa jayga
if (weather == "sunny"):
    print("Go for a walk")
elif (weather == "rainy"):
    print("Read a book")
# elif (weather == "Snowy" or "snowy"): ye dusra vala snowy srf ek string rh jayga jo hmesha true hoga
elif (weather == "snowy"):
    print("Build a snowman")
else:
    print("No info")

