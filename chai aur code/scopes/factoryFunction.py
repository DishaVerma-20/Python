# factory function or closure
# another example
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual #function ki definition return kri hai, saath mai khane peene ka samaan aur num ka reference bhi saath

f = chaicoder(2) # yaha pr actual value with num as 2 save ho gayi haii
g = chaicoder(3)

print(f)
print(g)

print(f(3))
print(g(3))

# Closure: andar wala function, bahar wale ka data yaad rakhta hai