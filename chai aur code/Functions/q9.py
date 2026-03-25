# Generator Function with yield

# Problem: Write a generator function that yields even numbers up to a specified limit.

# def even_gen(limit):
#     list = []
#     for i in range (2, limit+1, 2):
#         list.append(i)
#     return list
# even_gen(10)
# ye thik hai but list ke form mai return ho rha hai, aur yeh demanded he nahi haii

def even_gen(limit):
    for i in range (2, limit+1, 2):
        # return i 
        yield i
        # memory mai uss function ki value and state dono ko rkhta haii
for num in even_gen(10):
    print(num)
