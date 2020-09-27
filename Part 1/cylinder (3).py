# # solution 1
# import math
# radius = float(input("what is the radius of the cylinder?"))
# height = float(input("what is the height of the cylinder?"))
# # area cylinder =  π * r * r
# # volume = area x height
# area = math.pi * radius * radius
# volume =  area * height
# print("The area of the cylinder is " + str(area) + " and the volume of the cylinder is " + str(volume))

# solution 2 (def)

def S_area_calculator(radius, height):
    import math
    # S_area = 2pi*r*r + 2pi*r*h
    S_area = (2*math.pi*radius**2) + (2*math.pi*radius*height)
    return S_area

print (S_area_calculator(5,6))

def volume_calculator (radius, height):
    import math
    # area cylinder =  π * r * r
    # volume = area x height
    area = math.pi * radius * radius
    volume =  area * height
    # no need to print!!! otherwise you get a none back
    ans = "The area of the cylinder is " + str(area) + " and the volume of the cylinder is " + str(volume)
    return ans

# print (volume_calculator(1,1))