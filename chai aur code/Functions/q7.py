# Function with *args

# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args): # hum args ki jgh pr kuch bhi use kar sakte hai but asterisk hona mandate haii, preferred args
    print(*args) # yha values print ho jaygi
    
    for i in args:
        print(i*3)
        # hum bina kisi specified function jese sum ke bina bhi multiple values handle kar sakte hai


    # return args # isme tuple ke format mai ayyga
    return sum(args) # this syntax means multiple values
    # pass, this statement do nothing, just loop vgera exist krne lg jaate hai, without error without code


print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5, 6, 7))
