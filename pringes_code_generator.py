from random import randint as rand

code = "L20160366202000"

while len(code) != 19: # Each code is 19 characters long
    code += str(rand(0, 9))

print(code)