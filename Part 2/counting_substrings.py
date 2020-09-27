string = "banana"
substring = "nanan"
def count_substring(substring,string):
    count = 0
    for s in range(len(string)):
        if string[s:s+len(substring)] == substring:
            count += 1
    return count

print(count_substring(substring,string))

