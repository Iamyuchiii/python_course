def convertion_number_digit (number, base):
    digit_list = []
    while number != 0:
        last_digit = number % base
        digit_list.insert(0,last_digit)
        number = number // base
        print (last_digit)
        print (number)
    return digit_list
print (convertion_number_digit(1537246, 7))