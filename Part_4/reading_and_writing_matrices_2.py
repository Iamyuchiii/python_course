data = [[35, 12, 6], [-32, 5, -26], [10, 8, -1]]

# def writing_file (list_list, filename):
#     with open(filename, "w") as f:
#         for e in list_list:
#             # only works for 3 variable in the list
#             # f.write('{0} {1} {2}'.format(*e) + '\n')
#             # also works, but is longer
#             print (*e, file = f)
#
# writing_file(data, "new.txt")

def reading_file(filename):
    with open(filename, "r") as f:
        clean = []
        matrix = []
        # cleaning the file
        for line in f:
            temp = []
            line.strip()
            if line != "\t":
                s = line.replace(" ", ",")
                s1 = s.replace("\n", "")
                temp.append(s1)
                clean.append(temp)
        # sorting the clean and return the matrix
        for l in clean:
            split_value = l[0].split(",")
            temp = []
            for e in split_value:
                temp.append(int(e))
            matrix.append(temp)
        print(matrix)

reading_file("new.txt")
