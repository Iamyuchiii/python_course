list_1 = [3,-2,0,1]
list_2 = [3,4,2,-5]

def inner_product(list1, list2):
    sum_list = []
    sum = 0
    for e1,e2 in zip(list_1,list_2):
        c = e1 * e2
        sum_list.append(c)
    for e in sum_list:
        sum += e
    return sum

print (inner_product(list_1,list_2))

# # index way (better)
# def inprod(a, b):
#     if len(a) == len(b):
#         sum = 0
#         for i in range(len(a)):
#             sum += (a[i]*b[i])
#         return sum
#     else:
#         return False
#
# print(inprod([1,2,3,4],[3,4,2,3]))