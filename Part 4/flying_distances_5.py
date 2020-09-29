data = {
"amsterdam" : (("amsterdam"), (55, 22, "N"), (4, 32, "E")),
"montreal": (("montreal"), (45, 30, "N"), (73, 35, "W")),
"auckland": (("auckland"), (36, 52, "S"), (174, 45, "E"))
}

# def write_data (filename, dict):
#     with open(filename,"w") as f:
#         for key, value in dict.items():
#             print("name:", value[0], "latitudes:", str(value[1][0]) + chr(176), str(value[1][1]) + "'", value[1][2], "longitudes:", str(value[2][0]) + chr(176), str(value[2][1]) + "'", value[2][2], file = f)
#
# write_data("flying5.txt", data)

def write_data_c (filename, dict):
    deg_sign = chr(176)
    with open(filename,"w") as f:
        for key in dict:
            name, latitude, longitude = dict[key]
            lon_deg, lon_min, lon_dir = longitude
            lat_deg, lat_min, lat_dir = latitude

            format_print = "Name: %s " + "Latitude: %d%s %d' %s " + "Longtitude: %d%s %d' %s \n"

            value = (name, lat_deg, deg_sign, lat_min, lat_dir, lon_deg, deg_sign, lon_min, lon_dir)
            f.write(format_print % value)
write_data_c("flying5.txt", data)