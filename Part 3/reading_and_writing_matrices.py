data = [[35, 12, 6], [-32, 5, -26], [10, 8, -1]]

def writing_file (list_list, filename):
    with open(filename, "w") as f:
        for e in list_list:
            # only works for 3 variable in the list
            # f.write('{0} {1} {2}'.format(*e) + '\n')
            # also works, but is longer
            print (*e, file = f)

writing_file(data, "new.txt")