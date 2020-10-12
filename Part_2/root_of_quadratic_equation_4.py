"""
Test
a = 2
b = 5
c = 2
"""
import math
# a = float(input("what is a?"))
# b = float(input("what is b?"))
# c = float(input("what is c?"))

def user_input ():
    abc = input("what is the a, and c? >")
    input_l = abc.split(" ")
    a = float(input_l[0])
    b = float(input_l[1])
    c = float(input_l[2])
    return a, b, c

# passing the return value in to a global variable
a, b, c = user_input()

def f(a, b, c):
    discr = b**2 - 4 * a * c
    print(discr)
    if discr > 0:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        ans_l = [x1,x2]
        return ans_l
    else:
        return "sorry :("


print (f(a, b, c))