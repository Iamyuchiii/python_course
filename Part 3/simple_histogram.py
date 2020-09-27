n_list = [9,18,13,9,6,6,16,6,17,10,15,16,13,11,13,8,20,6,18,11]

def simple_h (n_list):
    dic_list = {}
    for n in n_list:
        if n not in dic_list:
            dic_list[n] = 1
        else:
            dic_list[n] += 1

    maximum = max (n_list)
    minimum = min (n_list)

    for i in range(minimum, maximum+1):
        if i in dic_list.keys():
            print (i, dic_list[i] * "#")
        else:
            print (i)

simple_h(n_list)



