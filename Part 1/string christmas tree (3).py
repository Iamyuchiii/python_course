# 13 stars at the bottom
def chris_tree (height):
    star = "*"
    space = " "
    bar = "|"
    newline = "\n"
    for i in range(1, height+1):
        if i != 0:
            tree = bar + i*space + star
    bottom = (height-1)*space + bar
    # top = bar + 6*space + star + 6*space + bar
    # tree_1 = bar + 5*space + 3*star + 5*space + bar
    # tree_2 = bar + 4*space + 5*star + 4*space + bar
    # tree_3 = bar + 3*space + 7*star + 3*space + bar
    # tree_4 = bar + 2*space + 9*star + 2*space + bar
    # tree_5 = bar + space + 11*star + space + bar
    # tree_6 = bar + 13*star + bar
    # bottom = 7*space + bar
    # tree = top + newline + tree_1 + newline + tree_2 + newline + tree_3 + newline + tree_4 + newline + tree_5 + newline + tree_6 + newline + bottom


print (chris_tree(8))

