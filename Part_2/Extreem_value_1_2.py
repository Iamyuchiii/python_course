t_list = [0,4,5,6]
def find_max_min (n_list):
    maximum = t_list[0]
    minimum = t_list[0]
    index_max = 0
    index_min = 0
    for i in range(len(n_list)):
        if n_list[i] > maximum:
            maximum = n_list[i]
            index_max = i
        elif n_list[i] < minimum:
            minimum = n_list[i]
            index_min = i
    return maximum, index_max, minimum, index_min
print (find_max_min(t_list))
