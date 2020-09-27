from distance_cal import distance

dic = {
    'Amsterdam' : ('Amsterdam', (52, 22, 'N'), (4, 32, 'E')),
    'Montreal'  : ('Montreal', (45, 30, 'N'), (73, 35, 'W')),
    'Auckland'  : ('Auckland', (36, 52, 'S'), (174, 45, 'E'))
    }


def ASCII_convertion(deg, min):
    """
    :param latdeg: degrees
    :param lonmin: minutes
    :return: removing non nummuric elements in the strings
    """
    n_deg = ""
    n_min = ""
    # identifying the non nummeric elements in the string and removing it
    for char in str(deg):
        # if char.isdigit(): Also works
        if ord("0") <= ord(char) and ord(char) <= ord("9"):
            n_deg = n_deg + char
    # minutes can be fill as a blank so returning blank as value 0
    if min == "":
        n_min = 0
    else:
        # identifying the non nummeric elements in the string and removing it
        for char in str(min):
            if ord("0") <= ord(char) and ord(char) <= ord("9"):
                n_min = n_min + char
    # returning all values into floats
    return float(n_deg), float(n_min)

def distance_cal (lat1,lon1,lat2,lon2):
    """
    :param lat1: latitute of the first city
    :param lon1: lontitude of the first city
    :param lat2: latitute of the second city
    :param lon2: lontitute of the second city
    :return: the distance between the city
    """
    # splitting the the degree, min and sign into seperate string
    lat1deg, lat1min, lat1sign = lat1
    lon1deg, lon1min, lon1sign = lon1
    lat2deg, lat2min, lat2sign = lat2
    lon2deg, lon2min, lon2sign = lon2
    # Using ASCII_convertion to eliminate the signs in degree and min
    lat1deg, lat1min = ASCII_convertion(lat1deg, lat1min)
    lon1deg, lon1min = ASCII_convertion(lon1deg, lon1min)
    lat2deg, lat2min = ASCII_convertion(lat2deg, lat2min)
    lon2deg, lon2min = ASCII_convertion(lon2deg, lon2min)
    # calculating the distance between the cities using the right value
    dis = distance(lat1deg,lat1min,lat1sign,lon1deg,lon1min,lon1sign,lat2deg,lat2min,lat2sign,lon2deg,lon2min,lon2sign)
    return dis
# print (distance_cal((52, 22, 'N'), (4, 32, 'E'), (45, 30, 'N'), (73, 35, 'W')))

header = [""]
header_format = '%10s%10s%10s%10s\n'
maxtrix_format = "%s%10.3f%10.3f%10.3f\n"

for head in sorted(dic):
    header.append(head)

for head in sorted(dic):
    name1, lat1, lon1 = dic[head]
    # lat1 = " ".join([str(i) for i in lat1])
    # lon1 = " ".join([str(i) for i in lon1])
    distance = [head]

    for head2 in sorted(dic):
        name2, lat2, lon2 = dic[head2]
        # lat2 = " ".join([str(i) for i in lat2])
        # lon2 = " ".join([str(i) for i in lon2])
        matrix = distance_cal(lat1,lon1,lat2,lon2)




# def flying_table (filename, dict):
# #     print (dic)
# #
# # flying_table("s",dic)



