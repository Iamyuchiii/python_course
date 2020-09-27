"""
Repeating programs
"""
def repeat_program ():
    """
    Def to repeat the program
    :return:
    if Y is given as input: repeat the given program
    if N is given as input: terminate the program
    """
    con = "Y"
    while con == "Y":
        user_input = input("Repeat the program? Y/N")
        con = user_input.upper()
        # replace this line with the program that needed to be repeated!!!
        if con == "N":
            return "Program terminated"

"""
Converting to ASCII 
(ord = from char to digit)
(chr = from digit to char)
"""
def ASCII_convertion(string):
    """
    converting string to ASCII to remove non_numeric elements
    """
    n_string = ""
    # identifying the non nummeric elements in the string and removing it
    for char in string:
        # if char.isdigit(): Also works
        if ord("0") <= ord(char) and ord(char) <= ord("9"):
            n_string = n_string + char
    return n_string

