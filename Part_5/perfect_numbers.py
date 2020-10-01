def f_divisors (number):
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def isperfect(number):
    divisors = f_divisors(number)
    # can also
    # proper_divisors = divisors[:-1]
    # return sum(proper_divisors) == number
    return sum(divisors) == 2*number

def print_perfect_number(limit):
    for i in range(1, limit+1):
        if isperfect(i):
            print(i, "is perfect")

print_perfect_number(10000000000)