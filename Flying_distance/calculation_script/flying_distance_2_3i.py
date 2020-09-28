from flying_distances_1 import distance
from string_splitting import str_split

import re # re.sub("[^0-9]", "", string) to remove every non numbers
lat1 = input('Give the latitude for city 1 >\n')
lon1 = input('Give the longitude for city 1 >\n')
lat2 = input('Give the latitude for city 2 >\n')
lon2 = input('Give the longitude for city 2 >\n')

def ASCII_convertion(deg, min):
    """
    :param latdeg: degrees
    :param lonmin: minutes
    :return: removing non nummuric elements in the strings
    """
    n_deg = ""
    n_min = ""
    # identifying the non nummeric elements in the string and removing it
    for char in deg:
        # if char.isdigit(): Also works
        if ord("0") <= ord(char) and ord(char) <= ord("9"):
            n_deg = n_deg + char
    # minutes can be fill as a blank so returning blank as value 0
    if min == "":
        n_min = 0
    else:
        # identifying the non nummeric elements in the string and removing it
        for char in min:
            if ord("0") <= ord(char) and ord(char) <= ord("9"):
                n_min = n_min + char
    # returning all values into floats
    return float(n_deg), float(n_min)

# Amsterdam: 52° 22’ N and 4° 32’ E
# Montreal: 45° 30’ N and 73° 35’ W

def distance_cal (lat1,lon1,lat2,lon2):
    """
    :param lat1: latitute of the first city
    :param lon1: lontitude of the first city
    :param lat2: latitute of the second city
    :param lon2: lontitute of the second city
    :return: the distance between the city
    """
    # splitting the the degree, min and sign into seperate string
    lat1deg, lat1min, lat1sign = str_split(lat1)
    lon1deg, lon1min, lon1sign = str_split(lon1)
    lat2deg, lat2min, lat2sign = str_split(lat2)
    lon2deg, lon2min, lon2sign = str_split(lon2)
    # Using ASCII_convertion to eliminate the signs in degree and min
    lat1deg, lat1min = ASCII_convertion(lat1deg, lat1min)
    lon1deg, lon1min = ASCII_convertion(lon1deg, lon1min)
    lat2deg, lat2min = ASCII_convertion(lat2deg, lat2min)
    lon2deg, lon2min = ASCII_convertion(lon2deg, lon2min)
    # calculating the distance between the cities using the right value
    dis = distance(lat1deg,lat1min,lat1sign,lon1deg,lon1min,lon1sign,lat2deg,lat2min,lat2sign,lon2deg,lon2min,lon2sign)
    return dis
# print (distance_cal((52, 22, 'N'), (4, 32, 'E'), (45, 30, 'N'), (73, 35, 'W')))
print(distance_cal(lat1,lon1,lat2,lon2))