# Coffee customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso. 

order_size = input("Small or Medium or Large: ")
extra_shot = input("Espresso or not? ")
if extra_shot == "True":
    coffee = order_size + " with an extra shot"
else:
    coffee = order_size + "coffee"
print(coffee)