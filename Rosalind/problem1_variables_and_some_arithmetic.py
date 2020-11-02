#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 1
"""

# import statements
from sys import argv

def parse_input(filename):
    """
    Extracts the a and b value from the filename
    :param filename: the path to the file
    :return: a and b value extracted from the file
    """
    with open(filename, "r") as f:
        for line in f:
            # strip the line and split it
            a, b = line.strip().split()
            return int(a), int(b)

def pythagoras(a,b):
    """
    calculates the revc using a and b
    :param a: a numeric value
    :param b: a numeric value
    :return: the total value of a**2 + b**2
    """
    c = a**2+b**2
    return c

def write_results(filename, result):
    """
    Write the result into the filename
    :param filename: path to write the file (or filename without a path)
    :param result: the result of rosalind
    :return: the file written in the specified path (or filename)
    """
    with open(filename, "w") as f:
        f.write(f"{result}")

if __name__ == "__main__":
    # specify the filename and resultfile name
    filename = argv[1]
    writefilepath = argv[2]
    # parse the values in the file
    a, b = parse_input(filename)
    # calculate the result
    c = pythagoras(a, b)
    print (c)
    # writing the result to a writefilepath
    write_results(writefilepath, c)