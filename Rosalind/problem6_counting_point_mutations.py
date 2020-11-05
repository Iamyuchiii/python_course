#!/usr/bin/env python3

"""
Author: Yuchen Huang
Script to solve problem 6
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
        # read the whole file and covert the tow DNA's into a list
        DNA_strings = f.read().split("\n")
        # removing possible empty spaces
        DNA_strings.remove("")
        return DNA_strings

def point_mutation_counting(DNA1,DNA2):
    """
    Counts the total mutation number from 2 equally long DNA
    :param DNA1: DNA string 1
    :param DNA2: DNA string 2
    :return: total numbers of mutation between DNA1 and DNA2
    """
    mutation = 0
    # for the length of DNA, because both DNA have the same length
    for d in range(len(DNA1)):
        # if string slicing each position for both DNA if they are the same
        if DNA1[d] != DNA2[d]:
            #if not the mutation count up
            mutation += 1
    return mutation

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
    DNA1, DNA2 = parse_input(filename)
    # counting the total numbers of mutations between DNA1 and DNA2
    result = point_mutation_counting(DNA1, DNA2)
    print (result)
    # writing the result to a writefilepath
    write_results(writefilepath, result)