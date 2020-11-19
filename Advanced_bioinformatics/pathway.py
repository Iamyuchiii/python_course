import scipy

def parseexpression(filename):
    with open(filename) as data:
        data_dict = {}
        temp_dict = {}
        for index, line in enumerate(data):
            if line.strip():
                if index == 0:
                    headerline = line.strip().split("\t")
                    for header in headerline[1:]:
                        temp_dict[header] = ""
                else:
                    otherlines = line.strip().split("\t")
                    for element, header in zip(otherlines[1:], list(temp_dict)):
                        temp_dict[header] = element
                        data_dict[otherlines[0]] = temp_dict
    return data_dict

def parseKEGG(filename):
    with open(filename) as data:
        KEGG_dict = {}
        for index,line in enumerate(data):
            if index != 0:
                stripline = line.strip().split("\t")
                KEGG_dict[stripline[0]] = stripline[1]
    return KEGG_dict


if __name__ == "__main__":
    expression_data = parseexpression("20181122_Sclav_data.txt")
    KEGG = parseKEGG("20181122_Sclav_data_KEGG.txt")
    pathway = parseKEGG("20181122_Sclav_data_pathway.txt")