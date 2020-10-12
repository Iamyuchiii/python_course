string = "babanana"
substring = "ba"
def count_substring(substring,string):
    for s in range(len(string)):
        if string[s:s + len(substring)] == substring:
            string = string[0:s] + string[s + len(substring):]
    return string


print(count_substring(substring, string))