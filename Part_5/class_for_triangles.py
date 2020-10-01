class Triangles:
    """
    class for calculating the circumference and the area of the triangles
    """
    def __init__ (self, b, c):
        # self.c_x = c[0] also works for unpacking
        self.b_x, self.b_y = b
        self.c_x, self.c_y = c

    def circumference(self):
        ab = (self.b_x**2 + self.b_y**2)**0.5
        ac = (self.c_x**2 + self.c_y**2)**0.5
        bc = (((self.b_x+self.c_x)/2) ** 2 + ((self.b_y-self.c_y)/2) ** 2) ** 0.5
        return ab+ac+bc

    def area(self):
        xb, yb = self.b_x, self.b_y
        xc, yc = self.c_x, self.c_y
        a = abs(xb*yc - xc*yb)/2
        return a

my_triangle = Triangles((3,0), (0,4))
print(my_triangle.circumference())
# print(my_triangle.area())
# r1 = Triangles()
# r1.name = "Tom"




