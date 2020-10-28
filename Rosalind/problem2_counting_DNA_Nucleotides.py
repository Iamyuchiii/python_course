#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 5
"""

# import statements
from sys import argv

def parse_input(filename):
    """
    Parsing the content into a string
    :param filename: the path to the file
    :return: a and b value extracted from the file
    """
    with open(filename, "r") as f:
        # the first line is the DNA
        DNA = f.readline()
        return DNA

def count_DNA(DNA):
    """
    Counts the number of A, C, G and T in string DNA
    :param DNA: a string of DNA
    :return: total numbers of A, C, G and T
    """
    A = DNA.count("A")
    C = DNA.count("C")
    G = DNA.count("G")
    T = DNA.count("T")
    return A, C, G, T

def write_results(filename, result):
    """
    Write the result into the filename
    :param filename: path to write the file (or filename without a path)
    :param result: the result of rosalind
    :return: the file written in the specified path (or filename)
    """
    with open(filename, "w") as f:
        A, C, G, T = result
        f.write(f"{A} {C} {G} {T}")

if __name__ == "__main__":
    # specify the filename and resultfile name
    filename = argv[1]
    writefilepath = argv[2]
    # parse the values in the file
    DNA = parse_input(filename)
    # counting the total numbers of nucleotides
    result = count_DNA(DNA)
    A , C, G, T = count_DNA(DNA)
    print (f"{A} {C} {G} {T}")
    # writing the result to a writefilepath
    write_results(writefilepath, result)


