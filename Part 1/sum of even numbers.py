def sum_add (number):
    sum = 0
    for i in range(number+1):
        if i%2 == 0:
            sum += i
    return sum

print(sum_add(10))