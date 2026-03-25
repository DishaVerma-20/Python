# Function with **kwargs

# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.


def print_kwargs(**kwargs):
    # print("Name: ", name, "Power: ", power)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name = "Disha", power = "Laser") # yha order kesa bhi ho chlega
print_kwargs(name = "Shaktiman")
print_kwargs(name="Disha Verma", classe = "CSE-DS", roll = 2300321540076, home = "Hapur")
# keyword arguments hai, yha order doesn't matter
# otherwise order matters, wrong output aa jata hai

