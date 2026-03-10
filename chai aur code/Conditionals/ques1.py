# Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age_person = int(input())
if (age_person < 13):
    print("Child")
elif (age_person>=13 and age_person<=19): # age_person < 20 kyuki vo sb uppr check ho gya 13 se niche tk
    print("Teenager")
elif (age_person>=20 and age_person<=59): # age < 60
    print("Adult")
else:
    print("Senior")