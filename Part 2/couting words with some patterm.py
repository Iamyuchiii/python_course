list_r = ["write", "some", "function", "that", "takes", "some", "list"]
pattern = "so"

def pattern_finder (list_of_string, pattern):
    total = 0
    for s in list_of_string:
        if pattern in s:
            total += 1
    return total

print(pattern_finder(list_r, pattern))