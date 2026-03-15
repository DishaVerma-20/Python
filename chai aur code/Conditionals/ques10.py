# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter animal: ")
age = int(input())

if (species == "Dog" and age<2):
    print("Puppy Food")
elif (species == "Cat" and age > 5):
    print("Senior cat food")
else:
    print("No information")