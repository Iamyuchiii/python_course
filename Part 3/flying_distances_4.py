def flying_data():
    # amsterdam = ('Amsterdam', (52, 22, 'N'), (4, 32, 'E'))
    # name, lon, lat = amsterdam
    city1, lon1, lat1= ('amsterdam', (52, 22, 'N'), (4, 32, 'E'))
    city2, lon2, lat2 = ("montreal", (45, 30, "N"), (73, 35, "W"))
    city3, lon3, lat3 = ("auckland", (36, 52, "S"), (174, 45, "E"))
    data_dict = {}
    data_dict[city1] = city1, lon1, lat1
    data_dict[city2] = city2, lon2, lat2
    data_dict[city3] = city3, lon3, lat3
    return data_dict

print(flying_data())