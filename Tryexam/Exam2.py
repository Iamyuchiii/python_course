"""
quaestion 2a + b
"""
def high_low (number):
    if number > 1:
        lowest = 1
        highets = number
    elif 0 <= number <= 1:
        lowest = number
        highets = 1
    else:
        raise ValueError("the number is 0 or below 0")

    return  lowest, highets

def sqaure_est(number, requirement):
    low, high = high_low(number)
    interval = high - low
    answers = [1, number]

    while interval > requirement:
        mid = (low + high)/2
        mid2 = mid**2
        answers += [mid]
        if mid2 > number:
            high = mid
        else:
            low = mid

        interval = high - low
    return answers[len(answers)-1]

print (sqaure_est(2, 0.2))

"""
question 3
"""
def program_options (default, optional, filename):
    with open(filename, "w") as f:
        for item in optional:
            if item in default:
                if default[item] != optional[item]:
                    f.write(item + ' = ' + optional[item] + '\n' )
            else:
                f.write(item + ' = ' + optional[item] + '\n' )

"""
question 4 a + b
"""
def line_processing(line):
    elements = line.split()
    x_start = elements[1][2:-1]
    y_start = elements[2][2:]
    x_end = elements[4][2:-1]
    y_end = elements[5][2:]
    x_start = float(x_start)
    y_start = float(y_start)
    x_end = float(x_end)
    y_end = float(y_end)
    return x_start, y_start, x_end, y_end

def list_segments(filename):
    list_of_segments = []
    with open(filename, "r") as f:
      for line in f:
          x_start, y_start, x_end, y_end = line_processing(line)
          list_of_segments += [((x_start, y_start), (x_end, y_end))]
    return list_of_segments

