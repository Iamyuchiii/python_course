def limit (x,lb,ub):
    if x >= lb and x <= ub:
        return x
    elif x <= lb:
        return lb
    else:
        return ub
print(limit(0,0,2))