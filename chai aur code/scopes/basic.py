# Matlab Python ke paas ek list/dictionary hoti hai jisme: name → value stored hota hai
username = "disha"
username = "chai"
def func():
    # username = "chai"
    # hmne yaha comment kr diya isko, mtlb function mai usename nahi hai ab yeh uppr jayga aur username search karega, jo mil jayga usey le lega, jo badme aayga vo
    print(username)

print(username)
func()



# another function
x = 99
def func2(y):
    z = x+y
    return z
result = func2(1)
print(result)
# yha par x ki value global vali hogi 99


# another function
def func3():
    global x
    x = 12

func3()
print(x)
# I want to use and modify a global variable named x (outside the function).


x = 33

# another example
def f1():
    # x = 77, agar ye na ho then global vala x print hoga
    def f2():
        print(x)
        # return x, yha None print ho jayga, kyuki value store nahi hui for f1
    f2()
f1()


# another example
def f1():
    x = 101
    def f2():
        print(x)
    return f2
my_result = f1()
my_result()



