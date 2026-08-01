with open("hello.txt", "r") as f:
    line1 = f.readline()
    print(line1)
    

# readlines.. read many lines
with open("hello.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    # can take more memory

    for line in lines:
        # print(line)
        print(line.strip()) # if we do not want any whitespace or new line char


# best way to do it
with open("hello.txt", "r") as f:
    for line in f:
        # print(line)
        # for no spaces such as tab or new line
        print(line.strip())
        # puri memory save krke nahi rkheg.. on the spot 1 ine pr jayga read krega, print krega, aur dusri line.. mtlb khali kr dega khud ko


# if file does not exist use try except block
try:
    with open("helloo.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File does not exist.")
except:
    print("Some error occured")