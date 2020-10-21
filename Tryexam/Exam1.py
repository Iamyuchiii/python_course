# """
# question 2
# """
#
# def koch_curve (n):
#     if n == 0:
#         curve = "F"
#     else:
#         prev= koch_seq (n-1)
#         curve = prev + "L" + prev + "R" + prev + "L" + prev
#     return curve
#
#
# def koch_seq(n):
#     curve = "F"
#     for i in range(n):
#         curve = curve + 'L' + curve+ 'R' + curve+ 'L' + curve
#     return curve
#
# print (koch_curve(3))

"""
question 4
"""
def count_primes (n):
    count = 0
    for i in range(2, n+1):
        prime = True
        for j in range (2,i):
            if i%j == 0:
                prime = False
        if prime:
            count += 1
    return count
print (count_primes(10))

"""
question 5a
"""
import math
def on_circle(coords, center, dist):
    circle = True
    i = 0
    while circle and i < len(coords):
        x, y = coords[i]
        i_dis = math.sqrt((center[0]-x)**2+(center[1]-y)**2)
        if i_dis != dist:
            circle = False
        i += 1
    return circle

"""
question 5b
"""
data = {'entry498': ([(4,3),(2,3),(3,2)], (3,3), 1),
        'entry499': ([(5,3),(3,5),(3,1)], (3,3), 2),
        'entry500': ([(4,3),(2,3),(3,3)], (3,3), 1),
        'entry501': ([(4,3),(2,3),(3,1)], (3,3), 1)}

def circle_dict_to_file(dataset, output):
    with open(output, "w") as f:
        for key, value in dataset.items():
            # coords = value[0]
            # center = value[1]
            # dist = value[2]
            if on_circle(value[0], value[1], value[2]):
                f.write("{} is a circle \n".format(key))
            else:
                f.write("{} is not a circle \n".format(key))

circle_dict_to_file(data, "exam5b.txt")