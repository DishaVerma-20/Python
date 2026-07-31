f = open("hello.txt", "r")
content = f.read()
print(content)
print(type(content)) # class str
f.close()