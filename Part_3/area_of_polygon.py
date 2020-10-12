def area_polygon (a_list):
    x_list = []
    y_list = []
    sum1 = []
    ans2 = 0
    for t , e in a_list:
        x_list.append(t)
        y_list.append(e)
    for i in range(len(a_list)):
        s = x_list[i-1] * y_list[i]
        y = x_list[i] * y_list[i-1]
        ans = s - y
        sum1.append(ans)
    for i2 in sum1:
        ans2 += i2
    area = ans2/2
    return abs(area)

a_list = [(4,10),(9,7),(11,2),(2,2)]
print(area_polygon(a_list))

def polygon_area(list):
    total = 0
    for n in range(-1,len(list)-1):
        sp = list[n+1][0]-list[n][0]
        avgheight = (list[n][1]+list[n+1][1])/2
        area = sp * avgheight
        total += area
    return abs(total)
print(polygon_area(a_list))

def polygon_area_class(list):
    total = 0

    for i in range(-1,len(list)-1):
        x1 = list[i][0]
        y1 = list[i][1]
        x2 = list[i+1][0]
        y2 = list[i+1][1]

        width = x2 - x1
        avgheight = (y1+y2)/2
        area = width * avgheight
        total += area
    return abs (total)
print (polygon_area_class(a_list))
