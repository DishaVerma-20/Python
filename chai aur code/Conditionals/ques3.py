# Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60). 


# for larger grades than 100

grade = int(input())

if grade >= 101:
    print("please verify your grade again")
    exit()
    # program se exit kar lega yeh

if grade<60:
    print("F")
elif(grade<70):
    print("D")
elif (grade < 80):
    print("C")
elif(grade<90):
    print("B")
else:
    print("A")