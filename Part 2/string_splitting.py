# first solution
def str_split(textual):
    first_space = None
    last_space = None
    for i in range(len(textual)):
        if textual[i] == ' ':
            if first_space == None:
                first_space = i
            last_space = i
    first = textual[:first_space]
    middle = textual[first_space + 1:last_space]
    last = textual[last_space + 1:]
    return first, middle, last

print (str_split("52 22 N"))