import turtle
bob = turtle.Turtle()
yu = turtle.Turtle()
print(bob)

# dump 4 times for sqare
# bob.fd(100) # distance in pixel
# bob.lt(90) # lt for left turn (degrees) and rt for right turn (degrees)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

# smart to writing the same 4 times:
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)
square(yu)

# for i in range (4):
#     bob.fd(100)
#     bob.lt(90)
turtle.mainloop()



