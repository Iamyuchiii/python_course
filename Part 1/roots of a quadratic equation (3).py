import math
a = float(input("what is a?"))
b = float(input("what is b?"))
c = float(input("what is c?"))
def f(a,b,c):
    discr = b**2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return "discr is " + str(discr), "x1 is " + str(x1), "x2 is " + str(x2)
    else:
        return "sorry :("

print (f(a,b,c))