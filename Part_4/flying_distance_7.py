import re
# controller functie
def read_fd (filename):

    data = {}

    # file open
    this_file = open(filename, 'r')

    # for loopje
        # dingen in de dict zeeten

    for line in this_file:
        city = process_line(line)
        name = city[0]
        data[name]= city

    # dicht doen....
    this_file.close()

    return data

def process_line(line):
# to do line slopen tot city tuple
##    tokens = line.split()
##    name = tokens[1]
##    tag_lat = tokens[2]
##    lat_deg = tokens[3] # include graden symbool
##

# using reg expressions

    ll_pat = "([0-9]+). ([0-9]+).([NSEW])"
    pattern = r'Name: (.*) Latitude: '+ ll_pat + 'Longitude: '+ ll_pat
    matcher = re.compile(pattern)
    match = matcher.search(line)

    name = match.group(1)

    lat_deg = match.group(2)
    lat_min = match.group(3)
    lat_dir = match.group(4)
    lon_deg = match.group(5)
    lon_min = match.group(6)
    lon_dir = match.group(7)

    lat_deg = int(lat_deg)
    lat_min = int (lat_min)
    lon_deg = int(lon_deg)
    lon_min = int (lon_min)

    lat = (lat_deg, lat_min, lat_dir)
    lon = (lon_deg, lon_min, lon_dir)

    return (name,lat, lon)




    return city_tuple
