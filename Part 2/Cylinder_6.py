def main():
    c = "Y"
    while c == "Y":
        prompt_user()
        c = input("continue Y/N?")
        c = c.upper()
    if c == "N":
        print ("Program terminated")

# function where input is asked in one go
def prompt_user():
    user_input = input("what is the radius and height?")
    # this def can be replace by split
    radius, height = str_split(user_input)
    radius, height = float(radius), float(height)
    s_area, volume = area_volume_calculator(radius, height)
    print ("surface area is " + str(s_area),"volume is " + str(volume))

# # function where the input is asked one by one
# def prompt_user ():
#     radius_i = input("what is the radius?")
#     height_i = input("what is the height?")
#     radius_i = float(radius_i)
#     height_i = float(height_i)
#     s_area, volume = area_volume_calculator(radius_i,height_i)
#     print (s_area, volume)

def str_split(textual):
    first_space = None
    for i in range(len(textual)):
        if textual[i] == ' ':
            if first_space == None:
                first_space = i
    first = textual[:first_space]
    last = textual[first_space +1:]
    return first, last

def area_volume_calculator (radius, height):
    import math
    # s_area = 2pi*r^2 + 2pi*r*h
    s_area = (2*math.pi*radius**2) + (2*math.pi*radius*height)
    # area cylinder =  π * r * r
    # volume = area x height
    area = math.pi * radius * radius
    volume =  area * height
    return s_area, volume

main()