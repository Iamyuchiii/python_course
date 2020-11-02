#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 4
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
        # read all lines
        for line in f:
            # removing all possible enters
            DNA = line.replace("\n","")
        return DNA

def reverse_complement(DNA):
    """
    Computing the reverse DNA from the input DNA
    :param DNA: a string of DNA
    :return: the reverse complement of the DNA (3` - 5`)
    """
    DNA_complement = {"A" : "T", "C" : "G", "T" : "A", "G" : "C"}
    complement = ""
    for n in DNA:
        # for each n in DNA, the complement is taken out and added to the variable complement
        complement = DNA_complement[n] + complement # this adds the strings in reverse
    return complement

def write_results(filename, result):
    """
    Write the result into the filename
    :param filename: path to write the file (or filename without a path)
    :param result: the result of rosalind
    :return: the file written in the specified path (or filename)
    """
    with open(filename, "w") as f:
        f.write(result)

if __name__ == "__main__":
    # specify the filename and resultfile name
    filename = argv[1]
    writefilepath = argv[2]
    # parse the values in the file
    DNA = parse_input(filename)
    # reversing the DNA
    result = reverse_complement(DNA)
    print (result)
    # writing the result to a writefilepath
    write_results(writefilepath, result)



