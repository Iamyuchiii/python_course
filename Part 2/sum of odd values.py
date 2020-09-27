sum_list = [3, 5, 8, 1, -1, 39, 20]
def sum_odd_value (list):
    sum_odd = 0
    for e in sum_list:
        if e % 2 == 1:
            sum_odd += e
    return sum_odd

print (sum_odd_value(sum_list))
