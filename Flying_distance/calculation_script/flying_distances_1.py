import math

def convertion (sign, degrees, minutes):
    if sign == "N" or sign == "W":
        sign = 1
    elif sign == "S" or sign == "E":
        sign = -1
    else:
        return "Ops you can only chose between N,W,S,E"
    # radius convertion (d_r = degrees/radius)
    r_d = math.pi / 180
    # minutes convertion
    m_d = 1/60
    # final steps
    m = minutes * m_d
    convertion = (degrees + m) * r_d * sign
    return convertion



def haversine (lat1, lat2, lon1, lon2):
    # haversine splits in 3 parts
    p1 = math.sin(((lat2-lat1)/2))**2
    p2 = math.cos(lat1) * math.cos(lat2)
    p3 = math.sin(((lon2-lon1)/2))**2
    # calculating a^2 and a
    a_2 = p1 + p2 * p3
    a = math.sqrt(a_2)
    # calculating b^2 and b
    b_2 = 1 - a_2
    b = math.sqrt(b_2)
    # finally the distance
    distance = 2 * math.atan2(a,b)
    return distance

def distance (sign_1LA, degrees_1LA, minutes_1LA,
             sign_1LO, degrees_1LO, minutes_1LO,
             sign_2LA, degrees_2LA, minutes_2LA,
             sign_2LO, degrees_2LO, minutes_2LO):
    lat1 = convertion(sign_1LA, degrees_1LA, minutes_1LA)
    lon1 = convertion(sign_1LO, degrees_1LO, minutes_1LO)
    lat2 = convertion(sign_2LA, degrees_2LA, minutes_2LA)
    lon2 = convertion(sign_2LO, degrees_2LO, minutes_2LO)
    h = haversine(lat1, lat2, lon1, lon2)
    dis = h * 6367
    return dis


# print (haversine(1.5707963,0,0,0))