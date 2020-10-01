import math
class Polygon:
    def __init__(self, list_of_points):
        self.points = list_of_points

    def overwriting(self):
        new_list = input("New coordinates?\n")
        n_list_split = new_list.split()
        n_list = []
        for i in range(len(n_list_split)):
            if i % 2 == 0:
                x = n_list_split[i]
                y = n_list_split[i+1]
                xy = (x,y)
                n_list.append(xy)
        self.points = n_list

    def area(self):
        total = 0

        for i in range(-1, len(self.points) - 1):
            x1 = self.points[i][0]
            y1 = self.points[i][1]
            x2 = self.points[i + 1][0]
            y2 = self.points[i + 1][1]

            width = x2 - x1
            avgheight = (y1 + y2) / 2
            area = width * avgheight
            total += area
        print(abs(total))

    def perimeter(self):
        p = 0
        for i in range(-1, len(self.points) - 1):
            x1 = self.points[i][0]
            y1 = self.points[i][1]
            x2 = self.points[i + 1][0]
            y2 = self.points[i + 1][1]

            x_difference = x2 - x1
            y_difference = y2 - y1
            d = (x_difference)**2 + (y_difference)**2
            sqrt_d = math.sqrt(d)
            p += sqrt_d
        print(p)

    def bounding_box(self):
        x = []
        y = []
        for i in range(len(self.points)):
            for j in range(len(self.points[i])):
                if j % 2 == 0:
                    x.append(self.points[i][j])
                else:
                    y.append(self.points[i][j])
        min_x = min(x)
        max_x = max(x)
        min_y = min(y)
        max_y = max(y)
        print((min_x, min_y), (max_x, max_y))

    def moving_vector(self):
        vector = input("How much do you want to move?[dx,y number]\n")
        sign = input("Addition or subtraction?[+ or -]\n")
        n_list = []
        for i in range(len(self.points)):
            for j in range(len(self.points[i])):
                if j % 2 == 0:
                    x = self.points[i][j]
                    y = self.points[i][j+1]
                    v_split = vector.split()
                    if "dx" in v_split[0]:
                        if "+" in sign:
                            n_x = x + float(v_split[1])
                            xy = (n_x, y)
                            n_list.append(xy)
                        elif "-" in sign:
                            n_x = x - float(v_split[1])
                            xy = (n_x, y)
                            n_list.append(xy)
                    elif "dy" in vector[0]:
                        if "+" in sign:
                            n_y = y + float(v_split[1])
                            xy = (x, n_y)
                            n_list.append(xy)
                        elif "-" in sign:
                            n_y = y - float(v_split[1])
                            xy = (x, n_y)
                            n_list.append(xy)
        print (n_list)



x = [(4,10),(9,7),(11,2),(2,2)]
poly1 = Polygon(x)
poly1.area()
poly1.perimeter()
poly1.bounding_box()
poly1.moving_vector()